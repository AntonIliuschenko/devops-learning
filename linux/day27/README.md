# 📄 Day 27 — Docker Deeper (logs, exec, inspect, volumes)

## 🧠 Overview

This section covers essential Docker tools for:

* debugging containers
* inspecting runtime state
* interacting with running services
* managing data

👉 These are daily tools for DevOps engineers.

---

## 📜 docker logs

### 🔹 What it does

```bash
docker logs CONTAINER_ID
```

Shows:

* stdout
* stderr

👉 logs produced by the application

---

### 🔹 Follow logs (real-time)

```bash
docker logs -f CONTAINER_ID
```

#### Flag:

* `-f` → follow (like `tail -f`)

---

### 🔹 Last lines

```bash
docker logs --tail 20 CONTAINER_ID
```

#### Flag:

* `--tail` → show last N lines

---

### 🔥 DevOps Meaning

👉 First tool to check when something breaks.

---

## 🖥️ docker exec

### 🔹 What it does

```bash
docker exec CONTAINER_ID command
```

Runs a command inside a running container.

---

### 🔹 Interactive shell

```bash
docker exec -it CONTAINER_ID bash
```

#### Flags:

* `-i` → interactive
* `-t` → terminal

---

### 🔹 Run single command

```bash
docker exec CONTAINER_ID ls /
```

---

### ⚠️ Important

👉 Use for debugging, NOT for permanent changes.

---

## 🔍 docker inspect

### 🔹 What it does

```bash
docker inspect CONTAINER_ID
```

Returns full container info in JSON format.

---

### 🔹 Example (find IP)

```bash
docker inspect CONTAINER_ID | grep IPAddress
```

---

### 🔹 What you can find

* container IP
* volumes
* ports
* environment variables
* network settings

---

### 🔥 DevOps Meaning

👉 Deep debugging tool when something is unclear.

---

## 💾 Volumes (VERY IMPORTANT)

### ❗ Problem

```text
container deleted → data lost
```

---

### 🔹 Solution

Use volumes:

```bash
docker run -d -p 8080:80 -v $(pwd):/usr/share/nginx/html nginx
```

---

### 🔎 Flags:

* `-v` → mount volume
* `$(pwd)` → current host directory
* `/usr/share/nginx/html` → path inside container

---

### 📊 What happens

```text
host folder ↔ container folder
```

👉 changes are shared

---

### 🔥 Example

```bash
echo "Hello DevOps" > index.html
curl localhost:8080
```

👉 you will see your content

---

## 🧠 Why Volumes Matter

* containers are ephemeral
* data must persist
* separation of compute and storage

---

## ⚙️ DevOps Workflow

```text
run container
↓
check logs
↓
exec inside (if needed)
↓
inspect config
↓
use volumes for data
```

---

## 🚀 Debug Workflow

```bash
docker ps
docker logs CONTAINER_ID
docker exec -it CONTAINER_ID bash
docker inspect CONTAINER_ID
```

---

## 💡 Key Takeaways

* `logs` → first step in debugging
* `exec` → inspect inside container
* `inspect` → full metadata
* `volumes` → persistent data

---

## 📝 Notes

* never rely on container filesystem for data
* always externalize data using volumes
* containers should be replaceable at any time

## Practice: Mounting a Local Website into an Nginx Docker Container

For practicing and testing how to mount a directory into a Docker container, I created a simple welcome webpage using ChatGPT. I decided to keep this example in my repository inside a folder called `web_site`.

On my local machine, inside my Git project, I created the folder `web_site` and added an `index.html` file with the welcome page code.

### Steps

1. Navigate to the folder containing the website:

```bash
cd web_site/
```

2. Run an Nginx container and mount the current directory into it:

```bash
docker run -d -p 8080:80 -v $PWD:/usr/share/nginx/html nginx
```

### Explanation

* `$PWD` refers to the current directory on the host machine
* `/usr/share/nginx/html` is the default directory where Nginx serves static files inside the container
* The `-v` flag mounts the local folder into the container

### Result

After running the container, I opened the browser and navigated to:

```
http://127.0.0.1:8080/
```

Instead of the default Nginx page, I saw my custom welcome page.

### Conclusion

This confirms that the local directory was successfully mounted into the container, and Nginx is serving files directly from the host machine.

This is a simple but powerful way to test changes without rebuilding Docker images.

### Screenshot

Below is the result of the mounted website running in the browser:
![Screenshot](web_site/screenshot.png)
