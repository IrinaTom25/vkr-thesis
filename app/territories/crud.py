from sqlalchemy.orm import Session
from sqlalchemy import func, select
from geoalchemy2 import WKTElement
from app.territories.models import Territory, TerritoryMetric
from app.territories import schemas


def _territory_select():
    return select(
        Territory.id,
        Territory.name,
        Territory.territory_type,
        Territory.level,
        Territory.description,
        func.ST_AsText(Territory.geom).label("geom_wkt"),
        Territory.created_at,
    )


def get_territory(db: Session, territory_id: int):
    stmt = _territory_select().where(Territory.id == territory_id)
    result = db.execute(stmt).first()
    return result._asdict() if result else None


def list_territories(db: Session, limit: int = 100, offset: int = 0):
    stmt = _territory_select().order_by(Territory.id).offset(offset).limit(limit)
    results = db.execute(stmt).all()
    return [row._asdict() for row in results]


def create_territory(db: Session, data: schemas.TerritoryCreate):
    geom = WKTElement(data.geom_wkt, srid=4326)
    db_territory = Territory(
        name=data.name,
        territory_type=data.territory_type,
        level=data.level,
        description=data.description,
        geom=geom,
    )
    db.add(db_territory)
    db.commit()
    db.refresh(db_territory)
    return get_territory(db, db_territory.id)


def update_territory(db: Session, territory_id: int, data: schemas.TerritoryUpdate):
    db_territory = db.query(Territory).filter(Territory.id == territory_id).first()
    if not db_territory:
        return None
    
    update_data = data.model_dump(exclude_unset=True)
    if "geom_wkt" in update_data and update_data["geom_wkt"]:
        update_data["geom"] = WKTElement(update_data.pop("geom_wkt"), srid=4326)
    
    for field, value in update_data.items():
        setattr(db_territory, field, value)
    
    db.commit()
    db.refresh(db_territory)
    return get_territory(db, territory_id)


def delete_territory(db: Session, territory_id: int) -> bool:
    db_territory = db.query(Territory).filter(Territory.id == territory_id).first()
    if not db_territory:
        return False
    db.delete(db_territory)
    db.commit()
    return True


def list_intersecting_territories(db: Session, wkt: str, limit: int = 100, offset: int = 0):
    search_geom = WKTElement(wkt, srid=4326)
    stmt = (
        _territory_select()
        .where(func.ST_Intersects(Territory.geom, search_geom))
        .order_by(Territory.id)
        .offset(offset)
        .limit(limit)
    )
    results = db.execute(stmt).all()
    return [row._asdict() for row in results]


def get_metric(db: Session, metric_id: int):
    return db.query(TerritoryMetric).filter(TerritoryMetric.id == metric_id).first()


def list_metrics_by_territory(db: Session, territory_id: int):
    return db.query(TerritoryMetric).filter(TerritoryMetric.territory_id == territory_id).order_by(TerritoryMetric.year).all()


def create_metric(db: Session, territory_id: int, data: schemas.TerritoryMetricCreate):
    db_metric = TerritoryMetric(territory_id=territory_id, **data.model_dump())
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return db_metric


def update_metric(db: Session, metric_id: int, data: schemas.TerritoryMetricUpdate):
    db_metric = get_metric(db, metric_id)
    if not db_metric:
        return None
    
    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_metric, field, value)
    
    db.commit()
    db.refresh(db_metric)
    return db_metric


def delete_metric(db: Session, metric_id: int) -> bool:
    db_metric = get_metric(db, metric_id)
    if not db_metric:
        return False
    db.delete(db_metric)
    db.commit()
    return True