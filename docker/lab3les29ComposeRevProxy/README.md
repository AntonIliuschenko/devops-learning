# Day 29 — Docker Compose Reverse Proxy (Nginx → App)

## 📌 Overview

This lab demonstrates how to run multiple containers using Docker Compose and connect them via an internal network.

We configure **Nginx as a reverse proxy** that forwards incoming HTTP requests to an application container.

---

## 🧠 Architecture

```
Client (localhost:8080)
        ↓
     Nginx
        ↓
     App (Python HTTP server)
```

* **Nginx** acts as an entry point
* **App** serves HTTP content
* Docker Compose provides networking between containers

---

## 📁 Project Structure

```
.
├── docker-compose.yml
├── nginx.conf
```

---

## ⚙️ Configuration

### 🔹 Nginx config (`nginx.conf`)

```nginx
events {}

http {
    server {
        listen 80;

        location / {
            proxy_pass http://app:9000;
        }
    }
}
```

### 🔹 Docker Compose (`docker-compose.yml`)

```yaml
version: "3"

services:
  nginx:
    image: nginx
    ports:
      - "8080:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf

  app:
    image: python:3.11-slim
    command: ["python", "-m", "http.server", "9000"]
```

---

## 🚀 How to Run

```bash
docker-compose up -d
```

---

## 🔍 Verify

```bash
curl localhost:8080
```

You should receive a response from the Python HTTP server.

---

## 🧠 Key Concepts

* **Docker Compose** manages multiple containers
* Containers communicate via **service names**
* `app` is reachable from `nginx` using:

```bash
http://app:9000
```

* `localhost` inside a container refers to itself, not other containers

---

## ❗ Common Mistakes

* Using `localhost` instead of service name (`app`)
* Forgetting to match ports between app and nginx
* Not rebuilding containers after config changes

---

## 💡 Important Notes

* Containers are ephemeral (temporary)
* Configuration is injected via volumes
* Networking is handled automatically by Docker Compose

---

## 🧪 Practice Ideas

* Change app port (e.g., 8000 → 9000) and update nginx config
* Add another service and route traffic
* Replace Python server with a custom app

---

## ✅ Result

You now have a working setup where:

* Nginx receives requests on port `8080`
* Proxies them to another container (`app`)
* Demonstrates real-world microservice communication

---

## 🏁 Conclusion

This setup simulates a basic production architecture:

* Reverse proxy (Nginx)
* Application service
* Container networking

This is a foundational pattern used in DevOps and backend systems.
