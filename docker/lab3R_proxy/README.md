# 🚀 Docker + Nginx Reverse Proxy (Lab 3)

## 📌 Project Description

In this lab, a multi-container setup was implemented using Docker.

The system consists of:

* a **backend service** (Python HTTP server)
* a **frontend service** (Nginx)
* a **Docker network** for communication between containers

Nginx is configured as a **reverse proxy**, routing requests from the client to the backend service.

---

## 🧱 Architecture

* `/` → serves static HTML via Nginx
* `/api` → proxied to backend service

---

## 📂 Project Structure

```
.
├── Dockerfile              # backend
├── app.py                 # backend application
├── nginx/
│   ├── Dockerfile         # nginx image
│   ├── default.conf       # nginx config
│   └── index.html         # frontend page
└── README.md
```

---

## ⚙️ Technologies Used

* Docker
* Nginx
* Python (http.server)

---

## 🧠 What Was Done

### 1. Backend Service

A simple Python HTTP server was created to handle API requests.

📄 `app.py`

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"message": "Hello from backend"}')

server = HTTPServer(("0.0.0.0", 5000), Handler)
server.serve_forever()
```

---

### 2. Backend Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY app.py .

CMD ["python", "app.py"]
```

---

### 3. Nginx Configuration

📄 `nginx/default.conf`

```nginx
server {
    listen 8081;

    location / {
        root /usr/share/nginx/html;
        index index.html;
    }

    location /api {
        proxy_pass http://backend:5000;
    }
}
```

---

### 4. Nginx Dockerfile

```dockerfile
FROM nginx:1.25

COPY default.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/
```

---

### 5. Docker Network

```bash
docker network create my-net
```

Used to enable communication between containers via service name (`backend`).

---

### 6. Build and Run

#### Backend

```bash
docker build -t my-backend .
docker run -d --name backend --network my-net my-backend
```

#### Nginx

```bash
docker build -t my-nginx ./nginx
docker run -p 8080:8081 --network my-net my-nginx
```

---

## 🌐 Result

After running the containers:

* Frontend доступен по:

  ```
  http://localhost:8080
  ```

* API доступен по:

  ```
  http://localhost:8080/api
  ```

---

## 🔁 Request Flow

Client → Nginx → Backend → Nginx → Client

---

## 💡 Conclusion

In this lab:

* learned how to run multiple containers
* configured Docker networking
* implemented Nginx as a reverse proxy
* connected frontend and backend services
* practiced real-world container architecture
