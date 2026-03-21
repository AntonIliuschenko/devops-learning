# Day 4 — File Permissions

## 📖 What are permissions

Permissions define **who can access a file and what they can do with it**.

There are 3 types of users:

* **owner** — file owner
* **group** — group of users
* **others** — everyone else

---

## 🔍 View permissions

```bash
ls -l
```

Example output:

```bash
-rw-r--r-- 1 user user 1234 Mar 21 file.txt
```

---

## 🧩 Permission structure

```bash
-rw-r--r--
```

Breakdown:

```bash
- rw- r-- r--
  │   │   │
  │   │   └── others
  │   └────── group
  └────────── owner
```

---

## 🔑 Permission types

| Symbol | Meaning |
| ------ | ------- |
| r      | read    |
| w      | write   |
| x      | execute |

---

## 🔢 Numeric (octal) permissions

Each permission has a number:

| Permission | Value |
| ---------- | ----- |
| r          | 4     |
| w          | 2     |
| x          | 1     |

Examples:

```bash
755 = rwxr-xr-x
644 = rw-r--r--
700 = rwx------
```

---

## ⚙️ chmod — change permissions

### Numeric mode

```bash
chmod 755 script.sh
chmod 644 file.txt
```

### Symbolic mode

```bash
chmod +x script.sh        # add execute
chmod -w file.txt         # remove write
chmod u+x script.sh       # owner + execute
chmod g-w file.txt        # group - write
```

---

## 👤 chown — change owner

```bash
chown user file.txt
chown user:group file.txt
```

Recursive:

```bash
chown -R user:group /var/www # change owner of the folder /var/www
```

---

## 🧠 chmod vs chown

* `chmod` → changes **permissions**    # changes permitions what to do with file (execute, write,read)
* `chown` → changes **owner**	       # changes who can do operations with file/folder	

---

## ⚠️ Important notes

* `x` (execute) is required to run scripts
* wrong permissions can break applications
* never use `777` (means all can do everything) in production ❌

---

## 🔥 Real DevOps examples

Make script executable:

```bash
chmod +x deploy.sh
```

Fix web server permissions:

```bash
chown -R www-data:www-data /var/www
chmod -R 755 /var/www
```

Secure private key:

```bash
chmod 600 id_rsa
```

---

## 🚀 Key takeaway

* permissions = security
* understand `rwx`
* know `chmod` and `chown`
* use numeric and symbolic modes

