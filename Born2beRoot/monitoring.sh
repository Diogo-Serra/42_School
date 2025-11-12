#!/bin/bash

# -------------------------------------------------
# LOGGING 
# -------------------------------------------------
LOGDIR="/var/log/server_health"
mkdir -p "$LOGDIR"
exec > "$LOGDIR/report_$(date +%Y%m%d_%H%M%S).log" 2>&1
# -------------------------------------------------

# ------------------- DATA COLLECTION -------------------
arch=$(uname -srm)

# Physical CPUs
p_cpu=$(grep "physical id" /proc/cpuinfo | sort -u | wc -l)
[ "$p_cpu" -eq 0 ] && p_cpu=1

# Virtual CPUs
v_cpu=$(grep -c "processor" /proc/cpuinfo)

# Memory (in MB)
ram_used=$(free -m | awk 'NR==2 {print $3}')
ram_total=$(free -m | awk 'NR==2 {print $2}')
ram_pct=$(awk "BEGIN {printf \"%.2f\", $ram_used/$ram_total*100}")

# Disk (root partition)
disk_used=$(df -h / | awk 'NR==2 {print $3}')
disk_total=$(df -h / | awk 'NR==2 {print $2}')
disk_pct=$(df -h / | awk 'NR==2 {print $5}' | tr -d '%')

# CPU load
cpu_load=$(mpstat 1 1 | awk 'END {printf "%.2f%%", 100-$NF}' 2>/dev/null || echo "N/A")

# Last boot
last_boot=$(who -b | awk '{print $3" "$4}')

# LVM
lvm_status=$(lsblk | grep -q "lvm" && echo "Yes" || echo "No")

# TCP established connections
tcp_connections=$(ss -ta | grep -c ESTAB 2>/dev/null || echo "0")

# Logged-in users
user_count=$(who | wc -l)

# Primary IP (first global IPv4 address)
ip_primary=$(ip -4 addr show scope global | grep -oP 'inet \K[\d.]+' | head -1)

# Extra IPs (all others)
ip_extra=$(ip -4 addr show scope global | grep -oP 'inet \K[\d.]+' | tail -n +2 | tr '\n' ', ' | sed 's/, $//')
[ -z "$ip_extra" ] && ip_extra="None"

# MAC address(es)
mac_address=$(ip link show up | grep "link/ether" | awk '{print $2}' | tr '\n' ',' | sed 's/,$//')
[ -z "$mac_address" ] && mac_address="N/A"

# Sudo commands in the last 10 minutes
sudo_count=$(journalctl _COMM=sudo --since "10 minutes ago" --no-pager | grep -c "COMMAND=" 2>/dev/null || echo "0")
# -------------------------------------------------

# ------------------- PRINT REPORT -------------------
printf '%s\n' "============================================================"
printf '%s\n' "SERVER HEALTH REPORT – $(date '+%a %b %d %H:%M:%S %Z %Y')"
printf '%s\n\n' "============================================================"

printf '%-18s\n' "SYSTEM INFO"
printf ' %-16s: %s\n'   "Architecture"   "$arch"
printf ' %-16s: %s\n'   "Physical CPUs" "$p_cpu"
printf ' %-16s: %s\n'   "Virtual CPUs"  "$v_cpu"
printf ' %-16s: %s\n'   "Last Boot"     "$last_boot"
printf ' %-16s: %s\n'   "LVM Active"    "$lvm_status"
printf '\n'

printf '%-18s\n' "RESOURCE USAGE"
printf ' %-16s: %s MB / %s MB (%s%%)\n' "Memory" "$ram_used" "$ram_total" "$ram_pct"
printf ' %-16s: %s / %s (%s%%)\n'       "Disk (/)" "$disk_used" "$disk_total" "$disk_pct"
printf ' %-16s: %s\n'   "CPU Load"      "$cpu_load"
printf '\n'

printf '%-18s\n' "NETWORK"
printf ' %-16s: %s\n'   "Primary IP"    "$ip_primary"
printf ' %-16s: %s\n'   "Other IPs"     "$ip_extra"
printf ' %-16s: %s\n'   "MAC Address(s)" "$mac_address"
printf '\n'

printf '%-18s\n' "CONNECTIONS & USERS"
printf ' %-16s: %4s\n'  "TCP (ESTAB)"   "$tcp_connections"
printf ' %-16s: %4s\n'  "Logged-in Users" "$user_count"
printf ' %-16s: %4s (last 10 min)\n' "Sudo Commands" "$sudo_count"
# -------------------------------------------------
