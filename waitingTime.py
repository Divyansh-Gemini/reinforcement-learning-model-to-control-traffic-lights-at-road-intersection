import xml.etree.ElementTree as ET

def calculate_avg_waiting_time(file_path):
    tree = ET.parse(file_path)
    tripinfos = tree.getroot()

    total_waiting_time = 0
    total_trips = 0

    for tripinfo in tripinfos.findall('tripinfo'):
        waiting_time = float(tripinfo.get('waitingTime'))
        total_waiting_time += waiting_time
        total_trips += 1

    avg_waiting_time = total_waiting_time / total_trips
    return avg_waiting_time

avg_waiting_time = calculate_avg_waiting_time('output/tripinfo.xml')
print(f'Average waiting time:', avg_waiting_time)