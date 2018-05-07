# Get Scene Graph from V-Rep simulator

This project is try to get scene graph of warehouse from V-Rep simulator. 

## V-Rep file
This file `2warehouse_turtlebot2i_paper.ttt` is the simulation file and please open it with V-Rep. And when you run the python scripts to test the scene graph generation. Starting simulation in V-Rep is **NOT necessary**.

## Original files
The file `SceneObjectExtractor.py` and `simple_object_extractor.py` is the original files without change.


## Working files
The file `simple_object_extractor1.py` can run and the result is a really complex picture (svg). **All the nodes** are connected with each other.

The file `simple_object_extractor2.py` add the algorithm 1 from paper On Support Relations and Semantic Scene Graphs. But it isn't finished and there are some bugs need to be fixed.

Both the files above two with modified import the python class from `SceneObjectExtractor`**1**`.py`, not `SceneObjectExtractor.py`.
                   


