# Day 5 — Users and Groups

## 📖 What are users and groups

Linux is a **multi-user system**.

Each file and process belongs to:

* a **user**
* a **group**

This is the foundation of **system security and access control**.

---

## 👤 Check current user

```bash
whoami     # current user
id         # user ID and groups
```

Example:

```bash
uid=1000(user) gid=1000(user) groups=1000(user),27(sudo)
```

---

## 📂 User information files

```bash
/etc/passwd   # user info , anyone can see it. ex - cat /etc/passwd
/etc/shadow   # encrypted passwords, open as sudo. ex - sudo cat /etc/shadow
```

View users:

```bash
cat /etc/passwd
```

---

## 👥 Groups

Check groups:

```bash
groups
```

Check groups of a specific user:

```bash
id username
```

---

## ➕ Add user

```bash
sudo adduser username
```

This will:

* create user
* create home directory
* set password

---

## ❌ Delete user

```bash
sudo deluser username
```

Delete with home directory:

```bash
sudo deluser --remove-home username
```

---

## 👥 Manage groups

Create group:

```bash
sudo groupadd devops
```

Add user to group:

```bash
sudo usermod -aG devops username # sudo usermod -aG devops $USER ($USER is a variabe means you) this command will add you to group "devops"
```

Remove user from group:

```bash
sudo deluser username devops
```

---

## 🔐 sudo — run as root

```bash
sudo command
```

Root user = full system access ⚠️

Add user to sudo group:

```bash
sudo usermod -aG sudo username
```

---

## ⚙️ Switch user

```bash
su username
```

Switch to root:

```bash
sudo su
```

---

## 🔥 Real DevOps examples

Create "deploy" user:

```bash
sudo adduser deploy
sudo usermod -aG sudo deploy
```

Give access to project:

```bash
sudo chown -R deploy:deploy /var/www/app
```

---

## ⚠️ Important notes

* never work as root unless necessary
* use `sudo` instead
* always control group access
* wrong permissions = security risk

---

## 🧠 Key concepts

* every process runs as a user
* access is controlled by:

  * users
  * groups
  * permissions
* Linux security model is simple but powerful

---

## 🚀 Key takeaway

* know `whoami`, `id`, `groups`
* manage users with `adduser`, `deluser`
* manage groups with `groupadd`, `usermod`
* use `sudo` safely
