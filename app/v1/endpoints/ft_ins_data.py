from typing import Annotated, Optional
from app.core.models import crud, models
from app.core.schemas import schemas
from fastapi import APIRouter, params
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.dependencies import *

router_inst = APIRouter(
    prefix='',
    tags=['addition']
)

### DATOS DE LAS MEDICIONES DE LOS SENSORES ###
@router_inst.get("/ft_insts")
def read_ftinsts(ft_ins_id: Annotated[Optional[int], params] = None, ft_ins_inst: Annotated[Optional[int], params] = None,
               db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    result = crud.get_data(db, models.Ft_inst_data, ft_ins_id=ft_ins_id, ft_ins_inst=ft_ins_inst)
    return result

@router_inst.post("/ft_inst")
async def post_ftinst(schema: schemas.FtInstCreate, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    dictionary = schema.dict()
    try:
        result = crud.create_data(db, schema, models.Ft_inst_data)
    except IntegrityError:
        raise HTTPException(status_code=500,
                            detail=f"[ft_ins_inst {dictionary['ft_ins_inst']}] does not exist in inst_features")
    db.close()
    return result

@router_inst.get("/ft_inst/{id}")
def read_ftinst(id: int, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    result = crud.get_data(db, models.Ft_inst_data, ft_ins_id=id)
    return result


@router_inst.put("/ft_inst/{id}")
def put_ftinst(id: int, schema: schemas.FtInstCreate, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    dictionary = schema.dict()
    try:
        result = crud.update_data(db, schema, models.Ft_inst_data, False,
                                  column_id=models.Ft_inst_data.ft_ins_id, id=id)
    except IntegrityError:
        raise HTTPException(status_code=500,
                            detail=f"[ft_ins_inst {dictionary['ft_ins_inst']}] does not exist in inst_features")
    return result


### DATOS AGREGADOS (1d) DE LAS MEDICIONES DE LOS SENSORES ###
@router_inst.get("/fta_inst/1day")
def read_fta_1dayinst(fta1d_ins_id: Annotated[Optional[int], params] = None, fta1d_ins_inst: Annotated[Optional[int], params] = None,
               db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    result = crud.get_data(db, models.Fta_1day_inst_data, fta1d_ins_id=fta1d_ins_id, fta1d_ins_inst=fta1d_ins_inst)
    return result

@router_inst.post("/fta_inst/1day")
async def post_fta_1dayinst(schema: schemas.Fta_1dayInstCreate, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    dictionary = schema.dict()
    try:
        result = crud.create_data(db, schema, models.Fta_1day_inst_data)
    except IntegrityError:
        raise HTTPException(status_code=500,
                            detail=f"[fta1d_ins_inst {dictionary['fta1d_ins_inst']}] does not exist in inst_features")
    db.close()
    return result

@router_inst.get("/fta_inst/1day/{id}")
def read_fta_1dayinst(id: int, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    result = crud.get_data(db, models.Fta_1day_inst_data, fta1d_ins_id=id)
    return result


### DATOS AGREGADOS (1h) DE LAS MEDICIONES DE LOS SENSORES ###
@router_inst.get("/fta_inst/1hour")
def read_fta_1hourinst(fta1h_ins_id: Annotated[Optional[int], params] = None, fta1h_ins_inst: Annotated[Optional[int], params] = None,
               db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    result = crud.get_data(db, models.Fta_1hour_inst_data, fta1h_ins_id=fta1h_ins_id, fta1h_ins_inst=fta1h_ins_inst)
    return result

@router_inst.post("/fta_inst/1hour")
async def post_fta_1hourinst(schema: schemas.Fta_1hourInstCreate, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    dictionary = schema.dict()
    try:
        result = crud.create_data(db, schema, models.Fta_1hour_inst_data)
    except IntegrityError:
        raise HTTPException(status_code=500,
                            detail=f"[fta1h_ins_inst {dictionary['fta1h_ins_inst']}] does not exist in inst_features")
    db.close()
    return result

@router_inst.get("/fta_inst/1hour/{id}")
def read_fta_1hourinst(id: int, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    result = crud.get_data(db, models.Fta_1hour_inst_data, fta1h_ins_id=id)
    return result