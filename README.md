# 🛒 BUYROUTE — E-Commerce Platform

**BUYROUTE** is a full-stack e-commerce web application built with **Python Flask and MySQL**, designed to provide a smooth and structured online shopping experience.

The platform includes user authentication, email OTP verification, product browsing, shopping cart management, order processing, invoice generation, and an administrative dashboard for managing products.

---

## 📌 Overview

BUYROUTE provides separate functionality for customers and administrators.

### 👤 Customer Features

* User registration and login
* Email OTP verification
* Product search and browsing
* Shopping cart management
* Order placement and tracking
* Invoice generation
* Secure session handling

### 🔐 Admin Features

* Admin dashboard
* Product management
* Add new products
* Update existing products
* Delete products

---

## ✨ Features

| Feature                | Description                                         |
| ---------------------- | --------------------------------------------------- |
| 🔑 User Authentication | Registration and login functionality                |
| 📧 Email OTP           | Email-based OTP verification                        |
| 🔍 Product Search      | Search and browse available products                |
| 🛒 Shopping Cart       | Add and manage products in the cart                 |
| 📦 Order Management    | Place and track orders                              |
| 🧾 Invoice Generation  | Generate invoices for orders                        |
| 🛠️ Admin Dashboard    | Manage products through an administrative interface |
| 📋 Product Management  | Add, update, and delete products                    |
| 🔒 Session Handling    | Secure user session management                      |

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* Bootstrap
* JavaScript

### Backend

* Python
* Flask

### Database

* MySQL

---

## 📂 Project Structure

```text
BUYROUTE/
│
├── app.py                 # Main Flask application
├── otp.py                 # OTP verification functionality
├── cmail.py               # Email service functionality
│
├── templates/             # HTML templates
│   └── ...
│
├── static/                # Static assets
│   ├── css/
│   ├── js/
│   └── images/
│
└── README.md
```

---

## ⚙️ Application Architecture

```text
              ┌──────────────────────┐
              │      User / Admin     │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   HTML / CSS / JS    │
              │      Bootstrap       │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │     Flask Backend    │
              │       Python         │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │     MySQL Database   │
              └──────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

Make sure the following are installed:

* Python 3.x
* MySQL
* pip

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd BUYROUTE
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Create the required MySQL database and configure the database connection used by the Flask application.

Keep database credentials and other sensitive configuration values out of the repository.

### 5. Run the Application

```bash
python app.py
```

The application will then be available through the local Flask server.

---

## 🔐 Security

BUYROUTE includes secure session handling and email OTP verification as part of its authentication flow.

For development and deployment:

* Do not commit database passwords.
* Do not commit email credentials.
* Do not commit API keys or other secrets.
* Store sensitive configuration securely using environment variables or an appropriate secret-management solution.

---

## 🔮 Future Enhancements

The following features can be added in future versions:

* 💳 Online payment gateway integration
* ⭐ Product reviews and ratings
* ❤️ Wishlist functionality
* 📊 Advanced analytics dashboard

---

## 👨‍💻 Author

**Krishna Sai**

**B.Tech — Computer Science Engineering, 2026**

---

## 📄 License

This project is intended for educational and development purposes.

---

### ⭐ BUYROUTE

*A Flask-powered e-commerce platform focused on providing a structured online shopping experience.*
