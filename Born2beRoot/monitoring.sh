#!/bin/bash

# --- Data Collection ---
arc=$(uname -srm)
p_cpu=$(grep -c "^physical id" /proc/cpuinfo | sort -u | wc -l)
v_cpu=$(nproc)
ram_used=$(free -m | awk 'NR==2{print $3}')
ram_total=$(free -m | awk 'NR==2{print $2}')
ram_pct=$(awk "BEGIN {printf \"%.2f\", $ram_used*100/$ram_total}")
disk_used=$(df -h / | awk 'NR==2{print $3}')
disk_total=$(df -h / | awk 'NR==2{print $2}')
disk_pct=$(df -h / | awk 'NR==2{print $5}')
cpu_load=$(mpstat 1 1 2>/dev/null | awk 'END{printf "%.2f%%", 100-$NF}' || echo "N/A")
last_boot=$(who -b | awk '{print $3" "$4}')
lvm_status=$([ -n "$(lsblk | grep lvm)" ] && echo "Yes" || echo "No")
tcp_connections=$(ss -t state established 2>/dev/null | wc -l | awk '{print $1-1}' || echo "0")
user_count=$(who | wc -l)
ip_primary=$(hostname -I | awk '{print $1}')
mac_address=$(ip link | grep -o "link/ether [[:xdigit:]:]\+" | awk '{print $2}' | tr '\n' ', ' | sed 's/, $//')
sudo_count=$(journalctl _COMM=sudo --since "10 min ago" 2>/dev/null | grep -c "COMMAND" || echo "0")

# --- Output ---
echo "SERVER HEALTH REPORT – $(date '+%a %b %d %H:%M:%S %Z %Y')"
echo "========================================================"
echo

echo "SYSTEM INFO"
echo "  Architecture    : $arc"
echo "  Physical CPUs   : $p_cpu"
echo "  Virtual CPUs    : $v_cpu"
echo "  Last Boot       : $last_boot"
echo "  LVM Active      : $lvm_status"
echo

echo "RESOURCE USAGE"
echo "  Memory          : $ram_used MB / $ram_total MB ($ram_pct%)"
echo "  Disk (/)        : $disk_used / $disk_total ($disk_pct)"
echo "  CPU Load        : $cpu_load"
echo

echo "NETWORK"
echo "  Primary IP      : $ip_primary"
echo "  MAC Address(s)  : $mac_address"
echo

echo "CONNECTIONS & USERS"
echo "  TCP (ESTAB)     : $tcp_connections"
echo "  Logged-in Users : $user_count"
echo "  Sudo Commands   : $sudo_count (last 10 min)"
