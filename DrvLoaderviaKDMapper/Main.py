import os
import pathlib
import sys
def LoadDrvViaKDMapper(drv_name : str):
    kdmap = str('kdmapper.exe')
    if pathlib.Path(os.getcwd() + "\\{}".format(kdmap)).is_file():
        os.system('{} {}.sys'.format(kdmap, drv_name))
    else:
        print("Failed to Found Kdmapper.exe File for Loading Drv... Pls Install KDMapper!!!")
        os._exit(122)

if __name__ == "__main__":
    LoadDrvViaKDMapper("example.sys")