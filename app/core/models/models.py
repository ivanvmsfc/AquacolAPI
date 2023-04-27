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


class Ft_inst1_data(Base):
    __tablename__ = "ft_inst1_data"

    ft_ins1_id = Column(Integer, primary_key=True)
    ft_ins1_inst = Column(Integer, ForeignKey("inst_features.ins_fea_id"))
    ft_ins1_timestamp = Column(Integer)
    ft_ins1_t1 = Column(Float)
    ft_ins1_t2 = Column(Float)
    ft_ins1_ph = Column(Float)
    ft_ins1_o2 = Column(Float)
    ft_ins1_ec = Column(Float)
    ft_ins1_ta1 = Column(Float)
    ft_ins1_ha1 = Column(Float)
    ft_ins1_ta2 = Column(Float)
    ft_ins1_ha2 = Column(Float)

    def update(self,ft_ins1_id=None, ft_ins1_inst=None, ft_ins1_timestamp=None, ft_ins1_t1=None, ft_ins1_t2=None,
               ft_ins1_ph=None, ft_ins1_o2=None, ft_ins1_ec=None, ft_ins1_ta1=None, ft_ins1_ha1=None, ft_ins1_ta2=None,
               ft_ins1_ha2=None):
        self.ft_ins1_id = ft_ins1_id
        self.ft_ins1_inst = ft_ins1_inst
        self.ft_ins1_timestamp = ft_ins1_timestamp
        self.ft_ins1_t1 = ft_ins1_t1
        self.ft_ins1_t2 = ft_ins1_t2
        self.ft_ins1_ph = ft_ins1_ph
        self.ft_ins1_o2 = ft_ins1_o2
        self.ft_ins1_ec = ft_ins1_ec
        self.ft_ins1_ta1 = ft_ins1_ta1
        self.ft_ins1_ha1 = ft_ins1_ha1
        self.ft_ins1_ta2 = ft_ins1_ta2
        self.ft_ins1_ha2 = ft_ins1_ha2


class Ft_inst2_data(Base):
    __tablename__ = "ft_inst2_data"

    ft_ins2_id = Column(Integer, primary_key=True)
    ft_ins2_inst = Column(Integer, ForeignKey("inst_features.ins_fea_id"))
    ft_ins2_timestamp = Column(Integer)
    ft_ins2_t1 = Column(Float)
    ft_ins2_t2 = Column(Float)
    ft_ins2_ph = Column(Float)
    ft_ins2_o2 = Column(Float)
    ft_ins2_ec = Column(Float)
    ft_ins2_ta1 = Column(Float)
    ft_ins2_ha1 = Column(Float)
    ft_ins2_ta2 = Column(Float)
    ft_ins2_ha2 = Column(Float)

    def update(self,ft_ins2_id=None, ft_ins2_inst=None, ft_ins2_timestamp=None, ft_ins2_t1=None, ft_ins2_t2=None,
               ft_ins2_ph=None, ft_ins2_o2=None, ft_ins2_ec=None, ft_ins2_ta1=None, ft_ins2_ha1=None, ft_ins2_ta2=None,
               ft_ins2_ha2=None):
        self.ft_ins2_id = ft_ins2_id
        self.ft_ins2_inst = ft_ins2_inst
        self.ft_ins2_timestamp = ft_ins2_timestamp
        self.ft_ins2_t1 = ft_ins2_t1
        self.ft_ins2_t2 = ft_ins2_t2
        self.ft_ins2_ph = ft_ins2_ph
        self.ft_ins2_o2 = ft_ins2_o2
        self.ft_ins2_ec = ft_ins2_ec
        self.ft_ins2_ta1 = ft_ins2_ta1
        self.ft_ins2_ha1 = ft_ins2_ha1
        self.ft_ins2_ta2 = ft_ins2_ta2
        self.ft_ins2_ha2 = ft_ins2_ha2


