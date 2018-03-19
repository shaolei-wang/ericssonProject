The method for running the script is:
1. Run roscore in the terminal;
2. Run Vrep;
3. Open the scene draft_of_warehouse_ disable_other_scripts.ttt （now I
am working on the scene graph, so I disabled the other scripts in
Vrep）;
4. Run the script vrep_obst_extractor.py or you can run the simple one
get-sg-from-sim.py (only get the size and velocity of the objects). 

Note: please modify the port number if necessary when connecting with
Vrep.

Then it should work and you can get the output information from
terminal. This is the very beginning one. The scene graph and the
script need to be improved.
