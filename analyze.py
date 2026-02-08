#!/usr/bin/env python3
"""
System Report Analyzer - Medium Upgrade Version
Adds: better parsing, threshold alerts, colors
"""

import sys
import os

# Simple color codes
class Color:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    NC = '\033[0m'

def print_colored(text, color):
    """Print text in color"""
    print(f"{color}{text}{Color.NC}")

def analyze_report(report_file):
    """Analyze the system report"""
    
    # Check if file exists
    if not os.path.exists(report_file):
        print_colored(f"Error: File '{report_file}' not found!", Color.RED)
        return False
    
    # Read the file
    try:
        with open(report_file, 'r') as file:
            lines = file.readlines()
    except Exception as e:
        print_colored(f"Error reading file: {e}", Color.RED)
        return False
    
    # Extract CPU and Memory lines
    cpu_line = ""
    memory_line = ""
    
    for line in lines:
        if "Cpu(s)" in line:
            cpu_line = line.strip()
        if "Mem:" in line:
            memory_line = line.strip()
    
    # Display analysis
    print("\n" + "="*50)
    print_colored("        SYSTEM ANALYSIS REPORT", Color.BLUE)
    print("="*50 + "\n")
    
    # CPU Analysis
    if cpu_line:
        print_colored("CPU Usage:", Color.YELLOW)
        print(f"  {cpu_line}")
        
        # Extract idle percentage and calculate usage
        if "id" in cpu_line:
            parts = cpu_line.split(',')
            for part in parts:
                if 'id' in part:
                    try:
                        idle = float(part.split()[0])
                        usage = 100 - idle
                        
                        # Alert based on usage
                        if usage > 80:
                            print_colored(f"  ⚠️  WARNING: High CPU usage ({usage:.1f}%)", Color.RED)
                        elif usage > 50:
                            print_colored(f"  ⚡ Moderate CPU usage ({usage:.1f}%)", Color.YELLOW)
                        else:
                            print_colored(f"  ✓ Normal CPU usage ({usage:.1f}%)", Color.GREEN)
                    except:
                        pass
    else:
        print_colored("CPU data not found", Color.RED)
    
    print()
    
    # Memory Analysis
    if memory_line:
        print_colored("Memory Usage:", Color.YELLOW)
        print(f"  {memory_line}")
        
        # Simple check for memory status
        parts = memory_line.split()
        if len(parts) >= 3:
            print_colored("  ✓ Memory data collected", Color.GREEN)
    else:
        print_colored("Memory data not found", Color.RED)
    
    print("\n" + "="*50 + "\n")
    return True

def main():
    """Main function"""
    
    # Get report file from command line or use default
    if len(sys.argv) > 1:
        report_file = sys.argv[1]
    else:
        # Try to find the most recent report
        if os.path.exists("logs"):
            reports = [f for f in os.listdir("logs") if f.startswith("report_") and f.endswith(".txt")]
            if reports:
                reports.sort(reverse=True)
                report_file = os.path.join("logs", reports[0])
            else:
                print_colored("Error: No reports found in logs directory", Color.RED)
                return 1
        else:
            print_colored("Error: logs directory not found", Color.RED)
            return 1
    
    # Analyze the report
    success = analyze_report(report_file)
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
