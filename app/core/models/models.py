from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from app.core.models.database import Base

class Inst_Features(Base):
    __tablename__ = "inst_features"

    ins_fea_id = Column(Integer, primary_key=True)
    ins_fea_name = Column(String)
    ins_fea_desc = Column(String)
    ins_fea_lat = Column(Float)
    ins_fea_lon = Column(Float)
    ins_fea_own = Column(String)

    def update(self,ins_fea_id=None, ins_fea_name=None, ins_fea_desc=None, ins_fea_lat=None, ins_fea_lon=None,
               ins_fea_own=None):
        self.ins_fea_id = ins_fea_id
        self.ins_fea_name = ins_fea_name
        self.ins_fea_desc = ins_fea_desc
        self.ins_fea_lat = ins_fea_lat
        self.ins_fea_lon = ins_fea_lon
        self.ins_fea_own = ins_fea_own


class Ft_inst_data(Base):
    __tablename__ = "ft_ins_data"

    ft_ins_id = Column(Integer, primary_key=True)
    ft_ins_inst = Column(Integer, ForeignKey("inst_features.ins_fea_id"))
    ft_ins_timestamp = Column(Integer)
    ft_ins_t1 = Column(Float)
    ft_ins_t2 = Column(Float)
    ft_ins_ph = Column(Float)
    ft_ins_o2 = Column(Float)
    ft_ins_ec = Column(Float)
    ft_ins_ta1 = Column(Float)
    ft_ins_ha1 = Column(Float)
    ft_ins_ta2 = Column(Float)
    ft_ins_ha2 = Column(Float)
    ft_ins_ns = Column(Float)
    ft_ins_ni = Column(Float)

    def update(self,ft_ins_id=None, ft_ins_inst=None, ft_ins_timestamp=None, ft_ins_t1=None, ft_ins_t2=None,
               ft_ins_ph=None, ft_ins_o2=None, ft_ins_ec=None, ft_ins_ta1=None, ft_ins_ha1=None, ft_ins_ta2=None,
               ft_ins_ha2=None, ft_ins_ns=None, ft_ins_ni=None):
        self.ft_ins_id = ft_ins_id
        self.ft_ins_inst = ft_ins_inst
        self.ft_ins_timestamp = ft_ins_timestamp
        self.ft_ins_t1 = ft_ins_t1
        self.ft_ins_t2 = ft_ins_t2
        self.ft_ins_ph = ft_ins_ph
        self.ft_ins_o2 = ft_ins_o2
        self.ft_ins_ec = ft_ins_ec
        self.ft_ins_ta1 = ft_ins_ta1
        self.ft_ins_ha1 = ft_ins_ha1
        self.ft_ins_ta2 = ft_ins_ta2
        self.ft_ins_ha2 = ft_ins_ha2
        self.ft_ins_ns = ft_ins_ns
        self.ft_ins_ni = ft_ins_ni

class Fta_1day_inst_data(Base):
    __tablename__ = "fta_1day_ins_data"

    fta1d_ins_id = Column(Integer, primary_key=True)
    fta1d_ins_inst = Column(Integer, ForeignKey("inst_features.ins_fea_id"))
    fta1d_ins_timestamp = Column(Integer)
    fta1d_ins_t1 = Column(Float)
    fta1d_ins_t2 = Column(Float)
    fta1d_ins_ph = Column(Float)
    fta1d_ins_o2 = Column(Float)
    fta1d_ins_ec = Column(Float)
    fta1d_ins_ta1 = Column(Float)
    fta1d_ins_ha1 = Column(Float)
    fta1d_ins_ta2 = Column(Float)
    fta1d_ins_ha2 = Column(Float)
    fta1d_ins_ns = Column(Float)
    fta1d_ins_ni = Column(Float)

    def update(self,fta1d_ins_id=None, fta1d_ins_inst=None, fta1d_ins_timestamp=None, fta1d_ins_t1=None, fta1d_ins_t2=None,
               fta1d_ins_ph=None, fta1d_ins_o2=None, fta1d_ins_ec=None, fta1d_ins_ta1=None, fta1d_ins_ha1=None, fta1d_ins_ta2=None,
               fta1d_ins_ha2=None, fta1d_ins_ns=None, fta1d_ins_ni=None):
        self.fta1d_ins_id = fta1d_ins_id
        self.fta1d_ins_inst = fta1d_ins_inst
        self.fta1d_ins_timestamp = fta1d_ins_timestamp
        self.fta1d_ins_t1 = fta1d_ins_t1
        self.fta1d_ins_t2 = fta1d_ins_t2
        self.fta1d_ins_ph = fta1d_ins_ph
        self.fta1d_ins_o2 = fta1d_ins_o2
        self.fta1d_ins_ec = fta1d_ins_ec
        self.fta1d_ins_ta1 = fta1d_ins_ta1
        self.fta1d_ins_ha1 = fta1d_ins_ha1
        self.fta1d_ins_ta2 = fta1d_ins_ta2
        self.fta1d_ins_ha2 = fta1d_ins_ha2
        self.fta1d_ins_ns = fta1d_ins_ns
        self.fta1d_ins_ni = fta1d_ins_ni


class Fta_1hour_inst_data(Base):
    __tablename__ = "fta_1hour_ins_data"

    fta1h_ins_id = Column(Integer, primary_key=True)
    fta1h_ins_inst = Column(Integer, ForeignKey("inst_features.ins_fea_id"))
    fta1h_ins_timestamp = Column(Integer)
    fta1h_ins_t1 = Column(Float)
    fta1h_ins_t2 = Column(Float)
    fta1h_ins_ph = Column(Float)
    fta1h_ins_o2 = Column(Float)
    fta1h_ins_ec = Column(Float)
    fta1h_ins_ta1 = Column(Float)
    fta1h_ins_ha1 = Column(Float)
    fta1h_ins_ta2 = Column(Float)
    fta1h_ins_ha2 = Column(Float)
    fta1h_ins_ns = Column(Float)
    fta1h_ins_ni = Column(Float)

    def update(self,fta1h_ins_id=None, fta1h_ins_inst=None, fta1h_ins_timestamp=None, fta1h_ins_t1=None, fta1h_ins_t2=None,
               fta1h_ins_ph=None, fta1h_ins_o2=None, fta1h_ins_ec=None, fta1h_ins_ta1=None, fta1h_ins_ha1=None, fta1h_ins_ta2=None,
               fta1h_ins_ha2=None, fta1h_ins_ns=None, fta1h_ins_ni=None):
        self.fta1h_ins_id = fta1h_ins_id
        self.fta1h_ins_inst = fta1h_ins_inst
        self.fta1h_ins_timestamp = fta1h_ins_timestamp
        self.fta1h_ins_t1 = fta1h_ins_t1
        self.fta1h_ins_t2 = fta1h_ins_t2
        self.fta1h_ins_ph = fta1h_ins_ph
        self.fta1h_ins_o2 = fta1h_ins_o2
        self.fta1h_ins_ec = fta1h_ins_ec
        self.fta1h_ins_ta1 = fta1h_ins_ta1
        self.fta1h_ins_ha1 = fta1h_ins_ha1
        self.fta1h_ins_ta2 = fta1h_ins_ta2
        self.fta1h_ins_ha2 = fta1h_ins_ha2
        self.fta1h_ins_ns = fta1h_ins_ns
        self.fta1h_ins_ni = fta1h_ins_ni
