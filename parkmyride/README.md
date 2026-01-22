# ParkMyRide

Simple Django-based Vehicle Parking Booking System (ParkMyRide).

Setup (Windows):

1. Create a virtual environment and activate it:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

2. Install requirements:

```powershell
pip install -r requirements.txt
```

3. Run migrations and start server:

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

4. Open http://127.0.0.1:8000/ in your browser.

Notes:
- Default UI is in `templates/` and styles in `static/css/global.css`.
- Use `/signup/` and `/login/` to register and log in.
