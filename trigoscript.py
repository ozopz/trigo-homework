#!/bin/python3
import json
import requests
ip_addresses = requests.get('http://172.19.0.3:1337/inventory')
config = {
        "labels": {"job" : "node"},
        "targets": []
}
for ip in ip_addresses:
    config["targets"].append(ip)

combined_targets = ''.join([target.decode('utf-8') for target in config['targets']])

sensor_list = json.loads(combined_targets)

config['targets'] = sensor_list
output_data = [config] #formatting for json
json_config = json.dumps(output_data, indent=4)

with open('targets.json', 'w') as file:
    file.write(json_config)

