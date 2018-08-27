## usage
Newest scripts from vrep remote API. The performance improved and the speed is much faster than old one.

Change the objects lists in the head of file `RobotSG*.py`

## Bugs
- when you set the while loop only one, error happens:
'''
Traceback (most recent call last):
  File "simple_object_extractor_streamV5.py", line 219, in <module>
    vrep.simxFinish(clientID)
NameError: name 'clientID' is not defined

'''
I will fixed it tomorrow.
