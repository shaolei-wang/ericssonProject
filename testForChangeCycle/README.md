The lua script is contained in the child script of turtlebot2i and referenced in External controller tutorial of Vrep.

Open roscore and vrep, then input following command in a new terminal:

$ rostopic list
/greenCycle12766
/leftMotorSpeed12766
/redCycle12766
/redCycle19940966
/rightMotorSpeed12766
/rosout
/rosout_agg
/sensorTrigger12766
/simTime12766
/tf
/yellowCycle12766

$ rostopic pub /redCycle12766 std_msgs/Float32 "data: 100.0" 
publishing and latching message. Press ctrl-C to terminate

Then check in the command line in Vrep:
> sim.getObjectHandle('redCycle')
105

> sim.getObjectSizeValues(105)
{10, 10, 0}

> sim.getObjectSizeValues(105)
{100, 100, 0}

But nothing changed in the view of the scene graph.

Plus, the robot should move when starting simulation and from the script we can change the speed of left and right wheel. But it seems this function doesnot work.

Also, we can find there are two redCycle rostopic in the list from above. After reboot the roscore, this problem could be solved.
