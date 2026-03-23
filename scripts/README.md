# 🧪 My Practice Scripts

This section contains simple Bash scripts created for learning and practice.

---

## 📄 isdockeractive.sh

Checks if Docker service is running.

### Script

```bash
#!/usr/bin/env bash

if systemctl is-active --quiet docker; then
  echo "active"
else
  echo "not active"
fi
```

---

## 📄 arguments.sh

Demonstrates how to pass and use arguments in a Bash script.

### Script

```bash
#!/usr/bin/env bash

echo "First argument: $1"
echo "All arguments: $@"
echo "How many arguments: $#"
```

---

### ▶️ Usage

```bash
./arguments.sh user docker git
```

### 📌 Output

```bash
First argument: user
All arguments: user docker git
How many arguments: 3
```

---
## 📄 service_status.sh
Modified isdockeractive.sh, i changed it using arguments. If start ./service_status.sh nginx it will answer accordinly about status using argument.

## 🧠 What I learned

* How to check service status (`systemctl`)
* How to use positional arguments (`$1`, `$@`, `$#`)
* How to write simple automation scripts

---
