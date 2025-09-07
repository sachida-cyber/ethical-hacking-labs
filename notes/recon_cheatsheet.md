# Log Parser for Lab Practice
with open("sample.log", "r") as file:
    logs = file.readlines()

for line in logs:
    if "ERROR" in line:
        print(line.strip())
