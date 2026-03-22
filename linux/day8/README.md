# 📄 Day 8 — Process Monitoring

## 🧠 Overview

Process monitoring is essential for understanding system performance and troubleshooting issues in Linux.

---

## 📊 Real-time Monitoring

### `top`

Displays real-time system information:

* CPU usage
* Memory usage
* Running processes

```bash
top
```

---

### `htop`

Improved version of `top` with a better interface:

* Easier navigation
* Colored output
* Process management

```bash
htop
```

---

## 🔍 Key Metrics to Watch

* CPU usage
* Memory usage
* Load average
* Number of running processes

---

## 🛑 Managing Processes

### Kill a process

```bash
kill PID
```

### Force kill a process

```bash
kill -9 PID
```

---

## ⚠️ Signals

* **SIGTERM (15)** — graceful stop (default)
* **SIGKILL (9)** — force stop (cannot be ignored)

👉 Always try **SIGTERM first**, then use SIGKILL if needed.

---

## 🔎 Inspecting a Process

```bash
ps -p PID -f
```

Shows detailed information about a specific process.

---

## 🧪 Real-world Usage

Used when:

* a process hangs
* a service consumes too much CPU
* debugging performance issues

---

## 💡 Key Takeaway

Always prefer a **graceful shutdown (SIGTERM)** before using a **force kill (SIGKILL)**.

---

## 🚀 Example Workflow

```bash
top            # find problematic process
ps -p PID -f   # inspect process
kill PID       # try graceful stop
kill -9 PID    # force kill if needed
```
## 📝 Notes

- `kill -9` should be used only as a last resort
- always investigate the root cause of high CPU usage
