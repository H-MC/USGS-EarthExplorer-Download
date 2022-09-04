import os
import zipfile
import landsatxplore
from landsatxplore.earthexplorer import EarthExplorer
from retry import retry



@retry(tries=3, delay=5)
def S2_download(username, 
                password, 
                EntityID,
                OUTPUT_DIR, 
                EXTRACT=False):
    """
    Download Sentinel-2 data from USGS EarthExplorer. ("https://earthexplorer.usgs.gov/")
    This needs the USGS account. You can create the account from "https://ers.cr.usgs.gov/login".
    username: your USGS username.
    password: your USGS password.
    EntityID: the ID of the Sentinel-2 image. 
    OUTPUT_DIR: the directory that the downloaded image should be saved.
    EXTRACT: extract the zip file or not. It will be extracted to the same directory.

    This requires downloading and importing the EarthExplorer package.
    You can find it as a Python package at "https://github.com/yannforget/landsatxplore". 
    But something needs to revise at 'landsatxplore\earthexplorer.py'. In line 39,43,44, they have 
    to be deleted. In line 46, 'ncform' also have to be deleted.
    
    Each download will be attempted {TRY_TIME} times with a 5s delay between 2 attempts.
    If it is still invalid after {TRY_TIME} times, it will give up.

    by M.C. Hsieh. May,20 2022.
    """
    
    ee = EarthExplorer(username, password)
    ee.download(EntityID, output_dir=OUTPUT_DIR)
    
    # Extract image
    if EXTRACT:
        zipped_file = f'{EntityID}.zip'
        try:
            zipped_filepath = os.path.join(OUTPUT_DIR, zipped_file)
            with zipfile.ZipFile(zipped_filepath, 'r') as unzip:
                unzip.extractall(path=OUTPUT_DIR)
            print(f'{EntityID} extract completed')

        except: 
            print(f'{EntityID} extract failed')
    else:
        print(f'{EntityID} download completed')
    # ee.logout()
    
    
    