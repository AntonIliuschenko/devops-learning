# 📄 Day 16 — systemd Lifecycle

## 🧠 Overview

`systemd` is the service manager in modern Linux systems.

It is responsible for:

* starting services
* stopping services
* restarting services
* managing the service lifecycle

---

## ⚙️ Unit File Structure

Example:

```ini id="2czbcm"
[Unit]
Description=My Service

[Service]
ExecStart=/usr/bin/my-app

[Install]
WantedBy=multi-user.target
```

---

## 🔄 Service Lifecycle

When a service starts:

```text id="k5ccx1"
ExecStartPre (optional)
↓
ExecStart
↓
Service is running
↓
ExecStop (on stop)
```

---

## 🔁 Restart Policies

```ini id="kq0j4m"
Restart=always
Restart=on-failure
Restart=no
```

---

### 📊 Behavior

* **on-failure** → restart on crash or error
* **always** → always restart (even after manual stop)
* **no** → do not restart

---

## ⏱️ Restart Delay

```ini id="v7yd9z"
RestartSec=5
```

Wait time before restarting the service.

---

## 🔢 Exit Codes

* **0** → success
* **non-zero** → failure

👉 systemd uses exit codes to decide whether to restart a service.

---

## 🔍 Check Service Status

```bash id="mub6ov"
systemctl status nginx
```

---

## 📜 View Logs

```bash id="k4l4wa"
journalctl -u nginx
```

---

## ⚠️ Important Concept

👉 systemd continuously monitors services
and can automatically restart them if needed.

---

## 🚨 Common Issues

* service crashes → auto restart loop
* incorrect config → service cannot start
* restart policy misconfigured

---

## 🛠️ Troubleshooting Workflow

```bash id="x1d8zt"
systemctl status service_name
journalctl -u service_name
systemctl restart service_name
```

---

## 📊 Example Scenario

```text id="yq9j3h"
Problem:
service keeps restarting

Check:
journalctl logs → config error

Conclusion:
bad configuration causes crash

Solution:
fix config → restart service
```

---

## 💡 Key Takeaway

systemd manages the full lifecycle of services
and ensures they stay running based on defined policies.

---

## 📝 Notes

* `Restart=always` can cause restart loops (flapping)
* logs are critical for debugging
* systemd is the backbone of modern Linux service management
