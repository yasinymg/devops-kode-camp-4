import os
import sys
#define create folder
def create_folder():
    print("\nExecuting create_folder() function...\n")

    #create variable to hold get version return value
    vid = get_version()

    #check if 3 is in the return of get_version
    if "3" in vid:
        os.mkdir("kc4_osFolder-%s"%vid)

