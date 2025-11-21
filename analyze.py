cpu = ""
memory = ""

with open("logs/report.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    if "Cpu(s)" in line:
        cpu = line
    if "Mem:" in line:
        memory = line

print("System Analysis:")
print(cpu.strip())
print(memory.strip())
