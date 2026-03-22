# Day 6 — Processes

## What is a process

A process is a running program in the system.

Each process has:
- PID (process ID)
- user (owner)
- state
- resources (CPU, memory)

## View processes

```bash
ps aux
top
htop
```

# Find process
- ps aux | grep nginx

## Important fields in ps
- PID — process ID
- USER — owner
- %CPU — CPU usage
- %MEM — memory usage

# Important concept

- Each process runs as a user.

- This is the basis of Linux security.

# Real case
Used to check:

- what is running
- who consumes CPU
- which service is broken