class Ft_inst3_data(Base):
    __tablename__ = "ft_inst3_data"

    ft_ins3_id = Column(Integer, primary_key=True)
    ft_ins3_inst = Column(Integer, ForeignKey("inst_features.ins_fea_id"))
    ft_ins3_timestamp = Column(Integer)
    ft_ins3_t1 = Column(Float)
    ft_ins3_t2 = Column(Float)
    ft_ins3_ph = Column(Float)
    ft_ins3_o2 = Column(Float)
    ft_ins3_ec = Column(Float)
    ft_ins3_ta1 = Column(Float)
    ft_ins3_ha1 = Column(Float)
    ft_ins3_ta2 = Column(Float)
    ft_ins3_ha2 = Column(Float)

    def update(self,ft_ins3_id=None, ft_ins3_inst=None, ft_ins3_timestamp=None, ft_ins3_t1=None, ft_ins3_t2=None,
               ft_ins3_ph=None, ft_ins3_o2=None, ft_ins3_ec=None, ft_ins3_ta1=None, ft_ins3_ha1=None, ft_ins3_ta2=None,
               ft_ins3_ha2=None):
        self.ft_ins3_id = ft_ins3_id
        self.ft_ins3_inst = ft_ins3_inst
        self.ft_ins3_timestamp = ft_ins3_timestamp
        self.ft_ins3_t1 = ft_ins3_t1
        self.ft_ins3_t2 = ft_ins3_t2
        self.ft_ins3_ph = ft_ins3_ph
        self.ft_ins3_o2 = ft_ins3_o2
        self.ft_ins3_ec = ft_ins3_ec
        self.ft_ins3_ta1 = ft_ins3_ta1
        self.ft_ins3_ha1 = ft_ins3_ha1
        self.ft_ins3_ta2 = ft_ins3_ta2
        self.ft_ins3_ha2 = ft_ins3_ha2


class Fta_1day_inst1_data(Base):
    __tablename__ = "fta_1day_inst1_data"

    fta1d_ins1_id = Column(Integer, primary_key=True)
    fta1d_ins1_inst = Column(Integer, ForeignKey("inst_features.ins_fea_id"))
    fta1d_ins1_timestamp = Column(Integer)
    fta1d_ins1_t1 = Column(Float)
    fta1d_ins1_t2 = Column(Float)
    fta1d_ins1_ph = Column(Float)
    fta1d_ins1_o2 = Column(Float)
    fta1d_ins1_ec = Column(Float)
    fta1d_ins1_ta1 = Column(Float)
    fta1d_ins1_ha1 = Column(Float)
    fta1d_ins1_ta2 = Column(Float)
    fta1d_ins1_ha2 = Column(Float)

    def update(self,fta1d_ins1_id=None, fta1d_ins1_inst=None, fta1d_ins1_timestamp=None, fta1d_ins1_t1=None, fta1d_ins1_t2=None,
               fta1d_ins1_ph=None, fta1d_ins1_o2=None, fta1d_ins1_ec=None, fta1d_ins1_ta1=None, fta1d_ins1_ha1=None, fta1d_ins1_ta2=None,
               fta1d_ins1_ha2=None):
        self.fta1d_ins1_id = fta1d_ins1_id
        self.fta1d_ins1_inst = fta1d_ins1_inst
        self.fta1d_ins1_timestamp = fta1d_ins1_timestamp
        self.fta1d_ins1_t1 = fta1d_ins1_t1
        self.fta1d_ins1_t2 = fta1d_ins1_t2
        self.fta1d_ins1_ph = fta1d_ins1_ph
        self.fta1d_ins1_o2 = fta1d_ins1_o2
        self.fta1d_ins1_ec = fta1d_ins1_ec
        self.fta1d_ins1_ta1 = fta1d_ins1_ta1
        self.fta1d_ins1_ha1 = fta1d_ins1_ha1
        self.fta1d_ins1_ta2 = fta1d_ins1_ta2
        self.fta1d_ins1_ha2 = fta1d_ins1_ha2


class Fta_1hour_inst1_data(Base):
    __tablename__ = "fta_1hour_inst1_data"

    fta1h_ins1_id = Column(Integer, primary_key=True)
    fta1h_ins1_inst = Column(Integer, ForeignKey("inst_features.ins_fea_id"))
    fta1h_ins1_timestamp = Column(Integer)
    fta1h_ins1_t1 = Column(Float)
    fta1h_ins1_t2 = Column(Float)
    fta1h_ins1_ph = Column(Float)
    fta1h_ins1_o2 = Column(Float)
    fta1h_ins1_ec = Column(Float)
    fta1h_ins1_ta1 = Column(Float)
    fta1h_ins1_ha1 = Column(Float)
    fta1h_ins1_ta2 = Column(Float)
    fta1h_ins1_ha2 = Column(Float)

    def update(self,fta1h_ins1_id=None, fta1h_ins1_inst=None, fta1h_ins1_timestamp=None, fta1h_ins1_t1=None, fta1h_ins1_t2=None,
               fta1h_ins1_ph=None, fta1h_ins1_o2=None, fta1h_ins1_ec=None, fta1h_ins1_ta1=None, fta1h_ins1_ha1=None, fta1h_ins1_ta2=None,
               fta1h_ins1_ha2=None):
        self.fta1h_ins1_id = fta1h_ins1_id
        self.fta1h_ins1_inst = fta1h_ins1_inst
        self.fta1h_ins1_timestamp = fta1h_ins1_timestamp
        self.fta1h_ins1_t1 = fta1h_ins1_t1
        self.fta1h_ins1_t2 = fta1h_ins1_t2
        self.fta1h_ins1_ph = fta1h_ins1_ph
        self.fta1h_ins1_o2 = fta1h_ins1_o2
        self.fta1h_ins1_ec = fta1h_ins1_ec
        self.fta1h_ins1_ta1 = fta1h_ins1_ta1
        self.fta1h_ins1_ha1 = fta1h_ins1_ha1
        self.fta1h_ins1_ta2 = fta1h_ins1_ta2
        self.fta1h_ins1_ha2 = fta1h_ins1_ha2


