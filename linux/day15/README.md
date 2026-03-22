# 📄 Day 15 — fork, exec, and Zombie Processes

## 🧠 Overview

Linux processes are created and managed using two key mechanisms:

* `fork()` — creates a new process
* `exec()` — replaces process code

Understanding these is essential for debugging process-related issues.

---

## 🔀 fork()

`fork()` creates a copy of the current process.

```text id="g2z4oz"
parent process
      ↓
   fork()
      ↓
child process (same code, new PID)
```

* child gets a new PID
* initially identical to parent

---

## 🔄 exec()

`exec()` replaces the process code with a new program.

```text id="m3gk1c"
existing process
      ↓
   exec()
      ↓
new program (same PID)
```

👉 PID stays the same, but the program changes.

---

## ⚙️ fork + exec Model

Typical process creation:

```text id="1jpjcl"
fork → create child
exec → run new program
```

Used by:

* shells
* system services
* almost all applications

---

## 🧟 Zombie Processes

A zombie process is a process that:

* has finished execution
* but still exists in the process table

---

### 📊 State

```text id="z5b6rl"
Z — zombie
```

---

## ❗ Why Zombies Appear

```text id="x6m9ke"
child process exits
↓
parent does not call wait()
↓
zombie remains
```

The parent must read the exit status.

---

## 🚨 Why It Is a Problem

* fills process table
* can lead to system instability
* indicates broken process management

---

## 🛠️ Fix

* restart parent process
* or kill parent process

```bash id="5pq9pr"
kill <parent_PID>
```

---

## 🧩 Role of PID 1

PID 1 (`init` or `systemd`) is responsible for:

* adopting orphan processes
* cleaning up zombies

```text id="plg5ry"
orphan → adopted by PID 1 → cleaned
```

---

## ⚠️ Important Concept

👉 PID 1 is critical for system stability.

If it fails:

* processes are not cleaned properly
* system becomes unstable

---

## 🧪 Real-world Usage

Used when:

* many zombie processes appear
* services behave incorrectly
* issues inside containers

---

## 🚀 Debug Workflow

```bash id="h7qk3l"
ps aux | grep Z         # find zombie processes
ps -o ppid= -p PID     # find parent process
kill <parent_PID>      # fix issue
```

---

## 📊 Example Scenario

```text id="7c9zwr"
Problem:
many zombie processes

Check:
ps aux → Z state processes

Conclusion:
parent process is not handling children correctly

Solution:
restart or kill parent process
```

---

## 💡 Key Takeaway

Zombie processes are not running,
but they indicate a problem in process management.

---

## 📝 Notes

* zombies do not consume CPU, but occupy process table
* common in poorly written programs
* frequent in container environments with bad init handling
