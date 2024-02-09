import subprocess

# file names
nodesFile = 'nodes.nod.xml'
edgesFile = 'edges.edg.xml'
networkFile = 'network.net.xml'
routesFile = 'routes.rou.xml'
typesFile = 'types.type.xml'
configFile = 'configuration.sumocfg'

# command to generate network file (.net.xml)
netConvertCommand = ('netconvert --node-files ' + nodesFile + ' --edge-files ' + edgesFile + ' -t ' + typesFile + ' -o '
                     + networkFile + ' --lefthand')

# command to open simulation in SUMO
sumoGUICommand = 'sumo-gui -c ' + configFile

command = input('Which command you want to execute?\n1. netconvert\n2. sumo-gui\n>> ')

match command:
    case '1':
        subprocess.run(netConvertCommand)

    case '2':
        subprocess.run(sumoGUICommand)

    case default:
        print('Invalid input')
