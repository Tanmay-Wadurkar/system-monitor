#!/bin/bash

LOG_FILE="logs/report.txt"

echo "-----System Report-----"> $LOG_FILE
echo "Date:$(date)" >> $LOG_FILE

echo "CPU Usage : " >> $LOG_FILE
top -bn1 | grep "Cpu(s)" >> $LOG_FILE

echo "Memory Usage : " >> $LOG_FILE
free -h >> $LOG_FILE

echo "Disk Usage : " >> $LOG_FILE
df -h >> $LOG_FILE

python3 analyze.py

