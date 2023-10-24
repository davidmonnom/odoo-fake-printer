# Odoo Fake Printer
Here's a little script that will allow you to simulate an IOT and an Epson printer in Odoo.

This script allows you to create an image based on a ticket printed from the `point_of_sale` or `pos_self_order` module.

For the moment it doesn't contain all the functions of an IOT but only those I needed for my tests. Don't hesitate to open a PR if you want to add something.

### Installation
1. Create a new Python environnement:
`python3 -m venv env`

2. Activate the environnement:
`source env/bin/activate`

3. Install all requirements:
`pip install -r requirements.txt`

4. Don't forget to create the `.env` file at the root of the project. It must contain at least these 2 fields:

```
DATABASE_URL=postgresql://user:password@localhost:5432/database
SAVEPATH=/home/{USER}/images/
```

5. Create an Odoo database with `pos_iot` installed. 

### Utilisation
Firstly you need to use socat or equivalent to forward the port 8070 to 80
- `sudo socat TCP-LISTEN:80,fork TCP:localhost:8070`

Launch the server:
- `python main.py`

Create a fake IOT on the server by calling http://127.0.0.1/create_iot_device

In Odoo you can use a so-called "direct" ePoS Printer. To use this feature you can simply enter 127.0.0.1 which will point to your service.
