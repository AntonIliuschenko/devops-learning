# 📄 Day 18 — journald and Logs

## 🧠 Overview

`journald` is the logging system used by `systemd`.

It collects logs from:

* kernel
* system services
* applications

---

## 🔍 View Logs

Show all logs:

```bash id="i0g2k2"
journalctl
```

---

### 📦 Logs for a specific service

```bash id="oz3w5o"
journalctl -u nginx
journalctl -u ssh 
journalctl -u docker
```

Last 50 lines:

```bash id="3m3x1m"
journalctl -u ssh -n 50
```

Follow logs in real time:

```bash id="p9u9a2"
journalctl -u nginx -f
```

---

## ⏱️ Logs by Time

```bash id="q5m9t1"
journalctl --since "1 hour ago"
journalctl --since today
journalctl --since yesterday 
journalctl --since "2026-03-23 10:00:00" 
journalctl --until "2026-03-23 12:00:00"
```

---

## 🔄 Logs by Boot

```bash id="b4c7x2"
journalctl -b       # current boot
journalctl -b -1    # previous boot
```

---

## ⚠️ Log Levels

```bash id="z8k1p7"
journalctl -p err
```

#Levels:

* **emerg (0)**
* **alert (1)**
* **crit (2)**
* **err (3)**
* **warning (4)**
* **notice (5)**
* **info (6)**
* **debug (7)**
---

## What do the numbers mean?

Each log level has a numeric priority from 0 to 7:

0 = most critical (system unusable)
7 = least critical (debug information)

👉 Lower number = higher severity

Can numbers be used?

Yes ✅ You can use numbers instead of names:

journalctl -p 3        # same as err
journalctl -p 4        # same as warning



## 💾 Storage

* `/run/log/journal` → temporary (lost after reboot)
* `/var/log/journal` → persistent

---

## 🔧 Enable Persistent Logs

```bash id="q2x8f9"
sudo mkdir -p /var/log/journal
sudo systemctl restart systemd-journald
```

---

## 🛠️ Troubleshooting Workflow

```bash id="n7w2c6"
systemctl status service_name
journalctl -u service_name -n 50
journalctl -u service_name -f
```

---

## 📊 Example Scenario

```text id="r1k8qz"
Problem:
service does not start

Check:
journalctl -u service → shows error

Conclusion:
configuration or dependency issue

Solution:
fix error → restart service
```

---

## ⚠️ Important Concept

👉 `journalctl` is the main tool for debugging services in Linux.

---

## 🧪 Real-world Usage

Used when:

* service fails to start
* application crashes
* system behaves unexpectedly

---

## 🚀 Useful Commands

```bash id="c0z5p1"
journalctl -xe              # detailed recent logs
journalctl -u nginx -f      # live logs
journalctl --since today    # today's logs
```

---

## 💡 Key Takeaway

Logs are the **first place to look** when debugging issues.

---

## 📝 Notes

* always check logs before guessing
* persistent logs are important for debugging after reboot
* combine `journalctl` with `systemctl status` for full picture
