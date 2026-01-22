# 🚗 ParkMyRide – Vehicle Parking Booking System

ParkMyRide is a full-stack web application that allows users to search, book, and manage vehicle parking slots online. It provides an easy-to-use interface for customers and a powerful admin panel for managing parking locations, slots, and bookings.

Built using **Django (MVT)** for the backend and **HTML, CSS, and JavaScript** for the frontend, with **SQLite3** as the database.

---

## ✨ Features

### 👤 User Features

* User registration and login
* Search parking slots by location, date, time, and vehicle type
* View real-time slot availability
* Book parking slots
* View booking history
* Cancel upcoming bookings
* Responsive UI with modern card layout

### 🛠️ Admin Features

* Admin authentication
* Add, update, and delete parking locations
* Manage parking slots
* Approve or cancel bookings
* View reports and revenue summary

---

## 🧰 Technology Stack

### Frontend

* HTML5
* CSS3 (Pure CSS, no frameworks)
* JavaScript

### Backend

* Django (MVT Architecture)
* SQLite3 Database

### Tools

* Python 3.x
* Django ORM

---

## 📁 Project Structure

```
parkmyride/
│
├── parkmyride/          # Main project settings
│
├── accounts/           # User authentication app
├── parking/            # Locations and parking slots app
├── bookings/           # Booking management app
│
├── templates/          # All HTML templates
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── search.html
│   ├── booking.html
│   ├── history.html
│   └── admin/
│
├── static/
│   ├── css/style.css   # Global styling
│   └── js/main.js      # JavaScript logic
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 🖥️ Pages Included

### User Pages

* Home Page
* Sign Up Page
* Login Page
* User Dashboard
* Search Parking Page
* Booking Page
* Booking History Page

### Admin Pages

* Admin Login
* Admin Dashboard
* Manage Parking Slots
* Manage Bookings
* Reports / Analytics

---

## ⚙️ Setup Instructions

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/parkmyride-parking-booking-system.git
cd parkmyride-parking-booking-system
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Mac/Linux
```

### 3️⃣ Install Dependencies

```
pip install django
```

### 4️⃣ Apply Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser (Admin)

```
python manage.py createsuperuser
```

### 6️⃣ Run the Server

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🗃️ Sample Data

The project includes sample parking locations and 15 parking slots from Pune such as:

* Shivaji Nagar
* Hinjewadi Phase 1
* Wakad
* Baner
* Aundh
* Kothrud
* Swargate
* Hadapsar
* Viman Nagar
* Koregaon Park

Slots include realistic pricing and vehicle types (Car, Bike, Truck).

---

## 🔐 Authentication

* User authentication uses Django’s built-in User model
* Passwords are securely hashed
* Session-based login system

---

## 📊 Functional Highlights

* Prevents double booking of the same slot
* Displays availability status in real time
* Booking price calculated automatically
* Clean UI inspired by modern parking apps

---

## 🚀 Future Enhancements

* Online payment gateway integration
* Google Maps integration
* QR code ticket generation
* Email / SMS booking notifications
* REST API support
* Mobile app version

---

## 🧪 Testing

Basic manual testing:

* User registration & login
* Slot search & booking
* Booking cancellation
* Admin CRUD operations

---

## 📜 License

This project is created for educational and demonstration purposes.

---

## 🙌 Acknowledgements

* Django Documentation
* Open-source community

---

## 📬 Contact

For questions or suggestions:

**Developer:** Your Name
**Email:** [your-email@example.com](mailto:your-email@example.com)

---

✨ *Park smarter. Book faster. Welcome to ParkMyRide.*
