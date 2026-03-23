# 📄 Day 20 — special permissions

## What are special permissions

In addition to basic permissions (`rwx`), Linux has **special permission bits**:

* **setuid (SUID)**
* **setgid (SGID)**
* **sticky bit**

They allow controlled privilege management.

---

## 🔴 setuid (SUID)

### What it does

When a file has `setuid`, it runs with the **owner's privileges**, not the user's.

---

### Example

```bash id="6ay5sk"
ls -l /usr/bin/passwd
```

Output:

```id="hwhqmt"
-rwsr-xr-x 1 root root ... /usr/bin/passwd
```

👉 `s` instead of `x` means **setuid is enabled**

---

### Why it is needed

The `passwd` command modifies:

```bash id="y47h8n"
/etc/shadow
```

This file belongs to **root**, but users can still change their password.

✔️ Because `passwd` runs with root privileges via SUID

---

### Set SUID

```bash id="zlgf1v"
chmod u+s file
```

---

## 🔵 setgid (SGID)

### On files

Program runs with **group privileges**

---

### On directories

All new files inherit the **directory’s group**

---

### Example

```bash id="ib6f1k"
chmod g+s dir
```

```bash id="3r9rwh"
ls -ld dir
```

Output:

```id="6k4qtd"
drwxrwsr-x
```

👉 Files created inside will keep the same group

---

## 🟢 Sticky bit

### What it does

Used on shared directories.

Example:

```bash id="z2o6ie"
ls -ld /tmp
```

```id="z7on64"
drwxrwxrwt
```

---

### Behavior

* Everyone can create files
* Only file owner can delete their files

---

### Set sticky bit

```bash id="0dxqzy"
chmod +t dir
```

---

## 🔢 Numeric representation

Special permissions use an extra digit:

| Value | Meaning |
| ----- | ------- |
| 4     | setuid  |
| 2     | setgid  |
| 1     | sticky  |

Example:

```bash id="93hhai"
chmod 4755 file
```

* 4 → setuid
* 7 → owner (rwx)
* 5 → group (r-x)
* 5 → others (r-x)

---

## ⚠️ Security considerations

* SUID can be dangerous if misused
* Never set SUID on untrusted scripts
* Always check permissions on critical binaries

---

## 🚨 Real-world examples

### passwd works without root login

```bash id="u4rbb4"
passwd
```

✔️ Uses SUID to update `/etc/shadow`

---

### Shared directory (/tmp)

```bash id="y7cblx"
ls -ld /tmp
```

✔️ Sticky bit prevents users from deleting not his files

---

### Team collaboration directory

```bash id="d8cd0a"
chmod g+s project/
```

✔️ All files inherit the same group

---

## 🧠 Important concept

Special permissions allow:

* controlled privilege escalation
* secure multi-user environments
* safe shared directories

---

## ✅ Summary

| Permission | Effect                       |
| ---------- | ---------------------------- |
| setuid     | run as file owner            |
| setgid     | run as group / inherit group |
| sticky     | protect files in shared dirs |

---
