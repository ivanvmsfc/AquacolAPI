from app.core.models import crud
from app.core.schemas import schemas
from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.dependencies import *

router_inst2 = APIRouter(
    prefix='',
    tags=['addition']
)

### DATOS DE LAS MEDICIONES DE LOS SENSORES (PARA LA INST2) ###
@router_inst2.get("/ft_inst2")
def read_ftinst2(db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_ftInst2s(db)
    if insts is None:
        raise HTTPException(status_code=404, detail="User not found")
    return insts

@router_inst2.post("/ft_inst2", response_model=schemas.FtInst2Create)
async def post_ftinst2(ft_inst: schemas.FtInst2Create, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    # info: Request,
    #req_info = await info.json()
    # "data" : req_info
    crud.create_ft_inst2(db, ft_inst)
    return ft_inst

@router_inst2.get("/ft_inst2/{id}")
def read_ftinst2(id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme), username: str = Depends(get_current_user)):
    insts = crud.get_ftInst2(db, id)
    if insts == []:
        raise HTTPException(status_code=404, detail=f"ID ({id}) not found")
    return insts


### DATOS AGREGADOS DE LAS MEDICIONES DE LOS SENSORES (PARA LA INST2) ###
@router_inst2.get("/fta_inst2")
def read_ftainst2(db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_ftaInst2s(db)
    if insts is None:
        raise HTTPException(status_code=404, detail="User not found")
    return insts

@router_inst2.get("/fta_inst2/1day")
def read_fta_1dayinst2(db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_fta_1dayInst2s(db)
    if insts is None:
        raise HTTPException(status_code=404, detail="User not found")
    return insts

@router_inst2.post("/fta_inst2/1day", response_model=schemas.Fta_1dayInst2Create)
async def post_fta_1dayinst2(fta_1day_inst: schemas.Fta_1dayInst2Create, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    # info: Request,
    #req_info = await info.json()
    # "data" : req_info
    crud.create_fta_1day_inst2(db, fta_1day_inst)
    return fta_1day_inst

@router_inst2.get("/fta_inst2/1day/{id}")
def read_fta_1dayinst2(id: int, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_fta_1dayInst2(db, id)
    if insts == []:
        raise HTTPException(status_code=404, detail=f"ID ({id}) not found")
    return insts

@router_inst2.get("/fta_inst2/1hour")
def read_fta_1hourinst2(db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_fta_1hourInst2s(db)
    if insts is None:
        raise HTTPException(status_code=404, detail="User not found")
    return insts

@router_inst2.post("/fta_inst2/1hour", response_model=schemas.Fta_1hourInst2Create)
async def post_fta_1hourinst2(fta_1hour_inst: schemas.Fta_1hourInst2Create, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    # info: Request,
    #req_info = await info.json()
    # "data" : req_info
    crud.create_fta_1hour_inst2(db, fta_1hour_inst)
    return fta_1hour_inst

@router_inst2.get("/fta_inst2/1hour/{id}")
def read_fta_1hourinst2(id: int, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_fta_1hourInst2(db, id)
    if insts == []:
        raise HTTPException(status_code=404, detail=f"ID ({id}) not found")
    return insts