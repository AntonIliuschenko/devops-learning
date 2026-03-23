# 🚀 Day 23 — Bash deeper (functions, error handling, real scripts)

## 🧠 Functions

Functions allow you to write reusable code.

```bash
log() {
  echo "[INFO] $1"
}

log "Service started"
```

---

### 🔹 Functions with arguments

```bash
check_service() {
  systemctl is-active --quiet "$1"
}
```

Usage:

```bash
check_service nginx
```

---

## 🧠 Exit codes (very important)

In Bash:

* `0` → success
* non-zero → error

Example:

```bash
systemctl is-active nginx
echo $?
```

---

### 🔥 Check command result

```bash
if systemctl is-active --quiet nginx; then
  echo "running"
else
  echo "down"
fi
```

👉 This is the foundation of DevOps logic.

---

## 🧠 set -e (fail fast)

```bash
set -e
```

Script exits immediately if any command fails.

---

## 🧠 set -u

```bash
set -u
```

Treats unset variables as errors.

---

## 🧠 set -x (debug mode)

```bash
set -x
```

Prints each command before execution:

```bash
+ echo hello
```

---

## 🔥 DevOps standard

```bash
set -euo pipefail
```

---

## 🧠 pipefail

```bash
set -o pipefail
```

If any command in a pipeline fails → the whole pipeline fails.

---

## 🧠 Logging

```bash
log() {
  echo "$(date) [INFO] $1"
}
```

---

## 🧠 Error handling

```bash
if ! systemctl restart nginx; then
  echo "Failed to restart nginx"
  exit 1
fi
```

---

## 🧠 Dependency check

```bash
command -v docker >/dev/null || {
  echo "docker not installed"
  exit 1
}
```

---

## 🚀 Real DevOps script

```bash
#!/bin/bash
set -euo pipefail

log() {
  echo "$(date) [INFO] $1"
}

SERVICE="nginx"

if systemctl is-active --quiet "$SERVICE"; then
  log "$SERVICE is running"
else
  log "$SERVICE is down, restarting"
  systemctl restart "$SERVICE"
fi
```

---

## ⚠️ Best practices

* Always use `set -euo pipefail`
* Quote variables: `"$VAR"`
* Use functions for reusable logic
* Check command results
* Add logging

---

## 🧠 Important concept

Good Bash scripts should be:

* predictable
* safe
* readable
* easy to debug

---

## ✅ Summary

| Concept    | Purpose                |
| ---------- | ---------------------- |
| functions  | reuse code             |
| exit codes | detect success/failure |
| set -e     | stop on error          |
| set -u     | catch undefined vars   |
| set -x     | debug                  |
| pipefail   | catch pipeline errors  |
| logging    | visibility             |

---
