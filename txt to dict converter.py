lines = []
with open('tube_stop_info.txt', 'r') as file:
    for line in file:
        processed_line = line.strip()
        lines.append(processed_line)
        # Additional processing can be done here


print(lines)