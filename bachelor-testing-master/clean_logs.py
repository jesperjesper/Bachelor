#This python scripts extracts json objects from the docker compose logs 


import json
import re

log_file_path = 'logs/logs.txt'
clean_log_file_path = 'logs/clean_logs.json'

json_pattern = re.compile(r'\{.*?\}')
valid_json_objects = []

with open(log_file_path, 'r') as file:
    for line in file:
        matches = json_pattern.findall(line)
        for match in matches:
            try:
                valid_json_objects.append(json.loads(match))
            except json.JSONDecodeError:
                continue


with open(clean_log_file_path, 'w') as clean_file:

    json.dump(valid_json_objects, clean_file)
