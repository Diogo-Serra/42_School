#!/bin/bash

LOGDIR="/var/log/server_health"
mkdir -p "$LOGDIR"
exec > "$LOGDIR/report_$(date +%Y%m%d_%H%M%S).log" 2>&1

# -------------------------------------------------------------------
arc=$(uname -a)
p_cpu=$(grep "physical id" /proc/cpuinfo | sort -u | wc -l)
v_cpu=$(grep -c "processor" /proc/cpuinfo)
ram_used=$(free -m | awk 'NR==2 {print $3}')
ram_total=$(free -m | awk 'NR==2 {print $2}')
ram_pct=$(free -m | awk 'NR==2 {printf "%.2f", $3/$2*100}')
disk_used=$(df -h / | awk 'NR==2 {print $3}')
disk_total=$(df -h / | awk 'NR==2 {print $2}')
disk_pct=$(df -h / | awk 'NR==2 {print $5}')
cpu_load=$(mpstat 1 1 | awk 'END {printf "%.2f%%", 100-$NF}' 2>/dev/null || echo "N/A")
last_boot=$(who -b | awk '{print $3" "$4}')
lvm_status=$(lsblk | grep -q "lvm" && echo "Yes" || echo "No")
tcp_connections=$(ss -ta | grep -c ESTAB 2>/dev/null || echo "0")
user_count=$(users | wc -w)
ip_primary=$(ip -4 addr show scope global | grep -oP 'inet \K[\d.]+' | head -1)
ip_extra=$(ip -4 addr show scope global | grep -oP 'inet \K[\d.]+' | tail -n +2 | paste -sd, -)
mac_address=$(ip link show up | grep "link/ether" | awk '{print $2}' | paste -sd, -)
sudo_count=$(journalctl _COMM=sudo --since "10 min ago" | grep -c COMMAND 2>/dev/null || echo "0")
# -------------------------------------------------------------------

echo "SERVER HEALTH REPORT – $(date '+%a %b %d %H:%M:%S %Z %Y')"
echo "========================================================"
echo

echo "SYSTEM INFO"
echo "  Architecture    : $(uname -srm)"
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
[ -n "$ip_extra" ] && echo "  Other IPs       : $ip_extra"
echo "  MAC Address(s)  : $mac_address"
echo

echo "CONNECTIONS & USERS"
echo "  TCP (ESTAB)     : $tcp_connections"
echo "  Logged-in Users : $user_count"
echo "  Sudo Commands   : $sudo_count (last 10 min)"
