#!/bin/bash
# ========================================
# 1. DATA COLLECTION
# ========================================
arch=$(uname -a)
cpu_physical=$(lscpu | awk '/^Socket\(s\):/ {print $2}')
vcpu=$(nproc)

# ---- Memory -------------------------------------------------
mem_total=$(free -m | awk '/^Mem:/ {print $2}')
mem_used=$(free -m  | awk '/^Mem:/ {print $3}')
mem_percent=$(awk "BEGIN {printf \"%.0f\", $mem_used*100/$mem_total}")

# ---- Disk ---------------------------------------------------
read -r _ disk_used _ disk_total disk_percent _ < \
    <(df -h --block-size=G --total | tail -n1)
disk_used=${disk_used%G}
disk_total=${disk_total%G}
disk_percent=${disk_percent%\%}

# ---- CPU load (user + system) -------------------------------
read -r cpu_user cpu_nice cpu_system cpu_idle _ < \
    <(grep '^cpu ' /proc/stat | awk '{print $2,$3,$4,$5}')
cpu_total=$((cpu_user + cpu_nice + cpu_system + cpu_idle))
cpu_used=$((cpu_user + cpu_system))
# simple percentage (no bc)
cpu_load=$(awk "BEGIN {printf \"%.2f\", $cpu_used*100/$cpu_total}")

# ---- Misc ---------------------------------------------------
last_boot=$(who -b | awk '{print $3 " " $4}')
lvm_use=$([ $(lsblk -o TYPE | grep -c lvm) -gt 0 ] && echo "yes" || echo "no")

tcp_established=$(( $(ss -tan state established | wc -l) - 1 ))
user_log=$(( $(w -h | wc -l) ))

ip_addr=$(ip -4 -br addr show dev "$(ip -br link show | awk '/UP/ {print $1}' | head -1)" |
          awk '{print $3}' | cut -d/ -f1)
mac_addr=$(ip link show | awk '/ether/ {print $2; exit}')

sudo_cmd_count=$(journalctl -u sudo --since "1970-01-01" | grep -c "COMMAND=" || echo 0)

# ========================================
# 2. PRINTING – tidy sections
# ========================================
print_section() {
    printf "\n\e[1;34m=== %s ===\e[0m\n" "$1"
}

print_section "SYSTEM OVERVIEW"
printf "  Architecture      : %s\n" "$arch"
printf "  CPU physical      : %s\n" "$cpu_physical"
printf "  vCPU              : %s\n" "$vcpu"

print_section "MEMORY"
printf "  Usage             : %s / %s MB (%s%%)\n" "$mem_used" "$mem_total" "$mem_percent"

print_section "DISK"
printf "  Usage             : %s / %s GB (%s%%)\n" "$disk_used" "$disk_total" "$disk_percent"

print_section "CPU"
printf "  Load (user+system): %s%%\n" "$cpu_load"

print_section "BOOT & LVM"
printf "  Last boot         : %s\n" "$last_boot"
printf "  LVM in use        : %s\n" "$lvm_use"

print_section "NETWORK"
printf "  TCP established   : %s\n" "$tcp_established"
printf "  Users logged in   : %s\n" "$user_log"
printf "  IP / MAC          : %s (%s)\n" "$ip_addr" "$mac_addr"

print_section "SUDO"
printf "  Commands executed : %s\n" "$sudo_cmd_count"
printf "\n"
