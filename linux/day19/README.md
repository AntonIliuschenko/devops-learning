# 📄 Day 19 — users, groups, permissions

## What are users and groups

Linux is a **multi-user system**, where access is controlled by:

* users
* groups
* permissions

Each file and process belongs to a user and a group.

---

## 👤 Users

Each user has:

* **UID** (User ID)
* **GID** (Primary Group ID)
* **home directory**
* **default shell**

### Check current user

```bash
whoami
id
```

Example:

```bash
uid=1000(user) gid=1000(user) groups=1000(user),27(sudo)
```

---

## 📁 System files

### `/etc/passwd`

Contains basic user information:

```bash
cat /etc/passwd
```

Format:

```
username:x:UID:GID:comment:home:shell
```

Example:

```
user:x:1000:1000:User:/home/user:/bin/bash
```

---

### `/etc/shadow`

Stores **encrypted passwords** (root only):

```bash
sudo cat /etc/shadow
```

---

### `/etc/group`

Defines groups:

```bash
cat /etc/group
```

---

## 👥 Groups

Check groups:

```bash
groups
```

Add user to group:

```bash
sudo usermod -aG docker user
```

👉 Important: use `-aG` (append), otherwise user will be removed from other groups.

---

## 🔐 Permissions

Check permissions:

```bash
ls -l
```

Example:

```
-rw-r--r-- 1 user user 1234 Mar 23 file.txt
```

---

## 📊 Permission structure

```
-rw-r--r--
```

Breakdown:

* **-** → file type
* **rw-** → owner
* **r--** → group
* **r--** → others

---

## 🔢 Numeric permissions (chmod)

| Number | Permission |
| ------ | ---------- |
| 7      | rwx        |
| 6      | rw-        |
| 5      | r-x        |
| 4      | r--        |
| 0      | ---        |

Example:

```bash
chmod 755 file
```

Means:

* owner → rwx (7)
* group → r-x (5)
* others → r-x (5)

---

## ✏️ Symbolic mode

```bash
chmod +x script.sh
chmod u+x file
chmod g-w file
```

* `u` = user
* `g` = group
* `o` = others

---

## 👑 Change ownership

```bash
chown user:user file
```

Change only group:

```bash
chown :group file
```

Recursive:

```bash
chown -R user:user directory/
```

---

## ⚡ Sudo (superuser)

Run command as root:

```bash
sudo command
```

Why needed:

* install packages
* manage users
* change system configs

---

## 🚨 Common real-world issues

### Permission denied

Example:

```bash
./script.sh: Permission denied
```

Fix:

```bash
chmod +x script.sh
```

---

### Cannot access file

```bash
cat file.txt
Permission denied
```

Fix:

```bash
sudo chown user:user file.txt
```

---

### Service cannot read files

Often happens with nginx/docker.

Fix:

```bash
sudo chown -R www-data:www-data /var/www
```

---

## 🧠 Important concepts

Security in Linux is based on:

* users
* groups
* permissions

👉 If something doesn’t work:

1. Check **who owns the file**
2. Check **permissions**
3. Check **which user runs the process**

---

## ✅ Summary

| Task               | Command  |
| ------------------ | -------- |
| Current user       | `whoami` |
| User info          | `id`     |
| File permissions   | `ls -l`  |
| Change permissions | `chmod`  |
| Change owner       | `chown`  |
| Run as root        | `sudo`   |

---
