# 📄 Day 22 — Bash scripting

## What is a bash script

A bash script is a file containing commands that are executed sequentially by the shell.

Used for:

* automation
* system administration
* deployment scripts

---

## ⚙️ Shebang

Defines which interpreter to use:

```bash
#!/bin/bash
```

---

## 🚀 Make script executable

```bash
chmod +x script.sh
./script.sh
```

---

## 🔤 Variables

```bash
name="Anton"
echo $name
```

---

## 📥 User input

```bash
read -p "Enter name: " name
echo "Hello $name"
```

---

## 📦 Arguments

```bash
echo $1
echo $2
```

Example:

```bash
./script.sh Anton DevOps
```

---

## 🔀 Conditions

```bash
if [ "$name" = "Anton" ]; then
  echo "Hello Anton"
fi
```

---

### With else

```bash
if [ "$name" = "Anton" ]; then
  echo "Hello Anton"
else
  echo "Unknown user"
fi
```

---

## 🔁 Loops

### For loop

```bash
for i in 1 2 3
do
  echo $i
done
```

---

### While loop

```bash
i=1
while [ $i -le 3 ]
do
  echo $i
  ((i++))
done
```

---

## ❗ Exit code

```bash
echo $?
```

* `0` → success
* non-zero → error

---

## ⚡ Command check example

```bash
if systemctl is-active --quiet nginx; then
  echo "nginx is running"
else
  echo "nginx is NOT running"
fi
```

---

## 🧠 Important concepts

* Bash is used for automation in DevOps
* Scripts should be simple and readable
* Always check exit codes
* Use scripts to reduce manual work

---

## 🚨 Best practices

* Use meaningful variable names
* Add comments
* Handle errors
* Test scripts before production use

---

# 🧪 Task — check-nginx.sh

Create a script:

```bash
check-nginx.sh
```

---

## Requirements

The script should:

* check if nginx is running
* print status message

---

## 💡 Example solution

```bash
#!/bin/bash

if systemctl is-active --quiet nginx; then
  echo "✅ nginx is running"
else
  echo "❌ nginx is NOT running"
fi
```

---

## 🔧 Make it executable

```bash
chmod +x check-nginx.sh
```

Run:

```bash
./check-nginx.sh
```

---

## 🚀 Bonus (recommended)

Improve script:

```bash
#!/bin/bash

SERVICE="nginx"

if systemctl is-active --quiet $SERVICE; then
  echo "✅ $SERVICE is running"
else
  echo "❌ $SERVICE is NOT running"
fi
```

---

## 📤 Upload to GitHub

```bash
git add check-nginx.sh
git commit -m "Add nginx check script"
git push
```

---

## 🧠 Real DevOps usage

This script can be used in:

* monitoring
* cron jobs
* CI/CD pipelines
* health checks

---
