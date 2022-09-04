# USGS-EarthExplorer-Download
Download satellite data from EarthExplorer (especially for Sentinel-2 data)
## Auto Batch-Download Sentinel-2 Data

### Install ```landsatxplore```
Require ```python landsatxplorer``` package. You can just install by: 
```python
pip install landsatxplore
```
This package provides an API that can download satellite data form [USGS EarthExplorer](https://earthexplorer.usgs.gov/ "link").\
However, EarthExplorer has changed the data sent to the server with POST while login. Hence, we may need to make some revision in the POST stage from the package.
1. Find "earthxplorer.py" (Usually, this file will be in "C:\Users\user\conda\Lib\site-packages\landsatxplore\earthexplorer.py"
2. In line39, 43, 44, which mentioned about "```ncform```" should be commented. And in line 46,  "```ncform```" should also be commented (See figure below).

<div align=center>
<img src="https://github.com/H-MC/USGS-EarthExplorer-Download/blob/main/Figure/CommentLine.png" width="800">
</div>

### Create .csv file 
Go to [USGS EarthExplorer](https://earthexplorer.usgs.gov/ "link"), select all the image that you would like to download, then click to export Metadata.\
Fill in your "```Export Name```", and select "```CSV```" for "```Export Format```". After a period of time, you will get a CSV file that contains all the metadata of your selection.

<div align=center>
<img src="https://github.com/H-MC/USGS-EarthExplorer-Download/blob/main/Figure/EarthExplorerCreateCSV.gif" width="800">
</div>

### Run ```Satellite-image-download.ipynb``` and download data
Before download form USGS EarthExplorer, you need to sign in with your account.\
Follow the instruction that shows up while running. Fill in the CSV file path and your Username and Password, then continue running the next cells to download satellite images.

<div align=center>
<img src="https://github.com/H-MC/USGS-EarthExplorer-Download/blob/main/Figure/operation.gif" width="800">
</div>
