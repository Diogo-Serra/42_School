<div align="center">

<img src="https://github.com/ayogun/42-project-badges/blob/main/covers/cover-born2beroot-bonus.png?raw=true"/>


# Born2beRoot — Secure Linux Configuration Guide

This guide documents the **initial setup and hardening** of a Debian-based system for the **42 School project environment**.  
It covers everything from user creation to SSH, password policies, and firewall configuration — all built for stability, security, and compliance.
</div>

---

### Download the VDI File

You can download the **.vdi file** using the link below:

[Download .vdi file](https://1drv.ms/f/c/C6D9B4F0E148D4C6/EoL0v2dzwsNMnMruQxg4hXkBD8hSPQRppuxdsQLh7K9pJg?e=HaqYWy)

## ⚙️ 1. Initial Machine Setup and Basic APT
  
  **Update and upgrade system**
  
   ```bash
   apt update && apt upgrade
   ```

  **Verify system information**

```bash
uname -a
lsblk
aa-status
```
💡 You may use aptitude for better dependency management.

---


## 🖥️ 2. Hostname Configuration

**Edit hostname**
```bash
nano /etc/hostname
nano /etc/hosts
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
adduser wil user42
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
Defaults env_reset
Defaults passwd_tries=3
Defaults badpass_message="Incorrect password! Please, try again."
Defaults logfile="/var/log/sudo/sudo.log"
Defaults log_input, log_output
Defaults iolog_dir="/var/log/sudo"
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
nano /etc/ssh/sshd_config
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

# Born2beroot - Partition Setup (LVM)

**Goal**: Secure, encrypted, logical partition layout using **LVM**.

---

## Disk Layout (Example: 20GB disk)

| Mount Point | Size     | Type           | LVM LV       | Encrypted |
|-------------|----------|----------------|--------------|-----------|
| `/boot`     | 512 MB   | ext4           | —            | No        |
| (LVM)       | ~19.5 GB | crypto_LVM     | —            | Yes       |
| `/` (root)  | 10 GB    | ext4           | lv_root      | Yes       |
| `/home`     | 4 GB     | ext4           | lv_home      | Yes       |
| `swap_1`    | 2 GB     | swap           | lv_swap_1    | Yes       |
| `/var`      | 3 GB     | ext4           | lv_var       | Yes       |
| `/var/log`  | 1 GB     | ext4           | lv_varlog    | Yes       |

---

## Installation Steps (Debian Installer)

1. **Boot Debian ISO** → Graphical/Expert install  
2. **Partition disks** → Manual  
3. Create:
   - `512M` → `/boot` → **ext4** → **Do not encrypt**
   - Rest → **Physical volume for encryption**
4. Set **LVM passphrase**  
5. Inside encrypted volume:
   - Create **LVM Volume Group** (`vg1`)
   - Create **Logical Volumes**:
     - `lv_root` → 10G → `/`
     - `lv_home` → 4G → `/home`
     - `lv_var` → 3G → `/var`
     - `lv_varlog` → 1G → `/var/log`
     - `lv_swap_1` → 2G → swap
6. Format each LV as **ext4** (swap as swap)  
7. **Finish partitioning** → Write changes

---

## Post-Install Check

```bash
lsblk -f
# Should show:
# ├─/boot (ext4)
# └─crypto_LVM
#    └─vg1
#       ├─lv_root → /
#       ├─lv_home → /home
#       ├─lv_var  → /var
#       ├─lv_varlog → /var/log
#       └─lv_swap_1 → swap
```

## 📘 Notes

    💡 Keep everything documented and reproducible for your 42 evaluation.

    🔒 Security and consistency are key — verify every change manually.

    🧰 Optional: automate setup using a Bash script for faster rebuilds.
