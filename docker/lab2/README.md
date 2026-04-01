# 🚀 Docker + Nginx (Custom Port 8081)

## 📌 Project Description

In this task, a Docker image was built based on **nginx** with the following customizations:

* the default server port was changed from `80` to `8081`
* a custom nginx configuration file was added
* a custom HTML page was created and served

---

## 📂 Project Structure

```
.
├── Dockerfile
├── default.conf
├── index.html
└── README.md
```

---

## ⚙️ Technologies Used

* Docker
* Nginx

---

## 🧠 What Was Done

### 1. Nginx Configuration

A custom `default.conf` file was created to:

* change the listening port to `8081`
* configure static content serving

```nginx
server {
    listen 8081;

    location / {
        root /usr/share/nginx/html;
        index index.html;
    }
}
```

---

### 2. HTML Page

A custom `index.html` file was created:

```html
<h1>Another port 8081</h1>
```

---

### 3. Dockerfile

The Dockerfile builds an image based on nginx and copies the configuration and HTML files:

```dockerfile
FROM nginx:1.25

COPY default.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/
```

---

### 4. Build the Image

```bash
docker build -t my-nginx .
```

---

### 5. Run the Container

```bash
docker run -p 8080:8081 my-nginx
```

---

## 🌐 Result

After running the container, the application is available at:

```
http://localhost:8080
```

The browser displays the custom page:

```
Another port 8081
```

---

## 💡 Conclusion

During this task:

* learned how to build custom Docker images
* understood basic nginx configuration
* changed the internal container port
* configured port mapping between host and container
* practiced serving static content with nginx
