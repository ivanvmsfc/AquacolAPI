from sqlalchemy.orm import Session
from app.core.models import models
from app.core.schemas import schemas
import jwt

# Obtener los detalles de la instalacion, a partir de su ID
#   Inputs: inst_id --> ID de la instalacion
#   Outputs: Datos de las instalaciones
def get_inst(db: Session, inst_id: int):
    return db.query(models.Inst_Features).filter(models.Inst_Features.ins_fea_id == inst_id).first()

def get_insts(db: Session):
    return db.query(models.Inst_Features).all()

def create_inst(db: Session, inst: schemas.InstCreate):
    Inst_features = models.Inst_Features(**inst.dict())
    db.add(Inst_features)
    db.commit()

def update_inst(db: Session, inst_id: int, new_inst: schemas.InstCreate):
    insts = db.query(models.Inst_Features).filter(models.Inst_Features.ins_fea_id == inst_id).first()
    if insts:
        insts.update(ins_fea_id=inst_id, **new_inst.dict())
        db.commit()
    return insts


### FT INST1 ###
def get_ftInst1s(db: Session):
    return db.query(models.Ft_inst1_data).all()

def get_ftInst1(db: Session, id: int):
    return db.query(models.Ft_inst1_data).filter(models.Ft_inst1_data.ft_ins1_id == id).all()

def create_ft_inst1(db: Session, ft_inst1: schemas.FtInst1Create):
    FT_inst1_data = models.Ft_inst1_data(**ft_inst1.dict())
    db.add(FT_inst1_data)
    db.commit()

def update_ft_inst1(db: Session, id: int, new_ft_inst1: schemas.FtInst1Create):
    ft_inst1 = db.query(models.Ft_inst1_data).filter(models.Ft_inst1_data.ft_ins1_id == id).first()
    if ft_inst1:
        ft_inst1.update(ft_ins1_id=id, **new_ft_inst1.dict())
        db.commit()
    return ft_inst1


### FT INST2 ###
def get_ftInst2s(db: Session):
    return db.query(models.Ft_inst2_data).all()

def get_ftInst2(db: Session, id: int):
    return db.query(models.Ft_inst2_data).filter(models.Ft_inst2_data.ft_ins2_id == id).all()

def create_ft_inst2(db: Session, ft_inst2: schemas.FtInst2Create):
    FT_inst2_data = models.Ft_inst2_data(**ft_inst2.dict())
    db.add(FT_inst2_data)
    db.commit()

def update_ft_inst2(db: Session, id: int, new_ft_inst2: schemas.FtInst2Create):
    ft_inst2 = db.query(models.Ft_inst2_data).filter(models.Ft_inst2_data.ft_ins1_id == id).first()
    if ft_inst2:
        ft_inst2.update(ft_ins2_id=id, **new_ft_inst2.dict())
        db.commit()
    return ft_inst2


### FT INST3 ###
def get_ftInst3s(db: Session):
    return db.query(models.Ft_inst3_data).all()

def get_ftInst3(db: Session, id: int):
    return db.query(models.Ft_inst3_data).filter(models.Ft_inst3_data.ft_ins3_id == id).all()

def create_ft_inst3(db: Session, ft_inst3: schemas.FtInst3Create):
    FT_inst3_data = models.Ft_inst3_data(**ft_inst3.dict())
    db.add(FT_inst3_data)
    db.commit()

def update_ft_inst3(db: Session, id: int, new_ft_inst3: schemas.FtInst3Create):
    ft_inst3 = db.query(models.Ft_inst3_data).filter(models.Ft_inst3_data.ft_ins1_id == id).first()
    if ft_inst3:
        ft_inst3.update(ft_ins3_id=id, **new_ft_inst3.dict())
        db.commit()
    return ft_inst3


### FTA INST1 ###
def get_ftaInst1s(db: Session):
    fta1day = db.query(models.Fta_1day_inst1_data).all()
    fta1hour = db.query(models.Fta_1hour_inst1_data).all()
    return [fta1day, fta1hour]

def get_fta_1dayInst1s(db: Session):
    return db.query(models.Fta_1day_inst1_data).all()

def get_fta_1dayInst1(db: Session, id: int):
    return db.query(models.Fta_1day_inst1_data).filter(models.Fta_1day_inst1_data.fta1d_ins1_id == id).all()

def create_fta_1day_inst1(db: Session, fta_1day_inst1: schemas.Fta_1dayInst1Create):
    FT_inst1_data = models.Fta_1day_inst1_data(**fta_1day_inst1.dict())
    db.add(FT_inst1_data)
    db.commit()

def update_fta_1day_inst1(db: Session, id: int, new_fta_1day_inst1: schemas.Fta_1dayInst1Create):
    fta_1day_inst1 = db.query(models.Fta_1day_inst1_data).filter(
        models.Fta_1day_inst1_data.fta_1day_ins1_id == id).first()
    if fta_1day_inst1:
        fta_1day_inst1.update(fta1d_ins1_id=id, **new_fta_1day_inst1.dict())
        db.commit()
    return fta_1day_inst1

def get_fta_1hourInst1s(db: Session):
    return db.query(models.Fta_1hour_inst1_data).all()

def get_fta_1hourInst1(db: Session, id: int):
    return db.query(models.Fta_1hour_inst1_data).filter(models.Fta_1hour_inst1_data.fta1h_ins1_id == id).all()

def create_fta_1hour_inst1(db: Session, fta_1hour_inst1: schemas.Fta_1hourInst1Create):
    FT_inst1_data = models.Fta_1hour_inst1_data(**fta_1hour_inst1.dict())
    db.add(FT_inst1_data)
    db.commit()

