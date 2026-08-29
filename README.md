# Open Dataset Registry API

![FastAPI](https://img.shields.io/badge/FastAPI-0.141-green)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-orange)
![JWT](https://img.shields.io/badge/Auth-JWT-red)
![Render](https://img.shields.io/badge/Hosted-Render-purple)

A public catalogue of datasets — browse, search and filter by
domain, format and tags. Built with FastAPI, SQLAlchemy and JWT authentication.

---

## 🌐 Live Demo

| URL | Description |
|-----|-------------|
| [API Docs (Swagger)](https://open-dataset-registry.onrender.com/docs) | Interactive documentation |
| [All Datasets](https://open-dataset-registry.onrender.com/datasets) | Browse all datasets |
| [Search by tag](https://open-dataset-registry.onrender.com/datasets/search?tag=Canada) | Filter Canadian datasets |
| [Portfolio Website](https://kelechiede.dev) | Developer portfolio |

---

## 🚀 Features

- Public browsing and searching of datasets
- Filter by domain, format and tag simultaneously
- Result count included in search responses
- JWT Bearer token authentication for admin operations
- Full CRUD — create, read, update and delete datasets
- Auto-generated Swagger UI at `/docs`
- Bcrypt password hashing

---

## 📡 API Endpoints

### Public
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/datasets` | All datasets |
| GET | `/datasets/{id}` | Single dataset by ID |
| GET | `/datasets/search` | Search by domain, format or tag |

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register as admin |
| POST | `/auth/login` | Login and receive JWT token |

### Protected (JWT required)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/datasets` | Add a new dataset |
| PUT | `/datasets/{id}` | Update a dataset |
| DELETE | `/datasets/{id}` | Delete a dataset |

---

## 🔍 Search Examples

Filter by domain

GET /datasets/search?domain=Climate

Filter by format

GET /datasets/search?format=CSV

Filter by tag

GET /datasets/search?tag=Canada

Combine filters

GET /datasets/search?domain=Finance&format=JSON


---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Framework | FastAPI 0.141 |
| Language | Python 3.13 |
| Database | SQLite via SQLAlchemy ORM |
| Authentication | JWT (python-jose + passlib bcrypt) |
| Server | Uvicorn |
| Hosting | Render (free tier) |

---

## 🏃 Run Locally

```bash
git clone https://github.com/Kelechiede/open-dataset-registry.git
cd open-dataset-registry
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python seed.py
uvicorn main:app --reload --port 8002
```

Visit `http://127.0.0.1:8002/docs`

---

## 👨‍💻 Developer

**Kelechukwu Innocent Ede**
- 🌐 Portfolio: [kelechiede.dev](https://kelechiede.dev)
- 💼 GitHub: [github.com/Kelechiede](https://github.com/Kelechiede)
- ✉️ Primary Email: kelechukwuede@gmail.com
- ✉️ Secondary Email: info@kelechiededata.org
- 🎓 MSc Software Engineering — Memorial University of Newfoundland
- 🎓 MSc Data Science — Oslo Metropolitan University
