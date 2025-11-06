#!/bin/bash

# This script monitors basic server health and system information,
# looping indefinitely for use as a systemd service.

while true
do
    # Clear the screen for a cleaner 'journalctl' output on each iteration
    # Note: This is optional but can make live-viewing easier to read.
    # To disable, just comment out the next line.
    clear

    # -------------------------------------------------------------------
    # System Information Gathering
    # -------------------------------------------------------------------
    arc=$(uname -a)
    p_cpu=$(grep "physical id" /proc/cpuinfo | sort -u | wc -l)
    v_cpu=$(grep -c "processor" /proc/cpuinfo)
    ram_info=$(free -m | awk 'NR==2 {printf "%s/%sMB (%.2f%%)", $3, $2, $3/$2*100}')
    disk_info=$(df -h / | awk 'NR==2 {printf "%s/%sB (%s)", $3, $2, $5}')
    cpu_load=$(mpstat 1 1 | awk 'END {printf "%.2f%%", 100 - $NF}')
    last_boot=$(who -b | awk '{print $3 " " $4}')
    lvm_status=$(if [ $(lsblk | grep -c "lvm") -gt 0 ]; then echo "active"; else echo "inactive"; fi)
    tcp_connections=$(ss -ta | grep -c ESTAB)
    user_count=$(users | wc -w)
    ip_address=$(ip -4 addr show scope global | grep inet | awk '{print $2}' | cut -d/ -f1)
    mac_address=$(ip link | grep "link/ether" | awk '{print $2}')
    sudo_count=$(journalctl _COMM=sudo | grep -c COMMAND)

    # -------------------------------------------------------------------
    # Final Output
    # -------------------------------------------------------------------
    cat << EOF
# =========================================================
# Server Health Report at $(date)
# =========================================================
# Architecture: $arc
# CPU physical: $p_cpu
# vCPU: $v_cpu
# Memory Usage: $ram_info
# Disk Usage: $disk_info
# CPU load: $cpu_load
# Last boot: $last_boot
# LVM use: $lvm_status
# Connexions TCP: $tcp_connections ESTABLISHED
# User log: $user_count
# Network: IP $ip_address($mac_address)
# Sudo: $sudo_count cmd
EOF

    # -------------------------------------------------------------------
    # Wait for 60 seconds before the next loop
    # -------------------------------------------------------------------
    sleep 60
done

