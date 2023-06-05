from fastapi import FastAPI, Request
from fastapi.security import HTTPBasic
from fastapi.openapi.utils import get_openapi
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

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Aquacol Data",
        version="1.0.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.include_router(router_insts)
app.include_router(router_token)
app.include_router(router_inst)
app.include_router(router_prueba)
