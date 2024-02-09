import random
import xml.etree.ElementTree as ET

def modify_trips_file(trips_file, output_file, vehicle_types, routes):
    tree = ET.parse(trips_file)
    root = tree.getroot()

    # Modify each trip element
    for trip in root.findall('trip'):
        # Remove old from and to attributes
        if "from" in trip.attrib:
            del trip.attrib["from"]
        if "to" in trip.attrib:
            del trip.attrib["to"]

        # Randomly choose vehicle type
        vehicle_type = random.choice(vehicle_types)
        trip.set('type', vehicle_type)

        # Randomly choose from and to edges from different directions
        random_route = random.choice(list(routes.keys()))
        from_edge, to_edge = routes[random_route]
        trip.set('from', from_edge)
        trip.set('to', to_edge)

    # Save the modified file
    tree.write(output_file)

# file names
trips_file = 'sumo/trips.trips.xml'
output_file = 'sumo/modified_trips.trips.xml'

# vehicle types
vehicle_types = ['car', 'bus', 'bike']

# routes
routes = {
    'routeTB': ['edgeOutTop', 'edgeInBottom'],
    'routeTR': ['edgeOutTop', 'edgeInRight'],
    'routeTL': ['edgeOutTop', 'edgeInLeft'],
    'routeBT': ['edgeOutBottom', 'edgeInTop'],
    'routeBR': ['edgeOutBottom', 'edgeInRight'],
    'routeBL': ['edgeOutBottom', 'edgeInLeft'],
    'routeRT': ['edgeOutRight', 'edgeInTop'],
    'routeRB': ['edgeOutRight', 'edgeInBottom'],
    'routeRL': ['edgeOutRight', 'edgeInLeft'],
    'routeLT': ['edgeOutLeft', 'edgeInTop'],
    'routeLB': ['edgeOutLeft', 'edgeInBottom'],
    'routeLR': ['edgeOutLeft', 'edgeInRight'],
}

modify_trips_file(trips_file, output_file, vehicle_types, routes)

print(f'--> Added random vehicle types & routes in {output_file}')