import xml.etree.ElementTree as ET
import random

tree = ET.parse('sumo/routes.rou.xml')
root = tree.getroot()

# Sort vehicles by depart time
vehicles = root.findall('.//vehicle')
vehicles.sort(key=lambda x: float(x.get('depart')))

current_departure = 0

for vehicle in vehicles:
    # Generate a random departure interval between 5 & 10 seconds
    random_interval = random.uniform(5, 10)
    
    # Update the departure time with the interval
    current_departure += random_interval

    # Set the updated departure time for the current vehicle
    vehicle.set('depart', str(current_departure))

# Save the modified routes file
tree.write('sumo/sorted_random_route.rou.xml')
print(f'--> Increased time interval b/w depart time of each vehicle.')