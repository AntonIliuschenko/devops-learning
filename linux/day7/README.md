
# 📄 Day 7 — systemd basics

```markdown
# Day 7 — systemd basics

## What is systemd

systemd is the init system and service manager in Linux.

It:
- starts services
- manages processes
- handles boot process

## Manage services

```bash
systemctl start nginx
systemctl stop nginx
systemctl restart nginx
systemctl status nginx

# Enable/disable service
systemctl enable nginx # autostart on boot
systemctl disable nginx # no autostart on boot

# Service status
## How to check process running or not?
systemctl status ssh

Shows:

active/inactive
logs
errors
Important concept

systemd controls services and their lifecycle.

Real case

Used to:

start web servers
restart failed services
check service errors
