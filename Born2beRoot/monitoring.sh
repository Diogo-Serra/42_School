#!/bin/bash

#LOGDIR="/var/log/server_health"
#mkdir -p "$LOGDIR"
#exec > "$LOGDIR/report_$(date +%Y%m%d_%H%M%S).log" 2>&1

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
ip_extra=$(ip -4 addr show scope global | grep -oP 'inet \K[\d.]+' | tail -n +2 | tr '\n' ', ' | sed 's/, $//')
mac_address=$(ip link show up | grep "link/ether" | awk '{print $2}' | tr '\n' ',' | sed 's/, $//')
sudo_count=$(journalctl _COMM=sudo --since "10 min ago" | grep -c COMMAND 2>/dev/null)
# -------------------------------------------------------------------

printf "\n\n\n"
printf '%s\n' "$(printf '=%.0s' {1..56})"
printf '%s\n' "SERVER HEALTH REPORT – $(date '+%a %b %d %H:%M:%S %Z %Y')"
printf '%s\n\n' "$(printf '=%.0s' {1..56})"

printf '%-18s\n' "SYSTEM INFO"
printf '  %-16s: %s\n' "Architecture" "$(uname -srm)"
printf '  %-16s: %s\n' "Physical CPUs" "$p_cpu"
printf '  %-16s: %s\n' "Virtual CPUs" "$v_cpu"
printf '  %-16s: %s\n' "Last Boot" "$last_boot"
printf '  %-16s: %s\n' "LVM Active" "$lvm_status"
printf '\n'

printf '%-18s\n' "RESOURCE USAGE"
printf '  %-16s: %d MB / %d MB  (%s)\n' "Memory" "$ram_used" "$ram_total" "$ram_pct%"
printf '  %-16s: %s / %s     (%s)\n' "Disk (/)" "$disk_used" "$disk_total" "$disk_pct"
printf '  %-16s: %s\n' "CPU Load" "$cpu_load"
printf '\n'

printf '%-18s\n' "NETWORK"
printf '  %-16s: %s\n' "Primary IP" "$ip_primary"
[ -n "$ip_extra" ] && printf '  %-16s: %s\n' "Other IPs" "$ip_extra"
printf '  %-16s: %s\n' "MAC Address(s)" "$mac_address"
printf '\n'

printf '%-18s\n' "CONNECTIONS & USERS"
printf '  %-16s: %s\n' "TCP (ESTAB)" "$tcp_connections"
printf '  %-16s: %s\n' "Logged-in Users" "$user_count"
printf '  %-16s: %s\n\n\n' "Sudo Commands" "$sudo_count"