class Fta_1day_inst2_data(Base):
    __tablename__ = "fta_1day_inst2_data"

    fta1d_ins2_id = Column(Integer, primary_key=True)
    fta1d_ins2_inst = Column(Integer, ForeignKey("inst_features.ins_fea_id"))
    fta1d_ins2_timestamp = Column(Integer)
    fta1d_ins2_t1 = Column(Float)
    fta1d_ins2_t2 = Column(Float)
    fta1d_ins2_ph = Column(Float)
    fta1d_ins2_o2 = Column(Float)
    fta1d_ins2_ec = Column(Float)
    fta1d_ins2_ta1 = Column(Float)
    fta1d_ins2_ha1 = Column(Float)
    fta1d_ins2_ta2 = Column(Float)
    fta1d_ins2_ha2 = Column(Float)

    def update(self,fta1d_ins2_id=None, fta1d_ins2_inst=None, fta1d_ins2_timestamp=None, fta1d_ins2_t1=None, fta1d_ins2_t2=None,
               fta1d_ins2_ph=None, fta1d_ins2_o2=None, fta1d_ins2_ec=None, fta1d_ins2_ta1=None, fta1d_ins2_ha1=None, fta1d_ins2_ta2=None,
               fta1d_ins2_ha2=None):
        self.fta1d_ins2_id = fta1d_ins2_id
        self.fta1d_ins2_inst = fta1d_ins2_inst
        self.fta1d_ins2_timestamp = fta1d_ins2_timestamp
        self.fta1d_ins2_t1 = fta1d_ins2_t1
        self.fta1d_ins2_t2 = fta1d_ins2_t2
        self.fta1d_ins2_ph = fta1d_ins2_ph
        self.fta1d_ins2_o2 = fta1d_ins2_o2
        self.fta1d_ins2_ec = fta1d_ins2_ec
        self.fta1d_ins2_ta1 = fta1d_ins2_ta1
        self.fta1d_ins2_ha1 = fta1d_ins2_ha1
        self.fta1d_ins2_ta2 = fta1d_ins2_ta2
        self.fta1d_ins2_ha2 = fta1d_ins2_ha2


class Fta_1hour_inst2_data(Base):
    __tablename__ = "fta_1hour_inst2_data"

    fta1h_ins2_id = Column(Integer, primary_key=True)
    fta1h_ins2_inst = Column(Integer, ForeignKey("inst_features.ins_fea_id"))
    fta1h_ins2_timestamp = Column(Integer)
    fta1h_ins2_t1 = Column(Float)
    fta1h_ins2_t2 = Column(Float)
    fta1h_ins2_ph = Column(Float)
    fta1h_ins2_o2 = Column(Float)
    fta1h_ins2_ec = Column(Float)
    fta1h_ins2_ta1 = Column(Float)
    fta1h_ins2_ha1 = Column(Float)
    fta1h_ins2_ta2 = Column(Float)
    fta1h_ins2_ha2 = Column(Float)

    def update(self,fta1h_ins2_id=None, fta1h_ins2_inst=None, fta1h_ins2_timestamp=None, fta1h_ins2_t1=None, fta1h_ins2_t2=None,
               fta1h_ins2_ph=None, fta1h_ins2_o2=None, fta1h_ins2_ec=None, fta1h_ins2_ta1=None, fta1h_ins2_ha1=None, fta1h_ins2_ta2=None,
               fta1h_ins2_ha2=None):
        self.fta1h_ins2_id = fta1h_ins2_id
        self.fta1h_ins2_inst = fta1h_ins2_inst
        self.fta1h_ins2_timestamp = fta1h_ins2_timestamp
        self.fta1h_ins2_t1 = fta1h_ins2_t1
        self.fta1h_ins2_t2 = fta1h_ins2_t2
        self.fta1h_ins2_ph = fta1h_ins2_ph
        self.fta1h_ins2_o2 = fta1h_ins2_o2
        self.fta1h_ins2_ec = fta1h_ins2_ec
        self.fta1h_ins2_ta1 = fta1h_ins2_ta1
        self.fta1h_ins2_ha1 = fta1h_ins2_ha1
        self.fta1h_ins2_ta2 = fta1h_ins2_ta2
        self.fta1h_ins2_ha2 = fta1h_ins2_ha2


