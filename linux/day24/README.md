# 📄 Day 24 — Network Debugging

## 🧠 Overview

Most issues in DevOps are network-related.

When something “does not work”, always think:

* is it DNS?
* is it network connectivity?
* is it a port issue?
* is the service running?
* is it blocked by firewall?

---

## 🔍 Basic Tools

### 📡 Ping (check connectivity)

```bash
ping google.com
```

Checks:

* DNS resolution
* network reachability

---

### 🌐 Curl (HTTP client)

```bash
curl http://example.com
curl -I http://example.com
curl -v http://example.com
```

#### Flags:

* `-I` → show only headers (HEAD request)
* `-v` → verbose mode (shows full request/response details)

Used to test:

* HTTP/HTTPS connectivity
* API endpoints
* service availability

---

### 🔌 Ports (listening services)

```bash
ss -tuln
ss -tulnp
```

#### Flags:

* `-t` → TCP sockets
* `-u` → UDP sockets
* `-l` → listening ports
* `-n` → numeric output (no DNS resolution)
* `-p` → show process using the port

---

### 🌍 DNS

```bash
dig google.com
dig +short google.com
```

#### Flags:

* `+short` → show only IP address (clean output)

Used to check:

* domain resolution
* DNS server response

---

### 🧭 Route (path to host)

```bash
traceroute google.com
```

Shows:

* network path
* where packets are dropped

---

### 🔎 Check Port

```bash
nc -zv localhost 443
```

#### Flags:

* `-z` → scan mode (no data transfer)
* `-v` → verbose

Used to check:

* if port is open
* if service is reachable

---

## 🛠️ Debug Workflow

```text
1. Check DNS
2. Check network connectivity
3. Check port
4. Check service
5. Check firewall
```

---

## 📊 Example Analysis

### Command:

```bash
curl -v https://google.com
```

Breakdown:

* DNS → resolves domain to IP
* TCP → establishes connection (3-way handshake)
* TLS → HTTPS handshake
* HTTP → request/response

---

## 🧠 Layer Understanding

When debugging:

* **DNS** → `dig`, `ping`
* **TCP** → `ss`, `nc`
* **HTTP** → `curl`

---

## 💡 Important Concept

👉 Always isolate the problem layer:

```text
DNS → TCP → HTTP → Application
```

---

## 🧪 Practice

```bash
curl -v https://google.com
ss -tulnp
dig google.com
```

Try to identify:

* where DNS happens
* where TCP connection is created
* where HTTP request is processed

---

## 🚀 Real-world Usage

Used when:

* service is not reachable
* API calls fail
* connection timeouts occur
* network issues appear

---

## 💡 Key Takeaway

Network debugging = checking layers step by step.

---

## 📝 Notes

* always test from simple to complex
* do not guess — verify each layer
* most issues are solved by isolating the failing component
