#!/bin/bash
# ========================================
# 1. DATA COLLECTION 
# ========================================
os_name=$(uname -o)
kernel_version=$(uname -r)
arch=$(uname -m)
cpu_cores=$(lscpu | awk '/^Socket$s$:/ {print $2}')
vcpu=$(nproc)

mem_total=$(free -m | awk '/^Mem:/ {print $2}')
mem_used=$(free -m  | awk '/^Mem:/ {print $3}')
mem_pct=$(awk "BEGIN {printf \"%.0f\", $mem_used*100/$mem_total}")

disk_used=$(df -h --total | tail -1 | awk '{print $3}' | sed 's/G$//')
disk_total=$(df -h --total | tail -1 | awk '{print $2}' | sed 's/G$//')
disk_pct=$(df -h --total | tail -1 | awk '{print $5}' | sed 's/%$//')

# CPU load from /proc/stat (user + system)
read -r u _ s i _ < <(grep '^cpu ' /proc/stat | awk '{print $2,$4,$5,$6}')
total=$((u + s + i))
used=$((u + s))
subject=$(awk "BEGIN {printf \"%.1f\", $used*100/$total}")
cpu_per_vcpu=$(awk "BEGIN {printf \"%.1f\", $used*100/$total/$vcpu}")

last_boot=$(who -b | awk '{print $3 " " $4}')
tcp_est=$(ss -t state established | wc -l)
tcp_est=$((tcp_est - 1))
users=$(w -h | wc -l)
ip_addr=$(ip route get 1 | awk '{print $7; exit}' 2>/dev/null || echo "N/A")
mac_addr=$(ip link | awk '/ether/ {print $2; exit}' 2>/dev/null || echo "N/A")
sudo_cmds=$(journalctl _COMM=sudo 2>/dev/null | grep -c "COMMAND=" || echo 0)

# Check if LVM is active
lvm_status=$(sudo lvdisplay > /dev/null 2>&1 && echo "Yes" || echo "No")

# ========================================
# 2. PRINTING 
# ========================================
echo "SYSTEM"
echo "  OS       : $os_name"
echo "  Kernel   : $kernel_version"
echo "  Architecture : $arch"
echo "  CPU      : $cpu_cores core(s), $vcpu vCPU"
echo "  Boot     : $last_boot"
echo "  LVM      : $lvm_status"
echo

echo "RESOURCES"
echo "  RAM  : $mem_used / $mem_total MB ($mem_pct%)"
echo "  Disk : $disk_used / $disk_total GB ($disk_pct%)"
echo "  CPU  : $subject% (user+system) | $cpu_per_vcpu% per vCPU"
echo

echo "NETWORK"
echo "  IP       : $ip_addr"
echo "  MAC      : $mac_addr"
echo "  TCP      : $tcp_est established"
echo "  Users    : $users logged in"
echo "  Sudo     : $sudo_cmds cmd(s)"
echo
