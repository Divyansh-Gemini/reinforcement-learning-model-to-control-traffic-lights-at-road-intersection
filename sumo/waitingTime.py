import xml.etree.ElementTree as ET

def calculate_avg_waiting_time(file_path):
    tree = ET.parse(file_path)
    tripinfos = tree.getroot()

    total_waiting_time = 0
    total_trips = 0

    # calculate sum of waiting time of each vehicle & count total no. of vehicles
    for tripinfo in tripinfos.findall('tripinfo'):
        waiting_time = float(tripinfo.get('waitingTime'))
        total_waiting_time += waiting_time
        total_trips += 1

    # calculate average waiting time
    avg_waiting_time = total_waiting_time / total_trips if total_trips else 0
    return avg_waiting_time

avg_waiting_time = calculate_avg_waiting_time('sumo/output/tripinfo.xml')
print('Average waiting time:', avg_waiting_time)