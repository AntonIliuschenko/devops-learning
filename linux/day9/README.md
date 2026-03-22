# 📄 Day 9 — System Load

## 🧠 Overview

System load shows how busy the system is and helps identify performance issues.

---

## 📊 Load Average

Check load average:

```bash
uptime
top
```

Example:

```
load average: 0.26, 0.30, 0.40
```

---

## 🔍 What It Means

Three values represent system load over time:

* **1 minute**
* **5 minutes**
* **15 minutes**

Load ≈ number of processes waiting for CPU

---

## ⚖️ Interpretation

To understand load correctly:

👉 Always compare it with the number of CPU cores

### Example

* 1 CPU core → load 1.0 = fully utilized
* 4 CPU cores → load 4.0 = fully utilized

---

## 🧪 CPU States (from `top`)

* **us** — user CPU usage
* **sy** — system CPU usage
* **id** — idle CPU
* **wa** — waiting for I/O

---

## 📈 Example Analysis

```
id = 95%
wa = 0%
```

👉 System is mostly idle

---

## ⚠️ Important Concept

High load does **not always mean a problem**.

It may be normal if:

* the system has many CPU cores
* processes are short-lived
* workload is expected

---

## 🧪 Real-world Usage

Used to:

* detect system overload
* analyze performance issues
* understand CPU bottlenecks

---

## 🚀 Quick Debug Workflow

```bash
uptime        # check load average
top           # analyze CPU usage
htop          # detailed view
```

---

## 💡 Key Takeaway

System load must always be interpreted **in context of CPU cores and system activity**.
## 📝 Notes

- high load with high `wa` → possible disk I/O problem
- high load with low CPU usage → processes may be blocked
