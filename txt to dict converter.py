import json

lines = {}
with open('tube_stop_info.txt', 'r') as file:
    for line in file:
        key, value = line.strip().split('->', 1)
        lines[key.strip()] = value.strip()

print(json.dumps(lines,indent=1))

