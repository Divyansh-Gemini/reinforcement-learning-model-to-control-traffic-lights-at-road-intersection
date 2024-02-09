import subprocess

# file names
nodesFile = 'nodes.nod.xml'
edgesFile = 'edges.edg.xml'
networkFile = 'network.net.xml'
randomTripsScript = 'randomTrips.py'
tripsFile = 'trips.trips.xml'
modifyTripsScript = 'modifyTrips.py'
modifiedTripsFile = 'modified_trips.trips.xml'
routesFile = 'routes.rou.xml'
sortRandomRoutesScript = 'sortRandomRoutes.py'
configFile = 'configuration.sumocfg'

# command to generate network file (.net.xml)
netConvertCommand = f'netconvert --node-files {nodesFile} --edge-files {edgesFile} -o {networkFile} --lefthand'

# generate random trips
randomTripsCommand = f'python {randomTripsScript} -n {networkFile} -e 1000 -o {tripsFile}'

# modify trips
modifyTripsCommand = f'python {modifyTripsScript}'

# generate .rou.xml file
duarouterCommand = f'duarouter -n {networkFile} -r {modifiedTripsFile} --ignore-errors --no-warnings --begin 0 --end 600 -o {routesFile}'

# sort random routes
sortRandomCommand = f'python {sortRandomRoutesScript}'

# command to open simulation in SUMO
sumoGUICommand = f'sumo-gui -c {configFile}'

command = input('Which command you want to execute?\n1. Generate network file\n2. Generate route file\n3. Open in SUMO\n>> ')

match command:
    case '1':
        subprocess.run(netConvertCommand)

    case '2':
        subprocess.run(randomTripsCommand)
        subprocess.run(modifyTripsCommand)
        subprocess.run(duarouterCommand)
        subprocess.run(sortRandomCommand)

    case '3':
        subprocess.run(sumoGUICommand)

    case default:
        print('Invalid input')
