# 🧠 42 Born2beRoot — Secure Linux Configuration Guide

This guide documents the **initial setup and hardening** of a Debian-based system for the **42 School project environment**.  
It covers everything from user creation to SSH, password policies, and firewall configuration — all built for stability, security, and compliance.

---


## ⚙️ 1. Initial Machine Setup and Basic APT
  
  **Update and upgrade system**
  
   ```bash
   apt update && apt upgrade
   apt install sudo vim net-tools
   ```

  **Verify system information**

```bash
uname -a
lsblk
aa-status
```

---
💡 You may use aptitude for better dependency management.


## 🖥️ 2. Hostname Configuration

**Edit hostname**
```bash
vim /etc/hostname
vim /etc/hosts
```

**Apply and verify**
```bash
hostnamectl set-hostname wil42
hostname
```

🌀 May need to change during evaluation.


---


## 👥 3. Groups and User Setup
``
Create group:
```bash
groupadd user42
```
Create user:
```bash
adduser wil
```
Add user to groups:
```bash
usermod -aG sudo,user42 wil
```

Verify:
```bash
groups wil
```

✅ During defense, be ready to create a new user/group dynamically.


---


## 🔐 4. Password Policy Configuration

Install PAM quality module:
```bash
apt install libpam-pwquality
```
Edit /etc/pam.d/common-password and add:
```bash
password requisite pam_pwquality.so retry=3 minlen=10 ucredit=-1 lcredit=-1 dcredit=-1 maxrepeat=3 usercheck=1 difok=7 enforce_for_root
```
Edit /etc/login.defs:
```bash
PASS_MAX_DAYS   30
PASS_MIN_DAYS   2
PASS_WARN_AGE   7
```
Update passwords:
```bash
passwd root
passwd wil
```
Verify password expiry:
```bash
chage -l wil
```


## ⚡ 5. Sudo (Visudo) Configuration

Create sudoers file:
```bash
visudo -f /etc/sudoers.d/custom
```
Add configuration:
```bash
Defaults passwd_tries=3
Defaults badpass_message="Wrong password! Try again."
Defaults logfile="/var/log/sudo/sudo.log"
Defaults log_input, log_output
Defaults requiretty
Defaults secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
```
Create log directory:
```bash
mkdir -p /var/log/sudo
```
Verify:
```bash
sudo -l
```

## 🔑 6. SSH Setup

Install SSH server:
```bash
apt install openssh-server
```
Edit SSH configuration:
```bash
vim /etc/ssh/sshd_config
```
Set:
```bash
Port 4242
PermitRootLogin no
```
Restart SSH:
```bash
systemctl restart ssh
```
Verify:
```bash
ss -tuln | grep 4242
```

## 🧱 7. Firewall Setup

Install UFW:
```bash
apt install ufw
```
Configure firewall:
```bash
ufw allow 4242
ufw enable
ufw default deny incoming
```
Verify:
```bash
ufw status verbose
```

---


## 📘 Notes

    💡 Keep everything documented and reproducible for your 42 evaluation.

    🔒 Security and consistency are key — verify every change manually.

    🧰 Optional: automate setup using a Bash script for faster rebuilds.
