# 📄 Day 21 — system resources, ulimit, OOM

## What are system resources

Every process in Linux uses system resources:

* CPU
* memory (RAM)
* file descriptors
* processes/threads

These resources are **limited**, so the system must control usage.

---

## ⚙️ What is ulimit

`ulimit` controls **resource limits per process**.

Check current limits:

```bash id="xqg9l2"
ulimit -a
```

---

## 📊 Common limits

| Option | Description                       |
| ------ | --------------------------------- |
| `-n`   | max open files (file descriptors) |
| `-u`   | max user processes                |
| `-f`   | max file size                     |
| `-t`   | max CPU time                      |
| `-v`   | max virtual memory                |

---

## 🔧 Set limits

```bash id="y0zjlwm"
ulimit -n 4096
```

👉 Sets max open files to 4096

⚠️ Important:

* Works only for current shell session
* Resets after logout

---

## 📁 Persistent limits

To make limits permanent:

File:

```bash id="p7g32c"
/etc/security/limits.conf
```

Example:

```id="5evp5p"
* soft nofile 4096
* hard nofile 8192
```

---

## 🧠 Why it matters

Each process uses:

* file descriptors (files, sockets)
* memory
* CPU time

👉 If limits are too low → application will fail

---

## 🚨 Too many open files

### Error

```id="k8l9ch"
Too many open files
```

---

### What it means

Process exceeded limit of open file descriptors.

---

### Check open files

```bash id="x0h6e6"
lsof
```

For a process:

```bash id="0l6i6p"
lsof -p <PID>
```

Count open files:

```bash id="g0s0tq"
lsof | wc -l
```

---

### Fix

```bash id="y0ryz6"
ulimit -n 65535
```

Or update system limits.

---

## 🧠 What is OOM (Out Of Memory)

When system runs out of RAM:

👉 Linux activates **OOM killer**

---

## ⚡ OOM killer behavior

* selects a process
* kills it
* frees memory

---

## 🔍 Check memory usage

```bash id="lqfxiy"
free -h
```

```bash id="i7u0yd"
top
```

---

## 📊 Example output

```id="3j9b0m"
Mem:  8Gi total, 7.5Gi used, 200Mi free
```

👉 System is close to OOM

---

## 🧠 How OOM chooses process

Based on:

* memory usage
* process priority
* `oom_score`

Check:

```bash id="czd6t7"
cat /proc/<PID>/oom_score
```

---

## 🚨 Real-world scenarios

### 1. Service crashes under load

Cause:

* too many connections
* not enough file descriptors

Fix:

```bash id="c9yff2"
ulimit -n 65535
```

---

### 2. Memory exhaustion

Symptoms:

* slow system
* processes killed
* logs show OOM

Check:

```bash id="sx5l8p"
dmesg | grep -i oom
```

---

### 3. High number of connections (nginx, apps)

Each connection = file descriptor

👉 Must increase `nofile`

---

## ⚠️ Important concepts

* System resources are limited
* Limits protect system from crashes
* Misconfiguration → downtime

---

## 🧠 Best practices

* Monitor memory and file descriptors
* Set proper limits for services
* Test under load
* Use alerts (CPU, RAM, FD usage)

---

## ✅ Summary

| Resource   | Tool             |
| ---------- | ---------------- |
| Limits     | `ulimit`         |
| Memory     | `free -h`, `top` |
| Open files | `lsof`           |
| OOM logs   | `dmesg`          |

---
