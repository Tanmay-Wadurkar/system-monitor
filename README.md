# 🖥️ System Monitor

A Linux system monitoring tool built with Shell Scripting and Python. Monitors CPU, memory, and disk usage with intelligent analysis and color-coded alerts.

![Linux](https://img.shields.io/badge/Platform-Linux-blue.svg)
![Shell Script](https://img.shields.io/badge/Shell-Bash-green.svg)
![Python](https://img.shields.io/badge/Python-3.x-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)

---

## ✨ Features

- 🖥️ **Real-time CPU Monitoring** - Tracks CPU usage with idle/active percentage calculation
- 💾 **Memory Tracking** - Monitors RAM usage with detailed statistics
- 💿 **Disk Usage Analysis** - Checks filesystem usage across all partitions
- 📝 **Timestamped Reports** - Each report saved with unique timestamp for history tracking
- 🚨 **Smart Alerts** - Color-coded warnings based on resource usage thresholds
  - 🟢 Normal (< 50%)
  - 🟡 Moderate (50-80%)
  - 🔴 High (> 80%)
- 🎨 **Color-Coded Terminal Output** - Easy-to-read interface with visual indicators
- 🐍 **Automated Python Analysis** - Intelligent parsing and alert generation

---

## 📋 Prerequisites

- **Operating System**: Linux (Ubuntu, Debian, CentOS, RHEL, etc.)
- **Shell**: Bash 4.0+
- **Python**: 3.6 or higher
- **System Tools**: `top`, `free`, `df`, `grep` (pre-installed on most Linux systems)

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Tanmay-Wadurkar/system-monitor.git
cd system-monitor
```

### 2. Make Scripts Executable

```bash
chmod +x monitor.sh analyze.py
```

### 3. Run the Monitor

```bash
./monitor.sh
```

That's it! The monitor will:
- Generate a timestamped report in `logs/` directory
- Automatically analyze the report
- Display color-coded results in your terminal

---
## 🐳 Docker Deployment

### Quick Start with Docker

The easiest way to run this monitor is using Docker:

```bash
# Pull and run from Docker Hub
docker run --rm -v $(pwd)/logs:/app/logs tanmaywadurkar/system-monitor:latest
```

Replace `tanmaywadurkar` with your Docker Hub username.

### What This Does

- Downloads the pre-built image (if not already downloaded)
- Runs the system monitor
- Saves reports to your local `logs/` directory
- Automatically removes container when done

### Docker Hub

**Image:** [tanmaywadurkar/system-monitor](https://hub.docker.com/r/tanmaywadurkar/system-monitor)

**Tags:**
- `latest` - Most recent version

### Build Locally

If you want to build the image yourself:

```bash
# Clone the repository
git clone https://github.com/Tanmay-Wadurkar/system-monitor.git
cd system-monitor

# Build the image
docker build -t system-monitor:latest .

# Run it
docker run --rm -v $(pwd)/logs:/app/logs system-monitor:latest
```

### Using Docker Compose

```bash
# Run with docker-compose
docker compose run --rm system-monitor

# Or build and run in one command
docker compose up --build
```

### Requirements

- Docker installed (version 20.10+)
- No other dependencies needed!

### Benefits of Docker Version

- ✅ No manual dependency installation
- ✅ Works on any system with Docker
- ✅ Consistent environment
- ✅ Easy to share and deploy
- ✅ Isolated from host system

## 📁 Project Structure

```
system-monitor/
├── monitor.sh          # Main monitoring script (Bash)
├── analyze.py          # Analysis script with alerts (Python)
├── .gitignore          # Git ignore rules
├── README.md           # This file
└── logs/               # Generated reports (auto-created)
    └── report_YYYYMMDD_HHMMSS.txt
```

---

## 📊 Sample Output

### Terminal Output:
```
Starting System Monitor...
Report will be saved to: logs/report_20260208_143022.txt
✓ Report generated successfully!
Running analysis...

==================================================
        SYSTEM ANALYSIS REPORT
==================================================

CPU Usage:
  %Cpu(s):  5.2 us,  2.1 sy,  0.0 ni, 92.3 id
  ✓ Normal CPU usage (7.7%)

Memory Usage:
  Mem:   15.6Gi   8.2Gi   4.5Gi   123Mi   2.9Gi   6.2Gi
  ✓ Memory data collected

==================================================

✓ Analysis complete!

========== Monitoring Complete ==========
Report saved to: logs/report_20260208_143022.txt
```

### Report File Content:
```
-----System Report-----
Date: 2026-02-08 14:30:22
Hostname: ubuntu-server
Uptime: up 5 days, 3 hours, 45 minutes

CPU Usage:
%Cpu(s):  5.2 us,  2.1 sy,  0.0 ni, 92.3 id, ...

Memory Usage:
              total        used        free      shared  buff/cache   available
Mem:           15Gi        8.2Gi       4.5Gi       123Mi       2.9Gi       6.2Gi
Swap:         2.0Gi          0B       2.0Gi

Disk Usage:
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       250G  145G   93G  58% /
...
```

---

## 🛠️ Usage

### Basic Monitoring
Run the monitor once:
```bash
./monitor.sh
```

### View Latest Report
```bash
cat logs/report_*.txt | tail -50
```

### Run Analysis on Specific Report
```bash
python3 analyze.py logs/report_20260208_143022.txt
```

### Auto-find Latest Report
```bash
python3 analyze.py
```

### Monitor Continuously (Every 5 minutes)
```bash
watch -n 300 ./monitor.sh
```

---

## ⚙️ Configuration

### Modify Alert Thresholds

Edit `analyze.py` to change when alerts trigger:

```python
# Around line 70-75
if usage > 80:              # Change from 80 to your threshold
    print("WARNING: High usage")
elif usage > 50:            # Change from 50 to your threshold
    print("Moderate usage")
```

### Change Report Frequency

For automated monitoring with cron:

```bash
# Edit crontab
crontab -e

# Add this line to run every hour
0 * * * * /path/to/system-monitor/monitor.sh

# Or every 30 minutes
*/30 * * * * /path/to/system-monitor/monitor.sh
```

---

## 📈 Version History

### v2.0 (February 2026) - Current
- ✅ Timestamped log files for historical tracking
- ✅ Color-coded terminal output (green/yellow/red)
- ✅ Automated Python analysis integration
- ✅ Error checking and validation
- ✅ Smart CPU usage threshold detection
- ✅ Fixed grep pattern for accurate CPU data extraction
- ✅ Added .gitignore for clean repository management

### v1.0 (Initial Release)
- Basic CPU, Memory, and Disk monitoring
- Simple report generation
- Manual analysis

---

## 🐛 Troubleshooting

### Issue: "Permission denied"
```bash
chmod +x monitor.sh analyze.py
```

### Issue: "python3: command not found"
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3

# CentOS/RHEL
sudo yum install python3
```

### Issue: Colors not showing
- Your terminal might not support ANSI colors
- The script will still work, just without colors
- Try a different terminal (e.g., GNOME Terminal, Konsole)

### Issue: "logs directory not found"
The script creates it automatically, but if needed:
```bash
mkdir -p logs
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Test thoroughly
5. Commit: `git commit -m 'Add amazing feature'`
6. Push: `git push origin feature/amazing-feature`
7. Open a Pull Request

### Ideas for Contributions:
- Add support for more metrics (network, processes)
- Email/Slack notification integration
- Web dashboard
- Docker containerization
- CI/CD pipeline
- Multi-server monitoring

---

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ Shell scripting fundamentals
- ✅ Python for system administration
- ✅ Git version control workflow
- ✅ Error handling and validation
- ✅ Color-coded CLI output
- ✅ Command-line argument parsing
- ✅ File I/O operations
- ✅ Regular expressions and text parsing

**Perfect for DevOps beginners!**

---

## 🚀 Future Enhancements (Roadmap)

### Phase 1: Containerization 🐳
- [ ] Create Dockerfile
- [ ] Docker Compose setup
- [ ] Push to Docker Hub
- [ ] Container orchestration basics

### Phase 2: CI/CD Pipeline ⚙️
- [ ] GitHub Actions workflow
- [ ] Automated testing
- [ ] Linting and code quality checks
- [ ] Auto-deployment

### Phase 3: Advanced Monitoring 📊
- [ ] Web dashboard with Flask/FastAPI
- [ ] Real-time metrics visualization
- [ ] Historical data graphing
- [ ] Network monitoring

### Phase 4: Alerting System 🔔
- [ ] Email notifications
- [ ] Slack integration
- [ ] SMS alerts (Twilio)
- [ ] Custom webhook support

### Phase 5: Multi-Server Support 🌐
- [ ] Agent-based architecture
- [ ] Centralized log collection
- [ ] Distributed monitoring
- [ ] Cloud deployment (AWS, Azure)

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👨‍💻 Author

**Tanmay Wadurkar**
- GitHub: [@Tanmay-Wadurkar](https://github.com/Tanmay-Wadurkar)
- Project: [system-monitor](https://github.com/Tanmay-Wadurkar/system-monitor)

---

## 🆘 Support

Need help?
- 📖 Check the [Troubleshooting](#-troubleshooting) section
- 🐛 [Open an issue](https://github.com/Tanmay-Wadurkar/system-monitor/issues)
- 💬 Start a [discussion](https://github.com/Tanmay-Wadurkar/system-monitor/discussions)

---

## 🙏 Acknowledgments

Built as part of a DevOps learning journey, focusing on:
- Linux system administration
- Shell scripting automation
- Python for DevOps
- Git workflow and best practices
- CI/CD fundamentals

---

**⭐ If you find this project helpful, please consider giving it a star!**

**Happy Monitoring! 🚀**
