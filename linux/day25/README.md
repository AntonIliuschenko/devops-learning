# 📄 Day 25 — Real-world Debugging Scenarios

## 🧠 Overview

In DevOps, problems are rarely about commands —
they are about **systematic thinking**.

When someone says:

```text
"the service is not working"
```

👉 You follow a structured approach:

```text
DNS → Network → Port → Service → Logs
```

---

## 🔥 Scenario 1 — Website Not Opening

### ❓ Problem

```text
https://my-site.com is not accessible
```

---

### ✅ Step 1 — DNS

```bash
dig +short my-site.com
```

* ❌ no IP → DNS issue
* ✔ IP exists → continue

---

### ✅ Step 2 — Network

```bash
ping my-site.com
```

* ❌ no response → network / firewall issue
* ✔ response OK → continue

---

### ✅ Step 3 — HTTP

```bash
curl -v https://my-site.com
```

Common results:

* `connection refused` → port closed
* `timeout` → network / firewall issue
* `500` → application error

---

### ✅ Step 4 — Port

```bash
ss -tulnp | grep 443
```

* ❌ no output → service is not listening
* ✔ port exists → continue

---

### ✅ Step 5 — Service

```bash
systemctl status nginx
```

---

### ✅ Step 6 — Logs

```bash
journalctl -u nginx -n 50
```

---

## 🔥 Scenario 2 — Port Is Open, but Not Working

### ❓ Problem

Port `8080` is open, but no response.

---

### ✅ Check Port

```bash
ss -tulnp | grep 8080
```

✔ port exists

---

### ✅ Test Locally

```bash
curl localhost:8080
```

❌ no response

---

### 🔍 Possible Causes

* application is stuck
* listening only on `127.0.0.1`
* firewall blocking access

---

### ✅ Check Binding

```bash
curl 127.0.0.1:8080
```

✔ works → problem is network / binding

---

## 🔥 Scenario 3 — DNS Works, but Service Fails

```bash
dig google.com
```

✔ DNS works

```bash
curl google.com
```

❌ fails

---

### 🔍 Possible Causes

* firewall
* proxy
* routing issues

---

## 🔥 Scenario 4 — Service Keeps Failing

```bash
systemctl status nginx
```

Shows:

```text
failed
```

---

### ✅ Check Logs

```bash
journalctl -u nginx -n 50
```

---

### 🔍 Common Causes

* configuration error
* port already in use
* permission issues

---

## 🔥 Scenario 5 — Everything Works, but Is Slow

### ✅ Check System Load

```bash
top
```

Look at:

* CPU
* memory
* load average

---

### ✅ Check Network Path

```bash
traceroute google.com
```

---

### ✅ Measure Response Time

```bash
curl -w "%{time_total}\n" -o /dev/null -s http://site
```

---

## 🧠 Core DevOps Algorithm

Always follow this order:

```text
1. DNS
2. Network
3. Port
4. Service
5. Logs
```

---

## 💡 Key Takeaways

* Do not guess — verify each layer
* Always isolate the problem
* Most issues are network-related
* Logs are your best debugging tool

---

## 📝 Notes

* Start simple → go deeper
* Check from outside → then inside
* One problem = one root cause
