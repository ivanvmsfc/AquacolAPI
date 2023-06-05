from fastapi import HTTPException
from sqlalchemy import inspect
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
def get_data(db: Session, table, **kwargs):
    if all(value is None for value in kwargs.values()):
        return db.query(table).all()
    else:
        filtered_kwargs = {key: value for key, value in kwargs.items() if value is not None}
        searched_data = db.query(table).filter_by(**filtered_kwargs).all()
        if searched_data:
            return searched_data
        else:
            raise HTTPException(status_code=404, detail='ID not found')

def create_data(db: Session, schema, table):
    data_to_insert = schema.dict()
    mapper = inspect(table)
    primary_key_column = mapper.primary_key[0].name
    inserted_data = table(**data_to_insert)
    db.add(inserted_data)
    db.commit()
    inserted_id = getattr(inserted_data, primary_key_column)
    data = {**data_to_insert, primary_key_column: inserted_id}
    return data

def update_data(db: Session, schema, table, bulk, **kwargs):
    data_to_update = db.query(table).filter(kwargs['column_id'] == kwargs['id']).first()
    if bulk:
        if data_to_update:
            first_column_name = table.__table__.columns.keys()[0]
            # first_column_value = getattr(data_to_update, first_column_name)
            data_to_update.update(**schema.dict())
            db.commit()
            data = {**schema.dict()}
            return True, data

        else:
            return False, 0
    else:
        if data_to_update:
            first_column_name = table.__table__.columns.keys()[0]
            # first_column_value = getattr(data_to_update, first_column_name)
            data_to_update.update(**{first_column_name: kwargs['id']}, **schema.dict())
            db.commit()
            data = {first_column_name: kwargs['id'], **schema.dict()}
            return data
        else:
            raise HTTPException(status_code=404, detail='ID not found')
