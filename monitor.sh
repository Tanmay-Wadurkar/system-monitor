#!/bin/bash

#System monitor medium upgraded version 
# Ads : timestamps, basic error checking, simple colors

# Configuration 

LOG_DIR="logs"
LOG_FILE="${LOG_DIR}/report_$(date +%Y%m%d_%H%M%S).txt"

#Simple color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'  # No Color

#Check if dir exisst 
if [ ! -d "$LOG_DIR" ];  then #check if log_file not exists 
  mkdir  -p "$LOG_DIR"
  echo -e "${green}Created log directory${NC}"
fi

if !  command -v python3 &> /dev/null;then
  echo -e "${RED}Error: python3 is not installed!${NC}"
  echo "Please install python3 to continue" 
  exit 1
fi

#start monitring 

echo -e "${GREEN} Start system monitoring... ${NC}"
echo -e "${YELLOW} REPORT will be saved to :$LOG_FILE ${NC}"

echo "-----SYSTEM MONITORING----" > $LOG_FILE
echo "Date and Time : $(date '+%Y/%m/%d %H:%M:%S')" >> $LOG_FILE
echo "Hostname : $(hostname)">> $LOG_FILE
echo "Uptime : $(uptime -p)" >> $LOG_FILE
echo "" >> $LOG_FILE

echo "CPU Usage : " >>  $LOG_FILE
top -bn1 | grep "Cpu(s)" >>  $LOG_FILE
echo "" >> $LOG_FILE

echo "Memory Usage : " >>  $LOG_FILE
free -h  >>  $LOG_FILE
echo "" >>   $LOG_FILE

echo "Disk Usage : " >>   $LOG_FILE
df -h >>  $LOG_FILE
echo "" >>   $LOG_FILE

echo -e "${GREEN} Report generated successfully!${NC}"

#Run python analysis

if python3 analyze.py "$LOG_FILE"; then
    echo -e "${GREEN}✓ Analysis complete!${NC}"
else
    echo -e "${RED}✗ Analysis failed!${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}========== Monitoring Complete ==========${NC}"
echo -e "${YELLOW}Report saved to: $LOG_FILE${NC}"
