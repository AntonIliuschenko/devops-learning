# 📄 Day 12 — Firewall (UFW)

## 🧠 Overview

A firewall controls incoming and outgoing network traffic based on defined rules.

In Linux, a common tool is **UFW (Uncomplicated Firewall)**.

---

## 🔍 Check Firewall Status

```bash
sudo ufw status verbose
```

Example:

```text
Status: active
Default: deny (incoming), allow (outgoing)
```

---

## ⚙️ Default Policy

* **deny incoming** — block all incoming connections
* **allow outgoing** — allow all outgoing traffic

👉 This is a secure default configuration.

---

## 🚀 Enable Firewall

```bash
sudo ufw enable
```

---

## 🔓 Allow Ports

Allow SSH:

```bash
sudo ufw allow 22/tcp
```

Allow HTTPS:

```bash
sudo ufw allow 443/tcp
```

Allow HTTP:

```bash
sudo ufw allow 80/tcp
```

---

## 📊 Check Rules

```bash
sudo ufw status
```

---

## 🧱 Common Ports

* **22** — SSH
* **80** — HTTP
* **443** — HTTPS

---

## ⚠️ Important Concept

👉 Only required ports should be open.

Everything else should be **blocked by default**.

---

## 🚨 Common Mistakes

* enabling firewall without allowing SSH → lock yourself out
* opening too many ports → security risk
* forgetting to check rules

---

## 🛠️ Troubleshooting Workflow

```bash
sudo ufw status          # check active rules
ss -tulnp                # check listening ports
curl localhost:80        # test local service
```

---

## 🧪 Real-world Usage

Used to:

* secure servers
* restrict access
* allow only required services

---

## 📊 Example Scenario

```text
Problem:
service is running but not accessible

Check:
ss -tulnp → port is listening
ufw status → port is blocked

Solution:
sudo ufw allow <port>
```

---

## 💡 Key Takeaway

Firewall is the first line of defense.
Only open ports that are absolutely necessary.

---

## 📝 Notes

* Always allow SSH before enabling UFW
* Verify rules after changes
* Combine firewall + service configuration for security
