from app.core.models import crud
from app.core.schemas import schemas
from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.dependencies import *

router_inst1 = APIRouter(
    prefix='',
    tags=['addition']
)

### DATOS DE LAS MEDICIONES DE LOS SENSORES (PARA LA INST1) ###
@router_inst1.get("/ft_inst1")
def read_ftinst1(db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_ftInst1s(db)
    if insts is None:
        raise HTTPException(status_code=404, detail="User not found")
    return insts

@router_inst1.post("/ft_inst1", response_model=schemas.FtInst1Create)
async def post_ftinst1(ft_inst: schemas.FtInst1Create, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    # info: Request,
    #req_info = await info.json()
    # "data" : req_info
    crud.create_ft_inst1(db, ft_inst)
    return ft_inst

@router_inst1.get("/ft_inst1/{id}")
def read_ftinst1(id: int, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_ftInst1(db, id)
    if insts == []:
        raise HTTPException(status_code=404, detail=f"ID ({id}) not found")
    return insts

@router_inst1.put("/ft_inst1/{id}")
def put_ftinst1(id: int, ft_inst: schemas.FtInst1Create, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    out = crud.update_ft_inst1(db, id, ft_inst)

    return out


### DATOS AGREGADOS DE LAS MEDICIONES DE LOS SENSORES (PARA LA INST1) ###
@router_inst1.get("/fta_inst1")
def read_ftainst1(db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_ftaInst1s(db)
    if insts is None:
        raise HTTPException(status_code=404, detail="User not found")
    return insts

@router_inst1.get("/fta_inst1/1day")
def read_fta_1dayinst1(db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_fta_1dayInst1s(db)
    if insts is None:
        raise HTTPException(status_code=404, detail="User not found")
    return insts

@router_inst1.post("/fta_inst1/1day", response_model=schemas.Fta_1dayInst1Create)
async def post_fta_1dayinst1(fta_1day_inst: schemas.Fta_1dayInst1Create, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    # info: Request,
    #req_info = await info.json()
    # "data" : req_info
    crud.create_fta_1day_inst1(db, fta_1day_inst)
    return fta_1day_inst

@router_inst1.get("/fta_inst1/1day/{id}")
def read_fta_1dayinst1(id: int, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_fta_1dayInst1(db, id)
    if insts == []:
        raise HTTPException(status_code=404, detail=f"ID ({id}) not found")
    return insts

@router_inst1.get("/fta_inst1/1hour")
def read_fta_1hourinst1(db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_fta_1hourInst1s(db)
    if insts is None:
        raise HTTPException(status_code=404, detail="User not found")
    return insts

@router_inst1.post("/fta_inst1/1hour", response_model=schemas.Fta_1hourInst1Create)
async def post_fta_1hourinst1(fta_1hour_inst: schemas.Fta_1hourInst1Create, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    # info: Request,
    #req_info = await info.json()
    # "data" : req_info
    crud.create_fta_1hour_inst1(db, fta_1hour_inst)
    return fta_1hour_inst

@router_inst1.get("/fta_inst1/1hour/{id}")
def read_fta_1hourinst1(id: int, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_fta_1hourInst1(db, id)
    if insts == []:
        raise HTTPException(status_code=404, detail=f"ID ({id}) not found")
    return insts