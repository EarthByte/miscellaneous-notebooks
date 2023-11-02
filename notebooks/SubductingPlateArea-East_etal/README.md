# SubductingPlateArea-East_etal

Scripts used in East et al. (2020).

Code and data bundle can also be downloaded from [Zenodo](https://zenodo.org/):<br>
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3386429.svg)](https://doi.org/10.5281/zenodo.3386429)

## How to run these notebooks

Use conda/mamba environment

- `conda create -n subductingPlateArea-east-etal-env gplately jupyter`
- `conda activate subductingPlateArea-east-etal-env`

## Input files

These notebooks depends on some input files.

- '../Data/Global_EarthByte_230-0Ma_GK07_AREPS.rot'
- '../Data/Global_EarthByte_230-0Ma_GK07_AREPS_Coastlines.gpmlz'
- '../Data/Global_EarthByte_230-0Ma_GK07_AREPS_PlateBoundaries.gpmlz'
- '../Data/Global_EarthByte_230-0Ma_GK07_AREPS_Topology_BuildingBlocks.gpmlz'
- '../Data/StaticPolygons/Global_EarthByte_GPlates_PresentDay_StaticPlatePolygons_2015_v1.shp'

The above files have been checked into this repository. But you might want to use your own files. You may change the file paths in the notebooks accordingly.

⚠⚠⚠These notebooks also need paleo age grids. These grids can be found here https://www.earthbyte.org/webdav/ftp/Data_Collections/Muller_etal_2016_AREPS/Muller_etal_2016_AREPS_Agegrids/Muller_etal_2016_AREPS_Agegrids_v1.17/Muller_etal_2016_AREPS_v1.17_netCDF.zip. You need to download the grids and put them in the "agegrids" folder. You can change the following line in the notebook1 to specify the location of age grids.

'agegrids/Muller_etal_2019_Tectonics_v2.0_netCDF/Muller_etal_2019_Tectonics_v2.0_AgeGrid-','.nc'

## References:

East, M., Müller, R.D., Williams, S., Zahirovic, S., Heine, C. 2020. Subduction history reveals Cretaceous slab superflux as a possible cause for the mid-Cretaceous plume pulse and superswell events. _Gondwana Research_ **79**: 125–139. doi: [10.1016/j.gr.2019.09.001](https://doi.org/10.1016/j.gr.2019.09.001).
