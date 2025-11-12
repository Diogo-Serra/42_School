#!/bin/bash

# ========================================
# 1. DATA COLLECTION
# ========================================

arch=$(uname -a)
cpu_physical=$(lscpu | grep Socket | awk '{print $2}')
vcpu=$(nproc)

mem_used=$(free -m | grep Mem | awk '{print $3}')
mem_total=$(free -m | grep Mem | awk '{print $2}')
mem_percent=$(free -m | grep Mem | awk '{print $3/$2 * 100}')

disk_used=$(df -h --block-size=G --total | tail -n 1 | awk '{print $3}' | cut -d G -f1)
disk_total=$(df -h --block-size=G --total | tail -n 1 | awk '{print $2}' | cut -d G -f1)
disk_percent=$(df -h --block-size=G --total | tail -n 1 | awk '{print $5}' | cut -d % -f1)

cpu_user=$(mpstat | tail -n 1 | awk '{print $4}')
cpu_system=$(mpstat | tail -n 1 | awk '{print $6}')
cpu_load=$(echo "$cpu_user + $cpu_system" | bc)

last_boot=$(who -b | awk '{print $3 " " $4}')

lvm_count=$(cat /etc/fstab | grep /dev/mapper | wc -l)
lvm_use=$([ $lvm_count -gt 0 ] && echo "yes" || echo "no")

tcp_established=$(echo "$(ss -t state established | wc -l) - 1" | bc)

user_log=$(($(w | wc -l) - 2))

ip_addr=$(ip address | grep enp | grep inet | awk '{print $2}' | cut -d / -f1)
mac_addr=$(ip address | grep enp -A 1 | grep ether | awk '{print $2}')

sudo_seq=$(cat /var/log/sudo/seq 2>/dev/null || echo "0")
sudo_cmd_count=$(echo "obase=10; ibase=36; $sudo_seq" | bc 2>/dev/null || echo "0")


# ========================================
# 2. PRINTING
# ========================================

printf "\n"
printf "#Architecture: %s\n" "$arch"
printf "#CPU physical: %s\n" "$cpu_physical"
printf "#vCPU: %s\n" "$vcpu"
printf "\n"
printf "#Memory Usage: %s/%sMB (%s%%)\n" "$mem_used" "$mem_total" "$(printf "%.0f" "$mem_percent")"
printf "#Disk Usage: %s/%sGb (%s%%)\n" "$disk_used" "$disk_total" "$disk_percent"
printf "\n"
printf "#CPU load: %s%%\n" "$(printf "%.2f" "$cpu_load")"
printf "#Last boot: %s\n" "$last_boot"
printf "#LVM use: %s\n" "$lvm_use"
printf "\n"
printf "#Connections TCP: %s ESTABLISHED\n" "$tcp_established"
printf "#User log: %s\n" "$user_log"
printf "\n"
printf "#Network: IP %s (%s)\n" "$ip_addr" "$mac_addr"
printf "#Sudo: %s cmd\n" "$sudo_cmd_count"
printf "\n"
printf "#Connections TCP: %s ESTABLISHED\n" "$tcp_established"
printf "#User log: %s\n" "$user_log"
printf "#Network: IP %s (%s)\n" "$ip_addr" "$mac_addr"
printf "#Sudo: %s cmd\n" "$sudo_cmd_count"

