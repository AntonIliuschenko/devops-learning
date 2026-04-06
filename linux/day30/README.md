# Day 30 — Docker Compose: Nginx + App + PostgreSQL

## 📌 Overview

This lab demonstrates a multi-container setup using Docker Compose.

We run three services:

* **Nginx** — reverse proxy (entry point)
* **App** — simple Python HTTP server
* **PostgreSQL** — database service

At this stage, the database is running but not yet used by the application.

---

## 🧠 Architecture

```text
Client (localhost:8080)
        ↓
      Nginx
        ↓
       App (Python HTTP server)
        
Database (PostgreSQL) — running separately
```

---

## 📁 Project Structure

```text
.
├── docker-compose.yml
├── nginx.conf
```

---

## ⚙️ docker-compose.yml

```yaml
version: "3"

services:

  nginx:
    image: nginx
    ports:
      - "8080:80"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
    depends_on:
      - app

  app:
    image: python:3.11-slim
    command: ["python", "-m", "http.server", "8000"]
    depends_on:
      - db
    environment:
      - DB_HOST=db
      - DB_NAME=mydb
      - DB_USER=user
      - DB_PASSWORD=pass

  db:
    image: postgres
    environment:
      - POSTGRES_DB=mydb
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
    volumes:
      - db_data:/var/lib/postgresql

volumes:
  db_data:
```

---

## ⚙️ Nginx Configuration

```nginx
server {
    listen 80;

    location / {
        proxy_pass http://app:8000;
    }
}
```

---

## 🚀 How to Run

```bash
docker-compose up -d
```

---

## 🔍 Verification

Check containers:

```bash
docker-compose ps
```

Expected:

```text
nginx → Up
app   → Up
db    → Up
```

---

Test access:

```bash
curl localhost:8080
```

---

## 🧠 Key Concepts

### 1. Reverse Proxy

Nginx forwards requests:

```text
client → nginx → app
```

---

### 2. Container Communication

Containers communicate via service names:

```text
nginx → app
app → db
```

NOT via `localhost`.

---

### 3. Environment Variables

```text
DB_HOST=db
DB_NAME=mydb
DB_USER=user
DB_PASSWORD=pass
```

Used to pass configuration to containers.

---

### 4. Volumes

```text
db_data → persistent storage for PostgreSQL
```

Database data survives container restart.

---

### 5. Container Lifecycle

* Container runs while main process is active
* If process stops → container exits

---

## ❗ Important Notes

* The **app does not yet use the database**
* PostgreSQL is running for learning networking and configuration
* Next step is to connect the app to the database

---

## 🏁 Conclusion

This setup demonstrates:

* Multi-container architecture
* Reverse proxy with Nginx
* Service communication via Docker network
* Environment variables usage
* Persistent storage with volumes

---

## 🚀 Next Step

👉 Connect the app to PostgreSQL
👉 Build a real backend service
