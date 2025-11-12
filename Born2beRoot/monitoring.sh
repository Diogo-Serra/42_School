#!/bin/bash


LOGDIR="/var/log/server_health"
mkdir -p "$LOGDIR"
exec > "$LOGDIR/report_$(date +%Y%m%d_%H%M%S).log" 2>&1

# -------------------------------------------------------------------
# Data Collection (simplified & reliable)
# -------------------------------------------------------------------

# System
arch=$(uname -srm)
p_cpu=$(lscpu | grep -E '^CPU\(s\):' | awk '{print $2}' | head -1)  # Total vCPUs
v_cpu=$p_cpu
p_cpu_count=$(grep "physical id" /proc/cpuinfo | sort -u | wc -l)
[[ $p_cpu_count -eq 0 ]] && p_cpu_count=1  # fallback

# Memory (in MB)
read ram_used ram_total <<< $(free --mega | awk 'NR==2 {print $3, $2}')
ram_pct=$(awk "BEGIN {printf \"%.2f\", $ram_used/$ram_total*100}")

# Disk (root partition)
read _ disk_used disk_total disk_pct _ <<< $(df -h / | awk 'NR==2')
disk_pct=${disk_pct%%%}  # Remove trailing %

# CPU Load
cpu_load=$(mpstat 1 1 | awk 'END {printf "%.2f%%", 100-$NF}' 2>/dev/null || echo "N/A")

# Boot
last_boot=$(who -b | awk '{print $3" "$4}')

# LVM
lvm_status=$(lsblk -o TYPE | grep -q lvm && echo "Yes" || echo "No")

# Network
tcp_connections=$(ss -t -a | grep -c ESTAB 2>/dev/null || echo "0")
ip_primary=$(ip -4 route get 1 | awk '{print $7; exit}')
ip_list=($(ip -4 addr show scope global | grep -oP 'inet \K[\d.]+' | sort))
mac_list=($(ip link show up | grep -E "link/ether" | awk '{print $2}'))

# Users
user_count=$(who | wc -l)  # More accurate than `users`
# user_count=$(users | wc -w)  # alternative

# Sudo
sudo_count=$(journalctl _COMM=sudo --since "10 minutes ago" --no-pager | grep -c "COMMAND=" 2>/dev/null || echo "0")

# Format extra IPs and MACs
ip_extra=$(printf '%s, ' "${ip_list[@]:1}" | sed 's/, $//')
[[ -z "$ip_extra" ]] && ip_extra="None"
mac_address=$(printf '%s, ' "${mac_list[@]}" | sed 's/, $//')
[[ -z "$mac_address" ]] && mac_address="N/A"

# -------------------------------------------------------------------
# Output Report
# -------------------------------------------------------------------

print_header() {
    printf '%s\n' "$(printf '=%.0s' {1..60})"
    printf '%s\n' "SERVER HEALTH REPORT – $(date '+%a %b %d %H:%M:%S %Z %Y')"
    printf '%s\n\n' "$(printf '=%.0s' {1..60})"
}

print_section() {
    printf '%-18s\n' "$1"
}

print_field() {
    printf ' %-16s: %s\n' "$1" "$2"
}

print_header

print_section "SYSTEM INFO"
print_field "Architecture" "$arch"
print_field "Physical CPUs" "$p_cpu_count"
print_field "Virtual CPUs"  "$v_cpu"
print_field "Last Boot"     "$last_boot"
print_field "LVM Active"    "$lvm_status"
printf '\n'

print_section "RESOURCE USAGE"
print_field "Memory"        "$ram_used MB / $ram_total MB ($ram_pct%)"
print_field "Disk (/)"      "$disk_used / $disk_total ($disk_pct%)"
print_field "CPU Load"      "$cpu_load"
printf '\n'

print_section "NETWORK"
print_field "Primary IP"    "$ip_primary"
print_field "Other IPs"     "$ip_extra"
print_field "MAC Address(s)" "$mac_address"
printf '\n'

print_section "CONNECTIONS & USERS"
print_field "TCP (ESTAB)"   "$tcp_connections"
print_field "Logged-in Users" "$user_count"
print_field "Sudo Commands" "$sudo_count (last 10 min)"

