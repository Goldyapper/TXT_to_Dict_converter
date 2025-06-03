import json

lines = {}
with open('tube_stop_info.txt', 'r') as file:
    for line in file:
        parts = line.strip().split(' ', 1)
        if len(parts) == 2:
            code, name = parts
            name = name.replace(' Underground Station', '')
            lines[name] = code

print(json.dumps(lines,indent=1))

