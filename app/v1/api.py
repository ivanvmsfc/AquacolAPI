from fastapi import FastAPI, Request
from fastapi.security import HTTPBasic
from app.core.models import models
from app.core.models.database import engine
from app.tests.v1.prueba import router_prueba
from app.v1.endpoints.insts import router_insts
from app.v1.endpoints.token import router_token
from app.v1.endpoints.ft_ins_data import router_inst


models.Base.metadata.create_all(bind=engine)

# Esquema de seguridad HTTPBasic
security = HTTPBasic()

app = FastAPI()
app.include_router(router_insts)
app.include_router(router_token)
app.include_router(router_inst)
app.include_router(router_prueba)
