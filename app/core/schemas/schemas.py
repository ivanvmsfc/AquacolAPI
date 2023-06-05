from pydantic import BaseModel

# Clase que modela la formato de salida
# El resultado del endpoint que implementa este metodo sólo devuelve 2 campos
# de las instalaciones (name y description)
class InstBase(BaseModel):
    ins_fea_name: str
    ins_fea_desc: str

    class Config:
        orm_mode = True

class InstCreate(BaseModel):

    ins_fea_name: str
    ins_fea_desc: str
    ins_fea_lat: float
    ins_fea_lon: float
    ins_fea_own: str

    class Config:
        orm_mode = True


class FtInstCreate(BaseModel):

    ft_ins_inst: int
    ft_ins_timestamp: int
    ft_ins_t1: float
    ft_ins_t2: float
    ft_ins_ph: float
    ft_ins_o2: float
    ft_ins_ec: float
    ft_ins_ta1: float
    ft_ins_ha1: float
    ft_ins_ta2: float
    ft_ins_ha2: float
    ft_ins_ns: float
    ft_ins_ni: float

    class Config:
        orm_mode = True


class Fta_1dayInstCreate(BaseModel):

    fta1d_ins_inst: int
    fta1d_ins_timestamp: int
    fta1d_ins_t1: float
    fta1d_ins_t2: float
    fta1d_ins_ph: float
    fta1d_ins_o2: float
    fta1d_ins_ec: float
    fta1d_ins_ta1: float
    fta1d_ins_ha1: float
    fta1d_ins_ta2: float
    fta1d_ins_ha2: float
    fta1d_ins_ns: float
    fta1d_ins_ni: float

    class Config:
        orm_mode = True


class Fta_1hourInstCreate(BaseModel):

    fta1h_ins_inst: int
    fta1h_ins_timestamp: int
    fta1h_ins_t1: float
    fta1h_ins_t2: float
    fta1h_ins_ph: float
    fta1h_ins_o2: float
    fta1h_ins_ec: float
    fta1h_ins_ta1: float
    fta1h_ins_ha1: float
    fta1h_ins_ta2: float
    fta1h_ins_ha2: float
    fta1h_ins_ns: float
    fta1h_ins_ni: float

    class Config:
        orm_mode = True

