# 📄 Customer Support Ticketing System

A **role-based Customer Support Ticketing System** built with **Django**, designed to simulate a real-world helpdesk workflow.
The platform allows **customers** to create support requests, **agents** to manage and resolve them, and **administrators** to control access and monitor operations.

This project demonstrates practical backend architecture, clean role-based permissions, and scalable workflow design similar to modern SaaS support platforms.

---

## 🚀 Features

### 🔐 Role-Based Authentication

* Customer
* Support Agent
* Admin

### 🎫 Ticket Lifecycle Management

```
OPEN → IN PROGRESS → RESOLVED → CLOSED
```

* Customer ticket creation & tracking
* Agent assignment workflow
* Threaded conversations (replies inside tickets)
* Search, filtering & pagination
* Role-specific dashboards

---

## 🧱 Tech Stack

### 🧩 Backend

* Python
* Django

### 🗄️ Database

* SQLite (Development)
* PostgreSQL-ready architecture

### 🎨 Frontend

* Django Templates
* HTML
* CSS

### 🛠️ Tools

* Git & GitHub

---

## 🗂️ Project Structure

```
project_root/
│
├── accounts/        # Authentication & role handling
├── tickets/         # Ticket models, views, replies
├── core/            # Dashboard & home views
├── templates/       # HTML templates
├── static/          # CSS files
└── manage.py
```

---

## 👤 User Roles & Capabilities

### 👨‍💻 Customer

* Create tickets
* View own tickets
* Reply to conversations

### 🧑‍💼 Support Agent

* View assigned tickets
* Assign unassigned tickets
* Update ticket status
* Reply to customers

### 👨‍💼 Admin

* Manage users & roles via Django Admin
* Full visibility across all tickets

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Mac/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If no requirements file exists:

```bash
pip install django
```

### 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run Development Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🔐 Authentication & Groups

Roles are implemented using **Django Groups**.

Create the following groups from Django Admin:

* `Customer`
* `SupportAgent`

Assign users to the appropriate group to enable role-specific dashboards and permissions.

---

## 📌 Key Functional Highlights

* Agents can see **both assigned and unassigned tickets**
* Customers only see **their own tickets**
* Closed tickets disable further updates
* Role-based navigation and dashboards
* Clean separation of concerns using Django apps

---

## 🧠 What This Project Demonstrates

* Real-world backend architecture with Django
* Role-based permission handling
* Scalable database modeling
* Practical SaaS-style workflow design
* Maintainable project structure

---

## 🔮 Future Improvements

* Email notifications
* REST API using Django REST Framework
* Docker containerization
* Production deployment
* File attachments in replies
* Ticket priority levels

---

## 📸 Screenshots


## 📄 License

This project is intended for **educational and demonstration purposes**.

---


