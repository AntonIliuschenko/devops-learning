# 📄 Day 29 — Docker Networking & Docker Compose

## 🧠 Overview

This stage introduces:

* container networking
* multi-container applications

👉 moving from:

```text
single container → full service
```

---

## 🌐 Docker Networking Basics

### 🔹 Example

```bash
docker run -d -p 8080:80 nginx
```

---

### 🔎 What happens

* container gets its own IP
* Docker creates virtual network
* port is exposed to host

---

### ⚠️ Important Concept

```text
localhost inside container ≠ host machine
```

---

## 🔍 Check Networks

```bash
docker network ls
```

Default networks:

* `bridge` — default network
* `host` — shares host network
* `none` — no networking

---

### 🔹 Inspect Network

```bash
docker network inspect bridge
```

👉 shows:

* connected containers
* IP addresses
* network settings

---

## 🔗 Container Communication

### ❌ Wrong

```text
localhost
```

---

### ✅ Correct

```text
container_name
```

👉 containers communicate using **names (DNS inside Docker network)**

---

## ⚙️ Docker Compose

Docker Compose is used to:

* run multiple containers
* define services in one file
* manage application stack

---

## 📄 Example `docker-compose.yml`

```yaml
version: "3"

services:
  web:
    image: nginx
    ports:
      - "8080:80"

  app:
    image: ubuntu
    command: ["sleep", "infinity"]
```

---

## 🔍 Explanation

### 🔹 services

Defines containers (services)

---

### 🔹 web

* nginx container
* exposed to host

---

### 🔹 ports

```text
host:container
8080 → 80
```

---

### 🔹 app

* second container
* runs indefinitely

---

## 🚀 Run Compose

```bash
docker-compose up
```

---

### 🔹 Run in background

```bash
docker-compose up -d
```

---

### 🔹 Stop all

```bash
docker-compose down
```

---

## 🧠 Why Compose Matters

Without compose:

```text
docker run ...
docker run ...
docker run ...
```

👉 hard to manage

---

With compose:

```text
one file → full system
```

---

## 🔥 Real DevOps Scenario

Typical stack:

* backend (API)
* database (PostgreSQL)
* nginx (reverse proxy)
* redis (cache)

👉 all managed via docker-compose

---

## 💡 Key Takeaways

* containers have isolated networking
* communication via container names
* Docker Compose manages multi-container apps
* infrastructure defined as code

---

## 📝 Notes

* avoid using localhost between containers
* use service names as hostnames
* compose simplifies development and testing
