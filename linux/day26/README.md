# 📄 Day 26 — Docker Basics

## 🧠 Overview

Docker is a platform for running applications in **containers**.

A container is an isolated environment that includes:

* application
* dependencies
* filesystem

👉 It runs as a **process on the host**, but isolated.

---

## 🔥 Why Docker Is Needed

Without Docker:

* "works on my machine" problem
* dependency conflicts
* inconsistent environments

With Docker:

* same image → same behavior everywhere
* easy deployment
* reproducible environments

---

## 📦 Core Concepts

* **image** — template (blueprint of application)
* **container** — running instance of an image
* **Dockerfile** — instructions to build image
* **registry** — storage for images (e.g. Docker Hub)

---

## 🔍 Check Docker

```bash id="q3h5xa"
docker --version
```

---

## 🚀 First Container

```bash id="v8tn3f"
docker run hello-world
```

👉 Docker:

1. pulls image from registry
2. creates container
3. runs it

---

## 🖥️ Interactive Container

```bash id="7u2l2k"
docker run -it ubuntu bash
```

### 🔎 Flags:

* `-i` → interactive (keeps STDIN open)
* `-t` → pseudo-terminal (you get a shell)

👉 Result: you enter a container like a separate Linux system

Exit:

```bash id="jfh8cv"
exit
```

---

## 📊 List Containers

```bash id="7h3n1y"
docker ps
```

👉 shows running containers

```bash id="g3b8cd"
docker ps -a
```

👉 shows all containers (including stopped)

---

## 📦 List Images

```bash id="c4l6t9"
docker images
```

---

## 🛑 Stop Container

```bash id="8k2mza"
docker stop CONTAINER_ID
```

👉 sends SIGTERM → then SIGKILL (like systemd)

---

## 🗑️ Remove Container

```bash id="u9p1qe"
docker rm CONTAINER_ID
```

---

## 🧹 Remove Image

```bash id="n5x7yb"
docker rmi IMAGE_ID
```

---

## 🌐 Run Web Server

```bash id="z2c9ru"
docker run -d -p 8080:80 nginx
```

### 🔎 Flags:

* `-d` → detached mode (runs in background)
* `-p 8080:80` → port mapping

```text
host:container
8080 → 80
```

👉 Access:

```text
http://localhost:8080
```

---

## 🧠 How to Think About Containers

```text
container = process + filesystem + isolation
```

---

## ⚙️ Under the Hood

Docker uses:

* **namespaces** → isolation
* **cgroups** → resource limits

👉 This is based on Linux (what you already learned)

---

## 🧪 Practice

Run:

```bash id="g6c9x1"
docker run -d -p 8080:80 nginx
```

Test:

```bash id="c0q2nt"
curl localhost:8080
```

👉 If you see HTML → it works

---

## 🛠️ Debug Workflow

```bash id="p8z4yr"
docker ps
docker logs CONTAINER_ID
docker exec -it CONTAINER_ID bash
```

---

## 💡 Key Takeaways

* containers are isolated processes
* images are templates
* Docker ensures consistency across environments
* networking works via port mapping

---

## 📝 Notes

* containers are lightweight (not full VMs)
* everything inside container is ephemeral unless persisted
* Docker is core tool for CI/CD and deployment
