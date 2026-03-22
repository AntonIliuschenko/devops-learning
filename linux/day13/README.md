# 📄 Day 13 — NAT and Forwarding

## 🧠 Overview

NAT and forwarding are key concepts in Linux networking, especially when working with:

* Docker containers
* virtual machines
* VPNs

---

## 🔀 What is FORWARD

FORWARD is a chain in `iptables` that handles:

👉 traffic passing **through the host**, not to/from the host itself

---

### 📊 Examples

* Docker containers
* VPN clients
* virtual machines

```text
container → host → internet
```

---

## 🌐 What is NAT

NAT (Network Address Translation) modifies network packets, usually:

👉 changes the **source IP address**

---

### 📊 Example

```text
container (172.x.x.x)
   ↓
host (public IP)
   ↓
internet
```

---

## ❓ Why NAT is Needed

Private IP addresses:

```text
10.x.x.x
172.16.x.x
192.168.x.x
```

👉 cannot access the internet directly

NAT allows them to:

```text
appear as the host IP
```

---

## 🐳 Docker Behavior

Docker automatically:

* adds `iptables` rules
* enables IP forwarding
* creates NAT rules

This allows containers to:

```text
access the internet
```

without manual configuration.

---

## ⚠️ Important Concept

👉 UFW does **not fully control Docker traffic**

Reason:

* Docker modifies `iptables` directly
* bypasses some UFW rules

---

## 🔍 Check Network Rules

```bash id="0q1n7q"
iptables -L -v -n
```

Check NAT table:

```bash id="l3q7y5"
iptables -t nat -L -v -n
```

---

## 🛠️ Troubleshooting Workflow

```bash id="n3rzm2"
iptables -L -v -n           # check filter rules
iptables -t nat -L -v -n   # check NAT rules
ip a                        # check interfaces
```

---

## 🚨 Common Issues

* container cannot access internet
* service port is open but not reachable
* forwarding disabled
* incorrect NAT rules

---

## 📊 Example Debug Scenario

```text
Problem:
container has no internet access

Check:
iptables NAT rules → missing
IP forwarding → disabled

Solution:
enable forwarding
fix NAT rules
```

---

## 💡 Key Takeaway

* FORWARD = traffic through the host
* NAT = allows private networks to access the internet
* Docker manages networking automatically, but may bypass firewall rules

---

## 📝 Notes

* Always check both:

  * filter rules (`iptables -L`)
  * NAT rules (`iptables -t nat -L`)
* Docker networking can conflict with firewall configuration
