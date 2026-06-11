from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.common.db import get_db
from app.territories import crud, schemas

router = APIRouter(prefix="/territories", tags=["territories"])


@router.post("/", response_model=schemas.TerritoryRead, status_code=status.HTTP_201_CREATED)
def create_territory(data: schemas.TerritoryCreate, db: Session = Depends(get_db)):
    return crud.create_territory(db, data)


@router.get("/", response_model=List[schemas.TerritoryRead])
def list_territories(limit: int = 100, offset: int = 0, db: Session = Depends(get_db)):
    return crud.list_territories(db, limit=limit, offset=offset)


@router.get("/intersects", response_model=List[schemas.TerritoryRead])
def list_intersecting_territories(wkt: str, limit: int = 100, offset: int = 0, db: Session = Depends(get_db)):
    return crud.list_intersecting_territories(db, wkt, limit=limit, offset=offset)


@router.get("/{territory_id}", response_model=schemas.TerritoryRead)
def get_territory(territory_id: int, db: Session = Depends(get_db)):
    territory = crud.get_territory(db, territory_id)
    if not territory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Territory not found")
    return territory


@router.put("/{territory_id}", response_model=schemas.TerritoryRead)
def update_territory(territory_id: int, data: schemas.TerritoryUpdate, db: Session = Depends(get_db)):
    territory = crud.update_territory(db, territory_id, data)
    if not territory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Territory not found")
    return territory


@router.delete("/{territory_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_territory(territory_id: int, db: Session = Depends(get_db)):
    if not crud.delete_territory(db, territory_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Territory not found")
    return None


@router.post("/{territory_id}/metrics", response_model=schemas.TerritoryMetricRead, status_code=status.HTTP_201_CREATED)
def create_metric(territory_id: int, data: schemas.TerritoryMetricCreate, db: Session = Depends(get_db)):
    territory = crud.get_territory(db, territory_id)
    if not territory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Territory not found")
    return crud.create_metric(db, territory_id, data)


@router.get("/{territory_id}/metrics", response_model=List[schemas.TerritoryMetricRead])
def list_metrics(territory_id: int, db: Session = Depends(get_db)):
    territory = crud.get_territory(db, territory_id)
    if not territory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Territory not found")
    return crud.list_metrics_by_territory(db, territory_id)


@router.put("/{territory_id}/metrics/{metric_id}", response_model=schemas.TerritoryMetricRead)
def update_metric(territory_id: int, metric_id: int, data: schemas.TerritoryMetricUpdate, db: Session = Depends(get_db)):
    territory = crud.get_territory(db, territory_id)
    if not territory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Territory not found")
    
    metric = crud.update_metric(db, metric_id, data)
    if not metric:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Metric not found")
    
    if metric.territory_id != territory_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Metric not found for this territory")
    
    return metric


@router.delete("/{territory_id}/metrics/{metric_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_metric(territory_id: int, metric_id: int, db: Session = Depends(get_db)):
    territory = crud.get_territory(db, territory_id)
    if not territory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Territory not found")
    
    if not crud.delete_metric(db, metric_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Metric not found")
    
    return None