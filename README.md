
# 🌩️ Cloud-Based Inventory Management System

**Technologies: Python, Tkinter, SQLite, Flask (optional for cloud API), Docker**

A Python desktop application that helps businesses manage inventory efficiently with a clean, interactive GUI built using Tkinter. The system allows users to add, update, delete, and search inventory items, track stock levels, and associate items with suppliers. Data is stored locally in SQLite with an option to sync to a Flask-based cloud API, making it accessible from multiple clients.

---

## 🔧 Features

- 🖥️ Desktop UI built with **Tkinter**
- 🗃️ Local database using **SQLite**
- ☁️ Optional **Flask API** for cloud sync
- 🐳 **Dockerized** for easy deployment
- 📦 Add, update, delete, and search inventory items
- 📊 Track stock levels and suppliers
- 🔐 Secure and scalable for multi-user cloud access (via AWS or Azure)

---

## 🖼️ UI Preview

---

## **Login Screen**

![Screenshot 2025-02-17 120421](https://github.com/user-attachments/assets/8f66ead5-7a97-43f7-921d-64691a1b93c7)

---
---

## **Dashboard**

![Screenshot 2025-02-17 120356](https://github.com/user-attachments/assets/4ba370a1-5c8c-4398-bc10-67b2669e777e)

---
---

## **Billing Area**

![Screenshot 2025-02-17 120436](https://github.com/user-attachments/assets/9b77dadb-2669-4860-b7a7-dfafc52279d8)

---

## 📂 Folder Structure 
📂 IMS
├── **app.py
├── billing.py
├── category.py
├── create_db.py
├── dashboard.py
├── email_pass.py
├── employee.py
├── ims.db
├── login.py
├── product.py
├── sales.py
├── supplier.py**
│
├── **bill/**                    # auto‑generated sales bills
│   ├── 10202541.txt
│   ├── 10204136.txt
│   ├── …                   # (8 more *.txt files)
│   └── 3232329.txt
│
├── **images/**                  # all UI graphics & icons
│   ├── bg.png
│   ├── cat.jpg
│   ├── …
│   ├── IMS.ico
│   └── **inventory system/**
│       ├── bill_logo.png
│       ├── close_eye.png
│       ├── …
│       └── total_sup.png
│
└── __pycache__/             # compiled byte‑code (ignored via .gitignore)
    ├── app.cpython‑312.pyc
    ├── category.cpython‑312.pyc
    ├── …
    └── supplier.cpython‑312.pyc

---

## 🛠️ Tech Stack

| Layer                    | Technology                                          | Purpose                                                                                      |
| ------------------------ | --------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| GUI / Front‑end          | **Tkinter**                                         | Native desktop interface for adding, editing, and viewing stock                              |
| Service / API (optional) | **Flask** (or FastAPI)                              | Exposes REST endpoints so other apps—or additional Tkinter clients—can sync over the network |
| Database                 | **SQLite** (local) → **PostgreSQL / MySQL** (cloud) | Starts lightweight, then scales to managed cloud DB                                          |
| DevOps                   | **Docker**, Docker Compose                          | Package GUI client, API service, and DB into portable containers                             |
| Cloud                    | AWS EC2 / Lightsail or Azure VM                     | Run the API + DB in the cloud so multiple Tkinter clients can connect securely               |

---

## 📌 Core Features
**1. Real‑time stock dashboard** – sortable table shows live quantities, cost price & selling price.

**2. CRUD operations** – add, update, delete items with validation (SKU uniqueness, non‑negative qty).

**3. Supplier & purchase order tracking** – link items to vendor profiles and record restock events.

**4. Search & barcode scan** – quick lookup by name, SKU, or external USB barcode reader.

**5. Role‑based login** – admin vs operator rights (Tkinter login window + hashed passwords).

**6. Offline‑first sync** – SQLite keeps working offline; when back online, auto‑syncs via Flask API.

---

## 🚀 Deployment Highlights

**Single‑user mode**: Ship just the Tkinter app with embedded SQLite DB.

**Multi‑user / cloud mode**:

    1. Build Docker images for the API and database.

    2. Push to a cloud VM or container service.

    3. Point each Tkinter client at the cloud API using an environment variable (API_URL).

**CI/CD**: GitHub Actions builds images, runs pytest, and pushes to Docker Hub on every commit.

---

## 🎯 Outcome & Skills Demonstrated
**End‑to‑end Python project**: GUI (Tkinter), REST (Flask/FastAPI), DB (SQLAlchemy).

Containerization & cloud deployment using Docker.

Practical design of offline‑capable desktop tools that can graduate to multi‑user cloud setups.

Strong understanding of data modeling, authentication, and networked application architecture—all in pure Python.

---

## 🔮 Future Improvements

- Add user authentication with JWT
- Generate downloadable reports (PDF/CSV)
- Implement barcode scanning integration
- Unit testing for backend logic
- Artificial Intelligence(AI) and Machine Learning(ML) will help to predict demand , automate stock replenishment and optimize inventory levels
- Retailing Integration means Seamless connectivity between online and offline stores will ensure real-time stock updates across multiple sales channels
- Enhanced Cybersecurity measures
- Augmented Reality(AR) and Virtual Reality(VR)

---

## 🙋‍♂️ Author

**Devang Angchekar**  
B.Sc. IT – St. Arnold's Degree College, University of Mumbai 
✉️ devangangchekar2004@gmail.com
[LinkedIn](https://www.linkedin.com/in/devang-angchekar-3583a02b9/) | [GitHub](https://github.com/Devang-09/) | [Instagram](https://www.instagram.com/_https_devang_)

---

## 🙌 Acknowledgements

- Python community for Tkinter docs
- Flask, SQLite, and Docker official docs

---

## 📝 License

This project is licensed under the MIT License. See [LICENSE](LICENSE.md) for details.

---

## ⭐️ Give it a Star!

If you found this project helpful or interesting, consider giving it a ⭐ on GitHub!

---

Let me know if you'd like to have Project Report.

---
