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
- ps aux | grep nginx # ps-processes command, a- all processes, u-user friendly(easy to read),
  		      #  x- show processes that do NOT have a controlling terminal (TTY) 
- ps aux --sort=-%cpu # sorted by cpu usage
- ps aux --sort=-%mem # sorted by memory usage

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

