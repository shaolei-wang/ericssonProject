#!/usr/bin/env python

from SceneObjectExtractor1 import SceneObjectExtractor
import time
import re
from graphviz import Digraph
import math   
#import vrep

#############################################
# generate scene graph
#############################################
dot = Digraph(comment='warehouse', format='svg')
dot.node_attr['shape']='record'
dot.node('warehouse', label='warehouse')
dot.node('floor', label='{floor|size: 25.0*25.0}')
#dot.node('robot', label='robot')
#dot.node('human', label='human')
#dot.node('shelf', label='shelf')
dot.edge('warehouse','floor')
#dot.edge('floor', 'robot')
#dot.edge('floor', 'human')
#dot.edge('floor', 'shelf')
#dot.node('ShelfBody', 'ShelfBody')
#dot.node('TagShelf', 'TagShelf')

# Update rate in seconds
rate = 0.5
pi = math.pi

extractor = SceneObjectExtractor('127.0.0.1', 19997)
print('Connected to remote API server')

print('Getting scene properties (this can take a while)...') 

# Get all objects info once (for static properties)
obj_all = extractor.get_all_objects_info()

print(obj_all) 

print('Finished getting scene properties!\n')

print('Started getting scene objects from vision sensor FOV...')

ii = 0
while ii == 0:
    ii = 1
    # Get dynamic object info (pose and vel) periodically
    extractor.update_dynamic_obj_info() 
    obj_allj = []

    for i in obj_all:

        size_x = i.size[0]
        size_y = i.size[1]
        size_z = i.size[2] 
        pose_x = i.pose[0]
        pose_y = i.pose[1]
        pose_z = i.pose[2]

        node_label = '{%s|size: %.2f, %.2f, %.2f|position: %.2f, %.2f, %.2f}'%(i.name, size_x, size_y, size_z, pose_x, pose_y, pose_z)

        dot.node(i.name, label=node_label)

        #print ('testting', i, i.name)
        if re.match(r'turtlebot2i*', i.name):
            dot.edge('floor', i.name, label='on')

        elif re.match(r'Bill*', i.name):
            dot.edge('floor', i.name, label='on') 

        # if re.match(r'TagShelf*', i.name):
            #dot.edge('floor', i.name) 

        elif re.match(r'ShelfBody*', i.name):
            dot.edge('floor', i.name, label='on') 

        elif re.match(r'stairs*', i.name):
            dot.edge('floor', i.name, label='on') 

        elif re.match(r'slidingDoor*', i.name):
            dot.edge('floor', i.name, label='on') 

        elif re.match(r'DockStationBody*', i.name):
            dot.edge('floor', i.name, label='on') 

        elif re.match(r'DockStationBody*', i.name):
            dot.edge('floor', i.name, label='on') 

        elif re.match(r'ConveyorBeltBody*', i.name):
            dot.edge('floor', i.name, label='on') 

        elif re.match(r'product*', i.name):
            dot.edge('floor', i.name, label='on') 
        
        obj_allj.append(i)

        #connect every two objects only one time
        for j in obj_all:
            if j not in obj_allj:
                dx = j.pose[0] - i.pose[0]
                dy = j.pose[1] - i.pose[1]
                dire_tan = math.atan2(dy, dx) - i.ori[2]

                if (dire_tan > -pi/8) and (dire_tan < pi/8):
                    dire_label = 'right'
                elif (dire_tan >= pi/8) and (dire_tan <= 3*pi/8):
                    dire_label = 'front-right'
                elif (dire_tan > 3*pi/8) and (dire_tan < 5*pi/8):
                    dire_label = 'front'
                elif (dire_tan >= 5*pi/8) and (dire_tan <= 7*pi/8):
                    dire_label = 'front-left'
                elif (dire_tan > 7*pi/8) or (dire_tan < -7*pi/8):
                    dire_label = 'left'
                elif (dire_tan >= -7*pi/8) and (dire_tan <= -5*pi/8):
                    dire_label = 'back-left'
                elif (dire_tan > -5*pi/8) and (dire_tan < -3*pi/8):
                    dire_label = 'back'
                else:
                    dire_label = 'back-right'

                #calculate distance when object is wall, not used now
                if not re.match(r'wall*', i.name):
                    ri = math.sqrt(i.size[0]*i.size[0] + i.size[1]*i.size[1])
                    rj = math.sqrt(j.size[0]*j.size[0] + j.size[1]*j.size[1])
                    temp_ij = dx*dx + dy*dy 
                    dist_ij = math.sqrt(temp_ij) - ri - rj
                else:
                    if posi_ix < (posi_wx + size_wx/2) and posi_ix > (posi_wx - size_wx/2):
                        dis_ij = dy - size_iy - size_jy
                    elif posi_iy < (posi_wy + size_wy/2) and posi_iy > (posi_wy - size_wx/2):
                        dis_ij = dx - size_ix - size_jx
                    else:
                        temp = dx * dx + dy * dy
                        dist_ij = math.sqrt(temp - size_ix / 2 - size_jx / 2)
                
                dist_lable = 'distance = %.2f' %(dist_ij)
                edge_label = dist_lable + ' | ' + dire_label
                dot.edge(i.name, j.name, label = edge_label)
        # if re.match(r'Waypoint*', i.name):
        #         dot.edge('floor', i.name)

    # Update vision sensor info
    extractor.update_all_robots_vision_sensors_fov()


    # Get objects that are in the sensor FOV
    for robot in extractor.robot_obj_list:
        obj_list = extractor.get_objects_from_vision_sensor(robot.vision_sensor)

        # Remove the robot itself from the list
        obj_list = [i for i in obj_list if i.name!=robot.name]

        # Print detected objects of the vision sensor
        print(robot.name, robot.vision_sensor.name, obj_list)

        # all the objects supported by floor, except products, now products not on the list
        # define a new object: floor?
        L = [floor]
        assign_object = []


        while jj not in assign_object:
            if len(L) != 0:
                parent = L[0]
                L.pop(0)
                for i in obj_list:
                    dot.node(i.name, label='%s'%i.name)
                    dot.edge(parent.name, i.name, label='on')
                    L.append(i)

        for i in range(len()):
            for j in range(i, len())
                dot.edge(obj_list[i].name, obj_list[j].name, label='')

    #output scene graph as .svg file in 
    dot.render('sg_extractor/warehouse_sg.gv', view=True)

    time.sleep(rate)

# Close the connection to V-REP
extractor.close_connection()
#vrep.simxFinish(clientID)