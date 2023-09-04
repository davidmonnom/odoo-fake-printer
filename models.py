from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class IotBox(Base):
    __tablename__ = "iot_box"

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer)
    create_uid = Column(Integer)
    write_uid = Column(Integer)
    name = Column(String)
    identifier = Column(String)
    ip = Column(String)
    version = Column(String)
    drivers_auto_update = Column(Boolean, default=True)
    create_date = Column(String)
    write_date = Column(String)


class IotDevice(Base):
    __tablename__ = "iot_device"

    id = Column(Integer, primary_key=True)
    iot_id = Column(Integer, ForeignKey("iot_box.id"))
    keyboard_layout = Column(Integer)
    create_uid = Column(Integer)
    write_uid = Column(Integer)
    name = Column(String)
    identifier = Column(String)
    type = Column(String)
    manufacturer = Column(String)
    connection = Column(String)
    display_url = Column(String)
    connected = Column(Boolean, default=False)
    create_date = Column(String)
    write_date = Column(String)