def update_fta_1hour_inst1(db: Session, id: int, new_fta_1hour_inst1: schemas.Fta_1hourInst1Create):
    fta_1hour_inst1 = db.query(models.Fta_1hour_inst1_data).filter(
        models.Fta_1hour_inst1_data.fta_1hour_ins1_id == id).first()
    if fta_1hour_inst1:
        fta_1hour_inst1.update(fta1h_ins1_id=id, **new_fta_1hour_inst1.dict())
        db.commit()
    return fta_1hour_inst1


### FTA INST2 ###
def get_ftaInst2s(db: Session):
    fta1day = db.query(models.Fta_1day_inst2_data).all()
    fta1hour = db.query(models.Fta_1hour_inst2_data).all()
    return [fta1day, fta1hour]

def get_fta_1dayInst2s(db: Session):
    return db.query(models.Fta_1day_inst2_data).all()

def get_fta_1dayInst2(db: Session, id: int):
    return db.query(models.Fta_1day_inst2_data).filter(models.Fta_1day_inst2_data.fta1d_ins2_id == id).all()

def create_fta_1day_inst2(db: Session, fta_1day_inst2: schemas.Fta_1dayInst2Create):
    FT_inst2_data = models.Fta_1day_inst2_data(**fta_1day_inst2.dict())
    db.add(FT_inst2_data)
    db.commit()

def update_fta_1day_inst2(db: Session, id: int, new_fta_1day_inst2: schemas.Fta_1dayInst2Create):
    fta_1day_inst2 = db.query(models.Fta_1day_inst2_data).filter(
        models.Fta_1day_inst2_data.fta_1day_ins2_id == id).first()
    if fta_1day_inst2:
        fta_1day_inst2.update(fta1d_ins2_id=id, **new_fta_1day_inst2.dict())
        db.commit()
    return fta_1day_inst2

def get_fta_1hourInst2s(db: Session):
    return db.query(models.Fta_1hour_inst2_data).all()

def get_fta_1hourInst2(db: Session, id: int):
    return db.query(models.Fta_1hour_inst2_data).filter(models.Fta_1hour_inst2_data.fta1h_ins2_id == id).all()

def create_fta_1hour_inst2(db: Session, fta_1hour_inst2: schemas.Fta_1hourInst2Create):
    FT_inst2_data = models.Fta_1hour_inst2_data(**fta_1hour_inst2.dict())
    db.add(FT_inst2_data)
    db.commit()

def update_fta_1hour_inst2(db: Session, id: int, new_fta_1hour_inst2: schemas.Fta_1hourInst2Create):
    fta_1hour_inst2 = db.query(models.Fta_1hour_inst2_data).filter(
        models.Fta_1hour_inst2_data.fta_1hour_ins2_id == id).first()
    if fta_1hour_inst2:
        fta_1hour_inst2.update(fta1h_ins2_id=id, **new_fta_1hour_inst2.dict())
        db.commit()
    return fta_1hour_inst2


### FTA INST3 ###
def get_ftaInst3s(db: Session):
    fta1day = db.query(models.Fta_1day_inst3_data).all()
    fta1hour = db.query(models.Fta_1hour_inst3_data).all()
    return [fta1day, fta1hour]

def get_fta_1dayInst3s(db: Session):
    return db.query(models.Fta_1day_inst3_data).all()

def get_fta_1dayInst3(db: Session, id: int):
    return db.query(models.Fta_1day_inst3_data).filter(models.Fta_1day_inst3_data.fta1d_ins3_id == id).all()

def create_fta_1day_inst3(db: Session, fta_1day_inst3: schemas.Fta_1dayInst3Create):
    FT_inst3_data = models.Fta_1day_inst3_data(**fta_1day_inst3.dict())
    db.add(FT_inst3_data)
    db.commit()

def update_fta_1day_inst3(db: Session, id: int, new_fta_1day_inst3: schemas.Fta_1dayInst3Create):
    fta_1day_inst3 = db.query(models.Fta_1day_inst3_data).filter(
        models.Fta_1day_inst3_data.fta_1day_ins3_id == id).first()
    if fta_1day_inst3:
        fta_1day_inst3.update(fta1d_ins3_id=id, **new_fta_1day_inst3.dict())
        db.commit()
    return fta_1day_inst3

def get_fta_1hourInst3s(db: Session):
    return db.query(models.Fta_1hour_inst3_data).all()

def get_fta_1hourInst3(db: Session, id: int):
    return db.query(models.Fta_1hour_inst3_data).filter(models.Fta_1hour_inst3_data.fta1h_ins3_id == id).all()

def create_fta_1hour_inst3(db: Session, fta_1hour_inst3: schemas.Fta_1hourInst3Create):
    FT_inst3_data = models.Fta_1hour_inst3_data(**fta_1hour_inst3.dict())
    db.add(FT_inst3_data)
    db.commit()

def update_fta_1hour_inst3(db: Session, id: int, new_fta_1hour_inst3: schemas.Fta_1hourInst3Create):
    fta_1hour_inst3 = db.query(models.Fta_1hour_inst3_data).filter(
        models.Fta_1hour_inst3_data.fta_1hour_ins3_id == id).first()
    if fta_1hour_inst3:
        fta_1hour_inst3.update(fta1h_ins3_id=id, **new_fta_1hour_inst3.dict())
        db.commit()
    return fta_1hour_inst3


def generate_token(payload: dict, secret_key: str, algorithm: str) -> str:
    """
    Generate a JWT token from a payload dictionary, a secret key and an algorithm.
    """
    token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return token



