# 📄 Day 17 — systemd Timers

## 🧠 Overview

A **systemd timer** is a scheduler used to run tasks at specific times.

👉 It is a modern alternative to `cron`.

---

## ⚙️ Core Concept

```text
timer → service → command
```

👉 Timer does **not run commands directly** — it triggers a service.

---

## 🔧 Example Timer Unit

```ini id="zjv8ye"
[Unit]
Description=Run backup

[Timer]
OnCalendar=hourly
Persistent=true

[Install]
WantedBy=timers.target
```

---

## 🔧 Example Service Unit

```ini id="0g7v3u"
[Service]
Type=oneshot
ExecStart=/usr/local/bin/backup.sh
```

---

## ⏰ OnCalendar Formats

Examples:

* `hourly`
* `daily`
* `*:0/5` → every 5 minutes
* `Mon *-*-* 03:00:00` → every Monday at 03:00

---

## 🔁 Persistent Timers

```ini id="2yq5m3"
Persistent=true
```

👉 If the system was off, the job runs after boot.

---

## 🧪 Timer Types

### `Type=oneshot`

* runs once
* exits after execution

Used for:

* backups
* cleanup scripts
* maintenance jobs

---

## 🛠️ Managing Timers

List timers:

```bash id="xw8g7n"
systemctl list-timers
```

Start timer:

```bash id="h0bqrs"
systemctl start backup.timer
```

Enable on boot:

```bash id="7y2qk0"
systemctl enable backup.timer
```

Check status:

```bash id="3bkl0u"
systemctl status backup.timer
```

---

## 🔍 Logs

```bash id="cb2p6b"
journalctl -u backup.service
```

👉 Always check logs of the **service**, not the timer.

---

## ⚠️ Important Concept

👉 Timer triggers a **service**, not
