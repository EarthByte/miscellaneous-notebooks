This file contains guidelines for running the ipython notebooks in this folder, which relate to the East et. al. submission to Gondwana Research:

'Subduction history reveals Cretaceous slab superflux as a possible cause for the mid-Cretaceous plume pulse and superswell events'

# this file was created by Madison East 16/5/19

There are 3 ipython notebooks in this folder. Below outlines what order to run them in and what they will do. Note that you will need to have installed pyGPlates.

1. 'Make-Subduction-Stats-Table-notebook1.ipynb' 
	RUN ME FIRST!
	This notebook extracts the raw data we need from the selected plate model. This is done by sampling along the subduction zones at various time steps and extracting parameters such as arc length, convergence rate and the age of the subducting seafloor. You will need the following files to run the notebook:
	
	- subduction_convergence.py
	- For the chosen plate model you will need the rotation file (.rot), the 'PlateBoundaries' and 'Topology_BuildingBlocks' files (.gpml format), the 'PresentDay_StaticPlatePolygons' shape file (.shp), and seafloor agegrids (.grd) 

	At the end of the notebook you are directed to save the generated data as a .csv file. This will be used as an input for the second notebook.

2. 'Calc-Subduction-Stats-Volume-Area-notebook2.ipynb'
	TIME TO CALCULATE AREA (subducting plate area) AND VOLUME (slab flux)!
	This notebook takes all the data generated in the first notebook and calcualtes the area and volume flux at each subduction segment for each time step. It allows you to visualise this result, and then at the end of the notebook, calcuates the total area and volume flux at each time step from 0 to 230 Ma. 
	You will need the following files:

	- topology_plotting.py
	- lithosphere_thickness_plate_model.py
	- And again you will need certain files from the chosen plate model

3. 'Visualise-Slab-Flux-Subducting-Area-notebook3.ipynb'
	This notebook take us to the fun part of plotting and playing with the data.