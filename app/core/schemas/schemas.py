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


class FtInst1Create(BaseModel):

    ft_ins1_inst: int
    ft_ins1_timestamp: int
    ft_ins1_t1: float
    ft_ins1_t2: float
    ft_ins1_ph: float
    ft_ins1_o2: float
    ft_ins1_ec: float
    ft_ins1_ta1: float
    ft_ins1_ha1: float
    ft_ins1_ta2: float
    ft_ins1_ha2: float

    class Config:
        orm_mode = True


class FtInst2Create(BaseModel):

    ft_ins2_inst: int
    ft_ins2_timestamp: int
    ft_ins2_t1: float
    ft_ins2_t2: float
    ft_ins2_ph: float
    ft_ins2_o2: float
    ft_ins2_ec: float
    ft_ins2_ta1: float
    ft_ins2_ha1: float
    ft_ins2_ta2: float
    ft_ins2_ha2: float

    class Config:
        orm_mode = True


class FtInst3Create(BaseModel):

    ft_ins3_inst: int
    ft_ins3_timestamp: int
    ft_ins3_t1: float
    ft_ins3_t2: float
    ft_ins3_ph: float
    ft_ins3_o2: float
    ft_ins3_ec: float
    ft_ins3_ta1: float
    ft_ins3_ha1: float
    ft_ins3_ta2: float
    ft_ins3_ha2: float

    class Config:
        orm_mode = True


class Fta_1dayInst1Create(BaseModel):

    fta1d_ins1_inst: int
    fta1d_ins1_timestamp: int
    fta1d_ins1_t1: float
    fta1d_ins1_t2: float
    fta1d_ins1_ph: float
    fta1d_ins1_o2: float
    fta1d_ins1_ec: float
    fta1d_ins1_ta1: float
    fta1d_ins1_ha1: float
    fta1d_ins1_ta2: float
    fta1d_ins1_ha2: float

    class Config:
        orm_mode = True


class Fta_1hourInst1Create(BaseModel):

    fta1h_ins1_inst: int
    fta1h_ins1_timestamp: int
    fta1h_ins1_t1: float
    fta1h_ins1_t2: float
    fta1h_ins1_ph: float
    fta1h_ins1_o2: float
    fta1h_ins1_ec: float
    fta1h_ins1_ta1: float
    fta1h_ins1_ha1: float
    fta1h_ins1_ta2: float
    fta1h_ins1_ha2: float

    class Config:
        orm_mode = True


class Fta_1dayInst2Create(BaseModel):

    fta1d_ins2_inst: int
    fta1d_ins2_timestamp: int
    fta1d_ins2_t1: float
    fta1d_ins2_t2: float
    fta1d_ins2_ph: float
    fta1d_ins2_o2: float
    fta1d_ins2_ec: float
    fta1d_ins2_ta1: float
    fta1d_ins2_ha1: float
    fta1d_ins2_ta2: float
    fta1d_ins2_ha2: float

    class Config:
        orm_mode = True


class Fta_1hourInst2Create(BaseModel):

    fta1h_ins2_inst: int
    fta1h_ins2_timestamp: int
    fta1h_ins2_t1: float
    fta1h_ins2_t2: float
    fta1h_ins2_ph: float
    fta1h_ins2_o2: float
    fta1h_ins2_ec: float
    fta1h_ins2_ta1: float
    fta1h_ins2_ha1: float
    fta1h_ins2_ta2: float
    fta1h_ins2_ha2: float

    class Config:
        orm_mode = True


class Fta_1dayInst3Create(BaseModel):

    fta1d_ins3_inst: int
    fta1d_ins3_timestamp: int
    fta1d_ins3_t1: float
    fta1d_ins3_t2: float
    fta1d_ins3_ph: float
    fta1d_ins3_o2: float
    fta1d_ins3_ec: float
    fta1d_ins3_ta1: float
    fta1d_ins3_ha1: float
    fta1d_ins3_ta2: float
    fta1d_ins3_ha2: float

    class Config:
        orm_mode = True


class Fta_1hourInst3Create(BaseModel):

    fta1h_ins3_inst: int
    fta1h_ins3_timestamp: int
    fta1h_ins3_t1: float
    fta1h_ins3_t2: float
    fta1h_ins3_ph: float
    fta1h_ins3_o2: float
    fta1h_ins3_ec: float
    fta1h_ins3_ta1: float
    fta1h_ins3_ha1: float
    fta1h_ins3_ta2: float
    fta1h_ins3_ha2: float

    class Config:
        orm_mode = True