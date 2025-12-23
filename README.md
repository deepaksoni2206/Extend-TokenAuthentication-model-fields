Here is the professional **README.md** file for your project in English. It is structured to be clear, professional, and easy for others (or recruiters) to understand.

---

# Custom Token Auth DRF 🚀

This project demonstrates how to extend the default **TokenAuthentication** in Django Rest Framework (DRF). By default, DRF's Token model only provides `Key`, `User`, and `Created` fields. In this project, we have customized it to include an additional field called **`origin`** to track where the user is logging in from (e.g., Android, Web, iOS).

## ✨ Features

* **Custom Token Model:** Inherits from DRF’s base token but adds a custom `origin` field.
* **Custom Authentication Backend:** Configured to use the custom model instead of the default one.
* **Simple Registration:** An API to register new users without needing an email.
* **Login with Tracking:** Generates a token and saves the "Origin" of the request.

---

## 🛠 Tech Stack

* **Backend:** Django 5.x
* **API Toolkit:** Django Rest Framework (DRF)
* **Database:** SQLite

---

## 🚀 Setup & Installation

### 1. Clone the Repository

```bash
git clone <your-repository-link>
cd CustomTokenAuth-DRF

```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on Mac/Linux:
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install django djangorestframework

```

### 4. Database Migrations

Since we are using a custom model, running migrations is mandatory to create the new tables.

```bash
python manage.py makemigrations
python manage.py migrate

```

---

## 🔌 API Documentation

### 1. User Registration

* **Endpoint:** `POST /api/register/`
* **Payload:**

```json
{
    "username": "aman_123",
    "password": "securepassword"
}

```

### 2. User Login (Generate Token)

* **Endpoint:** `POST /api/login/`
* **Payload:**

```json
{
    "username": "aman_123",
    "password": "securepassword",
    "origin": "Android App"
}

```

* **Response:** Returns the `token` key and the `origin` saved in the database.

---

## 📂 Core Logic Explanation

* **`models.py`**: We inherited from `rest_framework.authtoken.models.Token` to add the `origin` field.
* **`authentication.py`**: We created a class `CustomTokenAuthentication` and pointed its `model` attribute to our new `CustomToken` model.
* **`settings.py`**: Updated `DEFAULT_AUTHENTICATION_CLASSES` to use our custom authentication class instead of the built-in one.

---

## 🛡 License

This project is open-source and available under the MIT License.


