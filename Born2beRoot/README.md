# Debian Secure Setup Guide

This guide configures a **minimal, secure Debian system** (no GUI/X.org) with hardened settings for SSH, sudo, password policy, firewall, and AppArmor. Ideal for **42 School projects**, security evaluations, or production-like minimal servers.

> **Hostname format**: `<yourlogin>42` (e.g., `wil42`)  
> **SSH port**: `4242`  
> **Root login**: Disabled  
> **Firewall**: UFW (only port 4242 open)

---

## 1. Initial Machine Setup and Basic APT

Boot into terminal (no X.org installed).

``bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y sudo vim net-tools


## 1. Initial Machine Setup and Basic APT

Boot into terminal (no X.org installed).
Update system: apt update && apt upgrade.
Install essentials: apt install sudo vim net-tools (use aptitude if preferred for better dependency handling).
Verify OS: uname -a (check Debian stable, kernel).
Check partitions: lsblk (confirm LVM encrypted setup, e.g., /boot, /root, /home; adjust sizes for efficiency).
Enable AppArmor: aa-status (ensure active; reboot if needed).

## 2. Hostname Configuration

Edit /etc/hostname: Set to <yourlogin>42 (e.g., wil42).
Edit /etc/hosts: Add 127.0.0.1 <yourlogin>42.
Apply: hostnamectl set-hostname <yourlogin>42 or reboot.
Verify: hostname (prepare to change during evaluation).

## 3. Groups and User Setup

Create group: groupadd user42.
Create user: adduser <yourlogin> (e.g., wil).
Add to groups: usermod -aG sudo,user42 <yourlogin>.
Verify: groups <yourlogin> (should show sudo and user42; prepare to create new user/group in defense).

## 4. Password Policy Configuration

Install: apt install libpam-pwquality.
Edit /etc/pam.d/common-password:

Add password requisite pam_pwquality.so retry=3 minlen=10 ucredit=-1 lcredit=-1 dcredit=-1 maxrepeat=3 usercheck=1 difok=7 enforce_for_root.


Edit /etc/login.defs:

Set PASS_MAX_DAYS 30, PASS_MIN_DAYS 2, PASS_WARN_AGE 7.


Update passwords: passwd root and passwd <yourlogin> (comply with rules: 10+ chars, upper/lower/number, no 3+ identical, no username; root skips difok).
Verify: chage -l <yourlogin> (check expiry); test weak password rejection.

## 5. Sudo (Visudo) Configuration

Create sudoers file: visudo -f /etc/sudoers.d/custom.
Add lines:

Defaults passwd_tries=3
Defaults badpass_message="Wrong password! Try again."
Defaults logfile="/var/log/sudo/sudo.log"
Defaults log_input, log_output
Defaults requiretty
Defaults secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"


Create log dir: mkdir -p /var/log/sudo.
Verify: sudo -l (check settings); test wrong password (3 tries, custom message, logs).

## 6. SSH Setup

Install: apt install openssh-server.
Edit /etc/ssh/sshd_config: Set Port 4242, PermitRootLogin no.
Restart: systemctl restart ssh.
Verify: ss -tuln | grep 4242 (listening); test non-root SSH from host (understand for new account setup in defense).

## 7. Firewall Setup

Install: apt install ufw.
Configure: ufw allow 4242, ufw enable.
Set default: ufw default deny incoming.
Verify: ufw status verbose (active, only 4242 open, starts on boot).

--
