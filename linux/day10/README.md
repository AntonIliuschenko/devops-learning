# 📄 Day 10 — lsof and Deleted Files

## 🧠 Overview

`lsof` (List Open Files) is a powerful tool used to inspect open files and file descriptors in Linux.

👉 In Linux, **everything is a file**.

---

## 🔧 Basic Usage

Show all open files:

```bash
lsof
```

---

### Find files opened by a process

```bash
lsof -p PID
```

---

### Find deleted but still open files

```bash
lsof | grep deleted
```

---

## ⚠️ Important Concept

A file can be:

* removed from the filesystem
* but still used by a running process

👉 This happens because the process keeps an **open file descriptor**.

---

## ❗ Why It Happens

Typical scenario:

```text
file is deleted (rm)
↓
process is still running
↓
file descriptor remains open
```

---

## 🚨 Problem

Disk space is **not freed**, even though the file is deleted.

This can lead to:

* disk full errors
* system instability
* application failures

---

## 🛠️ Solution

To release disk space:

* restart the process
* or kill the process

```bash
kill PID
```

---

## 🔍 Check Disk Usage

```bash
df -h      # overall disk usage
du -sh *   # directory sizes
```

---

## 🧪 Real-world Usage

Used when:

* disk is full
* but no large files are visible

👉 Often caused by **deleted but still open files**

---

## 🚀 Debug Workflow

```bash
df -h                  # check disk usage
du -sh *               # check directories
lsof | grep deleted    # find hidden disk usage
kill PID               # free space
```

---

## 💡 Key Takeaway

Deleting a file does **not guarantee freeing disk space**
if it is still used by a running process.

---

## 📝 Notes

* This issue is common with log files
* Services like nginx, docker, or java apps often cause it
* Always investigate before killing production processes


## 🔥 Example

A log file was deleted, but disk space was still full.

Reason:
process was still writing to the deleted file

Solution:
restart service → disk space freed