class Fta_1day_inst3_data(Base):
    __tablename__ = "fta_1day_inst3_data"

    fta1d_ins3_id = Column(Integer, primary_key=True)
    fta1d_ins3_inst = Column(Integer, ForeignKey("inst_features.ins_fea_id"))
    fta1d_ins3_timestamp = Column(Integer)
    fta1d_ins3_t1 = Column(Float)
    fta1d_ins3_t2 = Column(Float)
    fta1d_ins3_ph = Column(Float)
    fta1d_ins3_o2 = Column(Float)
    fta1d_ins3_ec = Column(Float)
    fta1d_ins3_ta1 = Column(Float)
    fta1d_ins3_ha1 = Column(Float)
    fta1d_ins3_ta2 = Column(Float)
    fta1d_ins3_ha2 = Column(Float)

    def update(self,fta1d_ins3_id=None, fta1d_ins3_inst=None, fta1d_ins3_timestamp=None, fta1d_ins3_t1=None, fta1d_ins3_t2=None,
               fta1d_ins3_ph=None, fta1d_ins3_o2=None, fta1d_ins3_ec=None, fta1d_ins3_ta1=None, fta1d_ins3_ha1=None, fta1d_ins3_ta2=None,
               fta1d_ins3_ha2=None):
        self.fta1d_ins3_id = fta1d_ins3_id
        self.fta1d_ins3_inst = fta1d_ins3_inst
        self.fta1d_ins3_timestamp = fta1d_ins3_timestamp
        self.fta1d_ins3_t1 = fta1d_ins3_t1
        self.fta1d_ins3_t2 = fta1d_ins3_t2
        self.fta1d_ins3_ph = fta1d_ins3_ph
        self.fta1d_ins3_o2 = fta1d_ins3_o2
        self.fta1d_ins3_ec = fta1d_ins3_ec
        self.fta1d_ins3_ta1 = fta1d_ins3_ta1
        self.fta1d_ins3_ha1 = fta1d_ins3_ha1
        self.fta1d_ins3_ta2 = fta1d_ins3_ta2
        self.fta1d_ins3_ha2 = fta1d_ins3_ha2


class Fta_1hour_inst3_data(Base):
    __tablename__ = "fta_1hour_inst3_data"

    fta1h_ins3_id = Column(Integer, primary_key=True)
    fta1h_ins3_inst = Column(Integer, ForeignKey("inst_features.ins_fea_id"))
    fta1h_ins3_timestamp = Column(Integer)
    fta1h_ins3_t1 = Column(Float)
    fta1h_ins3_t2 = Column(Float)
    fta1h_ins3_ph = Column(Float)
    fta1h_ins3_o2 = Column(Float)
    fta1h_ins3_ec = Column(Float)
    fta1h_ins3_ta1 = Column(Float)
    fta1h_ins3_ha1 = Column(Float)
    fta1h_ins3_ta2 = Column(Float)
    fta1h_ins3_ha2 = Column(Float)

    def update(self,fta1h_ins3_id=None, fta1h_ins3_inst=None, fta1h_ins3_timestamp=None, fta1h_ins3_t1=None, fta1h_ins3_t2=None,
               fta1h_ins3_ph=None, fta1h_ins3_o2=None, fta1h_ins3_ec=None, fta1h_ins3_ta1=None, fta1h_ins3_ha1=None, fta1h_ins3_ta2=None,
               fta1h_ins3_ha2=None):
        self.fta1h_ins3_id = fta1h_ins3_id
        self.fta1h_ins3_inst = fta1h_ins3_inst
        self.fta1h_ins3_timestamp = fta1h_ins3_timestamp
        self.fta1h_ins3_t1 = fta1h_ins3_t1
        self.fta1h_ins3_t2 = fta1h_ins3_t2
        self.fta1h_ins3_ph = fta1h_ins3_ph
        self.fta1h_ins3_o2 = fta1h_ins3_o2
        self.fta1h_ins3_ec = fta1h_ins3_ec
        self.fta1h_ins3_ta1 = fta1h_ins3_ta1
        self.fta1h_ins3_ha1 = fta1h_ins3_ha1
        self.fta1h_ins3_ta2 = fta1h_ins3_ta2
        self.fta1h_ins3_ha2 = fta1h_ins3_ha2