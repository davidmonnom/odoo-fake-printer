1. Create new env
    python3 -m venv env

2. Activate env
    source env/bin/activate

3. Install requirements
    pip install -r requirements.txt

4. Add your database URL to .env file (not needed for epson printer)
    DATABASE_URL=postgresql://user:password@localhost:5432/database

5. Redirect port for native epson printer without IOT:
    sudo socat TCP-LISTEN:80,fork TCP:localhost:8069
