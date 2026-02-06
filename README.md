# 🖥️ System Monitor

A Linux system monitoring tool built with Shell Scripting and Python. Monitors CPU, memory, and disk usage with intelligent analysis and alerts.

[![Linux](https://img.shields.io/badge/Platform-Linux-blue.svg)](https://www.linux.org/)
[![Shell Script](https://img.shields.io/badge/Shell-Bash-green.svg)](https://www.gnu.org/software/bash/)
[![Python](https://img.shields.io/badge/Python-3.x-yellow.svg)](https://www.python.org/)

---

## ✨ Features

- 🖥️ **CPU Monitoring** - Real-time CPU usage with idle/active analysis
- 💾 **Memory Tracking** - RAM usage with threshold alerts
- 💿 **Disk Analysis** - Filesystem usage across partitions
- 📊 **Process Monitoring** - Top CPU and memory-consuming processes
- 🚨 **Smart Alerts** - Color-coded warnings for resource usage
- 📝 **Timestamped Reports** - Historical tracking with dated logs
- 🎨 **Color-Coded Output** - Easy-to-read terminal interface

---

## 📋 Prerequisites

- **OS**: Linux (Ubuntu, Debian, CentOS, etc.)
- **Shell**: Bash 4.0+
- **Python**: 3.6 or higher
- **System Tools**: `top`, `free`, `df`, `ps` (usually pre-installed)

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Tanmay-Wadurkar/system-monitor.git
cd system-monitor
```

### 2. Run Setup
```bash
chmod +x setup.sh
./setup.sh
```

### 3. Start Monitoring
```bash
./monitor.sh
```

---

## 📁 Project Structure

```
system-monitor/
├── monitor.sh          # Main monitoring script
├── analyze.py          # Python analysis module
├── setup.sh            # Environment setup script
├── .gitignore          # Git ignore rules
├── README.md           # This file
└── logs/               # Generated reports directory
    └── report_*.txt    # Timestamped reports
```

---

## 📊 Sample Output

```
===========================================
           SYSTEM ANALYSIS REPORT
===========================================

🖥️  CPU USAGE:
   %Cpu(s):  12.5 us,  3.2 sy,  0.0 ni, 84.3 id
   ✓ Normal CPU usage (15.7%)

💾 MEMORY USAGE:
   Total: 15.6Gi
   Used:  8.2Gi
   ✓ Normal memory usage (52.6%)

💿 DISK USAGE (Root Partition):
   Filesystem: /dev/sda1
   Size: 250G | Used: 145G | Available: 93G
   ⚡ Moderate disk usage (58%)

===========================================
```

---

## 🛠️ Usage

### Basic Monitoring
```bash
./monitor.sh
```

### View Latest Report
```bash
cat logs/latest_report.txt
```

### Run Analysis on Specific Report
```bash
python3 analyze.py logs/report_20240207_143022.txt
```

---

## 📈 Upgrade Roadmap

This project is being upgraded in phases to incorporate DevOps best practices:

### ✅ Phase 1: Foundation (Current)
- [x] Enhanced shell scripting with error handling
- [x] Improved Python analysis with color output
- [x] Timestamped logging
- [x] Setup automation
- [x] Git best practices (.gitignore)

### 🔄 Phase 2: Enhanced Monitoring (Next)
- [ ] Alert threshold configuration
- [ ] Email/Slack notifications
- [ ] Log rotation and cleanup
- [ ] Configuration file support

### 🐳 Phase 3: Dockerization
- [ ] Dockerfile creation
- [ ] Docker Compose setup
- [ ] Volume management
- [ ] Multi-container architecture

### ⚙️ Phase 4: Automation
- [ ] Cron job integration
- [ ] Automated scheduling
- [ ] Health check endpoints
- [ ] Dashboard (web interface)

### 🚀 Phase 5: CI/CD
- [ ] GitHub Actions workflow
- [ ] Automated testing
- [ ] Docker Hub integration
- [ ] Auto-deployment

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👨‍💻 Author

**Tanmay Wadurkar**
- GitHub: [@Tanmay-Wadurkar](https://github.com/Tanmay-Wadurkar)

---

## 🆘 Support

If you encounter any issues or have questions:
- Open an issue: [GitHub Issues](https://github.com/Tanmay-Wadurkar/system-monitor/issues)
- Check existing documentation in this README

---

## 🙏 Acknowledgments

Built as part of a DevOps learning journey, focusing on:
- Shell scripting fundamentals
- Python automation
- Docker containerization
- CI/CD pipelines
- Git workflow best practices

---

**⭐ If you find this project helpful, please consider giving it a star!**
