# 📄 Day 14 — Signals and Process Control

## 🧠 Overview

A signal is a message sent to a process to control its behavior.

Signals are used to:

* stop processes
* restart services
* reload configuration

---

## 🔔 What is a Signal

A signal is an asynchronous notification sent to a process.

```text id="2zdl2n"
process → receives signal → reacts
```

---

## ⚙️ Common Signals

* **SIGTERM (15)** — graceful stop
* **SIGKILL (9)** — force stop (cannot be caught)
* **SIGHUP (1)** — reload configuration

---

## 🛠️ Sending Signals

### Default (SIGTERM)

```bash id="b1pdri"
kill PID
```

---

### Force kill

```bash id="3a3sqf"
kill -9 PID
```

---

### Reload configuration

```bash id="fw4v6y"
kill -HUP PID
```

---

## ⚙️ systemd Behavior

When using:

```bash id="f9k6op"
systemctl stop service
```

systemd:

1. sends **SIGTERM**
2. waits for the process to stop
3. sends **SIGKILL** if needed

---

## ⚠️ Important Concept

👉 **SIGKILL cannot be caught or ignored**

The process is terminated immediately.

---

## 🚨 Why Avoid `kill -9`

Using SIGKILL may cause:

* no cleanup
* data loss
* incomplete logs
* corrupted state

---

## 🧪 Real-world Usage

Used when:

* process is stuck
* service does not respond
* restart issues occur

---

## 🚀 Debug Workflow

```bash id="c9c9lj"
ps aux | grep process     # find process
kill PID                  # try graceful stop
kill -9 PID               # force kil
```
