from app.core.models import crud
from app.core.schemas import schemas
from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.dependencies import *

router_inst3 = APIRouter(
    prefix='',
    tags=['addition']
)

### DATOS DE LAS MEDICIONES DE LOS SENSORES (PARA LA INST3) ###
@router_inst3.get("/ft_inst3")
def read_ftinst3(db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_ftInst3s(db)
    if insts is None:
        raise HTTPException(status_code=404, detail="User not found")
    return insts

@router_inst3.post("/ft_inst3", response_model=schemas.FtInst3Create)
async def post_ftinst3(ft_inst: schemas.FtInst3Create, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    # info: Request,
    #req_info = await info.json()
    # "data" : req_info
    crud.create_ft_inst3(db, ft_inst)
    return ft_inst

@router_inst3.get("/ft_inst3/{id}")
def read_ftinst3(id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme), username: str = Depends(get_current_user)):
    insts = crud.get_ftInst3(db, id)
    if insts == []:
        raise HTTPException(status_code=404, detail=f"ID ({id}) not found")
    return insts


### DATOS AGREGADOS DE LAS MEDICIONES DE LOS SENSORES (PARA LA INST3) ###
@router_inst3.get("/fta_inst3")
def read_ftainst3(db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_ftaInst3s(db)
    if insts is None:
        raise HTTPException(status_code=404, detail="User not found")
    return insts

@router_inst3.get("/fta_inst3/1day")
def read_fta_1dayinst3(db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_fta_1dayInst3s(db)
    if insts is None:
        raise HTTPException(status_code=404, detail="User not found")
    return insts

@router_inst3.post("/fta_inst3/1day", response_model=schemas.Fta_1dayInst3Create)
async def post_fta_1dayinst3(fta_1day_inst: schemas.Fta_1dayInst3Create, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    # info: Request,
    #req_info = await info.json()
    # "data" : req_info
    crud.create_fta_1day_inst3(db, fta_1day_inst)
    return fta_1day_inst

@router_inst3.get("/fta_inst3/1day/{id}")
def read_fta_1dayinst3(id: int, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_fta_1dayInst3(db, id)
    if insts == []:
        raise HTTPException(status_code=404, detail=f"ID ({id}) not found")
    return insts

@router_inst3.get("/fta_inst3/1hour")
def read_fta_1hourinst3(db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_fta_1hourInst3s(db)
    if insts is None:
        raise HTTPException(status_code=404, detail="User not found")
    return insts

@router_inst3.post("/fta_inst3/1hour", response_model=schemas.Fta_1hourInst3Create)
async def post_fta_1hourinst3(fta_1hour_inst: schemas.Fta_1hourInst3Create, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    # info: Request,
    #req_info = await info.json()
    # "data" : req_info
    crud.create_fta_1hour_inst3(db, fta_1hour_inst)
    return fta_1hour_inst

@router_inst3.get("/fta_inst3/1hour/{id}")
def read_fta_1hourinst3(id: int, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_fta_1hourInst3(db, id)
    if insts == []:
        raise HTTPException(status_code=404, detail=f"ID ({id}) not found")
    return insts