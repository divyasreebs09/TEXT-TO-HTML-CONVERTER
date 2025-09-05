# 📄 txt2html

A simple **Django web application** that converts plain text into clean **HTML format**.

## 🚀 Features

* Upload or input plain text
* Converts text into HTML automatically
* Simple and user-friendly interface

## 🛠️ Tech Stack

* **Python 3.13**
* **Django 5.2.4**
* SQLite (default Django DB)
* 
## 📂 Project Structure

```
txt2html/
│
├── converter/         # Main app (handles text to HTML conversion)
├── txt2html/          # Project settings and configuration
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/txt2html.git
   cd txt2html
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv env
   env\Scripts\activate   # On Windows
   source env/bin/activate  # On Mac/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**

   ```bash
   python manage.py migrate
   ```

5. **Start the development server**

   ```bash
   python manage.py runserver
   ```

6. Open in your browser:
   👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📌 URLs

* `/` → Homepage
* `/convert/` → Convert text to HTML


