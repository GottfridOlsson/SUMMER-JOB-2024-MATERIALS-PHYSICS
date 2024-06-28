##===============================================##
##     Project: SUMMER-JOB-2024-MATERIALS-PHYSICS
##        File: SEM-images-statistical-analysis.py
##      Author: GOTTFRID OLSSON 
##     Created: 2024-06-28
##     Updated: 2024-06-28
##       About: Analyze:
##              1) # particles per area, and
##              2) size distribution particles.
##===============================================##


import CSV_handler as CSV
import numpy as np


def getAreaFromMagnification(magnification):
    # equation derived, see logbooks
    A = (99840 / (magnification + 6.6))**2
    return A

def getMagnificationFromImageName(imageName):
    # split at '_X' and keep left part
    # split at '_'  and keep right part
    magnification = extractStringBetweenStrings(imageName, '_X', '_')
    return int(magnification)


def extractStringBetweenStrings(main_string, start_string, end_string):
    start_index = main_string.find(start_string)
    if start_index == -1:
        return None
    start_index += len(start_string)
    
    end_index = main_string.find(end_string, start_index)
    if end_index == -1:
        return None
    
    return main_string[start_index:end_index]




rootpath_analyzed_images = "C:\\SUMMER-JOB-2024-MATERIALS-PHYSICS\\DATA-ANALYSIS\\ImageJ\\Images for analysis\\"
samples = ["S08"]



for sample in samples:
    roothpath_sample = rootpath_analyzed_images + sample + "\\"
    print(roothpath_sample)


