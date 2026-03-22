# 📄 Day 11 — DNS and Resolvers

## 🧠 Overview

DNS (Domain Name System) translates domain names into IP addresses.

Example:

```text
google.com → 142.250.x.x
```

Without DNS, most network services would not work.

---

## 🔍 How to Check DNS

```bash
resolvectl status
```

---

### 📄 Configuration File

```bash
/etc/resolv.conf
```

Often contains:

```text
nameserver 127.0.0.53
```

---

## 🧩 What is a Stub Resolver

A **stub resolver** is a local DNS resolver running on the system.

In modern Linux systems:

* handled by `systemd-resolved`
* listens on:

```text
127.0.0.53
```

---

## ⚙️ How DNS Resolution Works

```text
Application
   ↓
Stub resolver (127.0.0.53)
   ↓
DNS server (e.g. 8.8.8.8)
   ↓
Response (IP address)
```

---

## 🧪 Testing DNS

### Basic test

```bash
ping google.com
```

---

### More precise tools

```bash
nslookup google.com
dig google.com
```

---

## ⚠️ Important Concept

DNS is a **critical dependency**.

If DNS fails:

* package installation fails
* APIs stop working
* services cannot connect to each other

---

## 🚨 Common Issues

* wrong DNS server in `/etc/resolv.conf`
* `systemd-resolved` not running
* network misconfiguration
* firewall blocking DNS

---

## 🛠️ Troubleshooting Workflow

```bash
resolvectl status       # check DNS configuration
ping google.com         # test name resolution
ping 8.8.8.8            # test network connectivity
nslookup google.com     # verify DNS server response
```

---

## 📊 Example Debug Scenario

```text
Problem:
server cannot resolve domains

Check:
ping google.com → fails
ping 8.8.8.8 → works

Conclusion:
network is OK, DNS is broken
```

---

## 💡 Key Takeaway

If a system cannot resolve domain names,
many services will stop working — even if the network is fine.

---

## 📝 Notes

* `127.0.0.53` is not an external DNS server — it's local
* Always test both:

  * IP connectivity
  * DNS resolution
