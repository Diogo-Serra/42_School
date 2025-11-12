#!/bin/bash
# ========================================
# 1. DATA COLLECTION (no mpstat, no bc)
# ========================================
arch=$(uname -m)
cpu_cores=$(lscpu | awk '/^Socket\(s\):/ {print $2}')
vcpu=$(nproc)

mem_total=$(free -m | awk '/^Mem:/ {print $2}')
mem_used=$(free -m  | awk '/^Mem:/ {print $3}')
mem_pct=$(awk "BEGIN {printf \"%.0f\", $mem_used*100/$mem_total}")

disk_used=$(df -h --total | tail -1 | awk '{print $3}' | sed 's/G$//')
disk_total=$(df -h --total | tail -1 | awk '{print $2}' | sed 's/G$//')
disk_pct=$(df -h --total | tail -1 | awk '{print $5}' | sed 's/%$//')

# CPU load from /proc/stat
read -r u _ s i _ < <(grep '^cpu ' /proc/stat | awk '{print $2,$4,$5,$6}')
total=$((u + s + i))
cpu_load=$(awk "BEGIN {printf \"%.1f\", ($u+$s)*100/$total}")

last_boot=$(who -b | awk '{print $3 " " $4}')
tcp_est=$(ss -t state established | wc -l)
tcp_est=$((tcp_est - 1))
users=$(w -h | wc -l)
ip_addr=$(ip route get 1 | awk '{print $7; exit}')
mac_addr=$(ip link | awk '/ether/ {print $2; exit}')
sudo_cmds=$(journalctl _COMM=sudo 2>/dev/null | grep -c "COMMAND=" || echo 0)

# ========================================
# 2. PRINTING – Clean & Beautiful
# ========================================
BLUE="\e[1;34m"
GREEN="\e[1;32m"
RESET="\e[0m"

echo -e "${BLUE}SYSTEM${RESET}"
printf "  OS       : %s\n" "$arch"
printf "  CPU      : %s core(s), %s vCPU\n" "$cpu_cores" "$vcpu"
printf "  Boot     : %s\n" "$last_boot"
echo

echo -e "${GREEN}RESOURCES${RESET}"
printf "  RAM  : %s / %s MB (%s%%)\n" "$mem_used" "$mem_total" "$mem_pct"
printf "  Disk : %s / %s GB (%s%%)\n" "$disk_used" "$disk_total" "$disk_pct"
printf "  CPU  : %s%% load\n" "$cpu_load"
echo

echo -e "${BLUE}NETWORK${RESET}"
printf "  IP       : %s\n" "$ip_addr"
printf "  MAC      : %s\n" "$mac_addr"
printf "  TCP      : %s established\n" "$tcp_est"
printf "  Users    : %s logged in\n" "$users"
printf "  Sudo     : %s cmd(s)\n" "$sudo_cmds"
echo
