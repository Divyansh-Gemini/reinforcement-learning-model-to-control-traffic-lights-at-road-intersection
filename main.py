import subprocess

# file names
nodesFile = 'sumo/nodes.nod.xml'
edgesFile = 'sumo/edges.edg.xml'
networkFile = 'sumo/network.net.xml'
modifyNetworkScript = 'sumo/modifyNetwork.py'
randomTripsScript = 'sumo/randomTrips.py'
tripsFile = 'sumo/trips.trips.xml'
modifyTripsScript = 'sumo/modifyTrips.py'
modifiedTripsFile = 'sumo/modified_trips.trips.xml'
routesFile = 'sumo/routes.rou.xml'
sortRandomRoutesScript = 'sumo/sortRandomRoutes.py'
configFile = 'sumo/configuration.sumocfg'
waitingTimeScript = 'sumo/waitingTime.py'

# command to generate network file (.net.xml)
netConvertCommand = f'netconvert --node-files {nodesFile} --edge-files {edgesFile} -o {networkFile} --lefthand'

# command to generate network file (.net.xml)
modifyNetworkCommand = f'python {modifyNetworkScript}'

# command to generate random trips
randomTripsCommand = f'python {randomTripsScript} -n {networkFile} -e 1000 -o {tripsFile}'

# command to modify trips (adding vehicle types & changing routes)
modifyTripsCommand = f'python {modifyTripsScript}'

# command to generate route file
duarouterCommand = f'duarouter -n {networkFile} -r {modifiedTripsFile} --ignore-errors --no-warnings --begin 0 --end 600 -o {routesFile}'

# command to randomize the interval b/w depart time of each trip
sortRandomCommand = f'python {sortRandomRoutesScript}'

# command to open simulation in SUMO
sumoGUICommand = f'sumo-gui -c {configFile}'

# command to open simulation in SUMO
getWaitingTimeCommand = f'python {waitingTimeScript}'

command = input('\nWhich command you want to execute?\n'
                ' 1. Generate network file\n'
                ' 2. Generate route file\n'
                ' 3. Open in SUMO\n'
                ' 4. Calculate waiting time\n\n>> ')

match command:
    case '1':
        subprocess.run(netConvertCommand)
        print(f'--> Generated {networkFile}')
        subprocess.run(modifyNetworkCommand)

    case '2':
        subprocess.run(randomTripsCommand)
        print(f'--> Generated random trips in using {randomTripsScript}')
        subprocess.run(modifyTripsCommand)
        subprocess.run(duarouterCommand)
        print(f'--> Generated {routesFile}')
        subprocess.run(sortRandomCommand)

    case '3':
        subprocess.run(sumoGUICommand)

    case '4':
        subprocess.run(getWaitingTimeCommand)

    case default:
        print('Invalid input')
