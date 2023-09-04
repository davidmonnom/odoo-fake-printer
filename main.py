import uvicorn
import json
import base64
import xml.etree.ElementTree as ET

from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import SessionLocal
from models import IotBox, IotDevice
from convert import decode_base64_data, _SAVEPATH_BASE64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/cgi-bin/epos/service.cgi")
async def service(request: Request, db: Session = Depends(get_db)):
    body = await request.body()
    xml_tree = ET.fromstring(body)
    base64 = xml_tree[0][0][0].text
    width = int(xml_tree[0][0][0].attrib['width'])
    height = int(xml_tree[0][0][0].attrib['height'])
    decode_base64_data(base64, width, height)
    return "<printer><response success='true'>true</response></printer>"


@app.post("/hw_drivers/action")
async def action(request: Request, db: Session = Depends(get_db)):
    raw_body = await request.body()
    body = json.loads(raw_body)
    print_data = json.loads(body['params']['data'])

    if print_data.get('receipt'):
        image_receipt = print_data['receipt']

        with open(_SAVEPATH_BASE64, "wb") as fh:
            fh.write(base64.b64decode(image_receipt))

    return {"status": 'ok', "value": 5.02}


@app.get("/hw_proxy/hello")
def hello(db: Session = Depends(get_db)):
    return "ping"


@app.post("/hw_drivers/event")
def event(db: Session = Depends(get_db)):
    return {"status": True}


@app.get("/create_iot_device")
def create_iot_device(db: Session = Depends(get_db)):
    iot_box = db.query(IotBox).filter(
        IotBox.identifier == 'fake_iot_box').first()

    if not iot_box:
        iot_box = IotBox(
            name='fake_iot_box',
            identifier='fake_iot_box',
            ip='127.0.0.1',
            version='21.10',
            drivers_auto_update=True)
        db.add(iot_box)
        db.commit()

        iot_printer = IotDevice(
            iot_id=iot_box.id,
            name='Fake printer',
            identifier='fake_iot_printer',
            type='printer',
            manufacturer='fake_iot_printer',
            connection='network',
            display_url='fake_iot_printer',
            connected=True)
        db.add(iot_printer)
        db.commit()

        iot_scale = IotDevice(
            iot_id=iot_box.id,
            name='Fake scale',
            identifier='fake_iot_scale',
            type='scale',
            manufacturer='fake_iot_scale',
            connection='network',
            display_url='fake_iot_scale',
            connected=True)
        db.add(iot_scale)
        db.commit()

    return {"status": True}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8069)
