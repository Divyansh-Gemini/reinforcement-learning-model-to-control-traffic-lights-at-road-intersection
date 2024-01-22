import subprocess

nodesFile = 'nodes.nod.xml'
edgesFile = 'edges.edg.xml'
rightSideNetworkFile = 'rightHandNetwork.net.xml'
leftSideNetworkFile = 'leftHandNetwork.net.xml'
routesFile = 'routes.rou.xml'
typesFile = 'types.type.xml'
configFile = 'configuration.sumocfg'

netConvertCommand = ('netconvert --node-files ' + nodesFile + ' --edge-files ' + edgesFile + ' -t ' + typesFile + ' -o '
                     + rightSideNetworkFile)

sumoGUICommand = 'sumo-gui -c ' + configFile

rightToLeftConvertCommand = 'netconvert -s ' + rightSideNetworkFile + ' --flip-y-axis -o ' + leftSideNetworkFile

command = input('Which command you want to execute?\n1. netconvert\n2. sumo-gui\n\n>> ')

match command:
    case '1':
        # generates .net.xml file
        subprocess.run(netConvertCommand)

        # convert .net.xml from right-hand-side to left-hand-side
        subprocess.run(rightToLeftConvertCommand)

    case '2':
        # launch SUMO GUI
        subprocess.run(sumoGUICommand)

    case default:
        print('Invalid input')
