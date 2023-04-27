from app.core.models import crud
from app.core.schemas import schemas
from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.dependencies import *

router_insts = APIRouter(
    prefix='',
    tags=['addition']
)

### DATOS DE LAS INTALACIONES ###
@router_insts.get("/insts/{inst_id}", response_model=schemas.InstCreate)
def read_inst(inst_id: int, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_inst(db, inst_id=inst_id)
    if insts is None:
        raise HTTPException(status_code=404, detail="Instalation not found")
    return insts

@router_insts.get("/insts")
def read_inst(db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    insts = crud.get_insts(db)
    if insts is None:
        raise HTTPException(status_code=404, detail="User not found")
    return insts

@router_insts.post("/insts", response_model=schemas.InstCreate)
async def post_inst(inst: schemas.InstCreate, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    # info: Request,
    #req_info = await info.json()
    # "data" : req_info
    crud.create_inst(db, inst)
    return inst

@router_insts.put("/insts/{inst_id}", response_model=schemas.InstCreate)
def put_inst(inst_id: int, inst: schemas.InstCreate, db: Session = Depends(get_db), username: str = Depends(get_current_user)):

    out = crud.update_inst(db, inst_id, inst)

    return out
