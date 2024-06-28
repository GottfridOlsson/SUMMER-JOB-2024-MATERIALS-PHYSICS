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



# LIBRARIES #
import matplotlib.pyplot as plt
import plot_functions as f
import CSV_handler as CSV
import numpy as np
import os



# FUNCTIONS #
def getRadiusFromAreaOfCircle(area):
    # given A = pi*r^2 --> r^2 = A/pi
    r = np.sqrt(area/np.pi)
    return r 

def getMicrometersPerPixel(magnification):
    # L in micrometer/px
    L = 195 / (magnification + 6.6) #mu/px
    return L

def getImagedAreaFromMagnification(magnification, pixel_area=512*512):
    A = pixel_area * (getMicrometersPerPixel(magnification))**2 # mu^2/px^2
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

def getAbsolutePathDirectoriesAndFilesInRootpath(rootpath):
    # brrowed from: https://stackoverflow.com/questions/120656/directory-tree-listing-in-python?noredirect=1&lq=1
    directory_paths, file_paths = [], []

    for dirname, dirnames, filenames in os.walk(rootpath):
        
        for subdirname in dirnames:
            directory_paths.append(os.path.join(dirname, subdirname))
        
        for filename in filenames:
            file_paths.append(os.path.join(dirname, filename))

    return directory_paths, file_paths

def isFileType(filePath, filetypeString):
    return filePath.endswith(filetypeString)





# CONSTANTS #

CSV_filetype = ".csv"


# PLOT SETTINGS #
fig_width_cm = 16
fig_height_cm = 9

font_size_axis = 13
font_size_tick = 11
font_size_legend = 9

x_label = "Particle radius / \\textmu m"
y_label = "Number of particles"

#x_lim = [np.min(x_data), np.max(x_data)]
#y_lim = [np.min(y_data), np.max(y_data)]

grid_major = True
grid_minor = False
legend_on = True

f.set_LaTeX_and_CMU(True) #must run before plotting


# ROOTPATH AND SAMPLE DIRECTORIES #
rootpath_analyzed_images = "C:\\SUMMER-JOB-2024-MATERIALS-PHYSICS\\DATA-ANALYSIS\\ImageJ\\Images for analysis\\"
samples = ["S08"]
rootpath_statistical_analyzis = "C:\\SUMMER-JOB-2024-MATERIALS-PHYSICS\\DATA-ANALYSIS\\Python\\Statistical analysis\\"


for sample in samples:
    roothpathSample = rootpath_analyzed_images + sample
    _, filePaths = getAbsolutePathDirectoriesAndFilesInRootpath(roothpathSample)

    all_radii_mu = []
    total_imagedArea_mu2 = 0
    total_numberOfParticles = 0
    numberOfFilesAnalyzed = 0


    for filePath in filePaths:
        
        fileName = extractStringBetweenStrings(filePath, "\\" + sample + "\\", ".")
        magnification = getMagnificationFromImageName(fileName)


        if isFileType(filePath, CSV_filetype):
            numberOfFilesAnalyzed = numberOfFilesAnalyzed + 1

            # Extract values
            partileAnalysisData = CSV.read(filePath) # csv from ImageJ has columns: particle number, area (px^2), mean, min, max.  Mean min and max does not mean anything relevant 
            ###partileAnalysisData = partileAnalysisData.iloc[:, :-3]   # df.iloc[row_start:row_end , col_start, col_end]
            particleNumber = partileAnalysisData.iloc[:,0]
            areas = partileAnalysisData.iloc[:,1]

            # Convert to the variables we want
            radii = getRadiusFromAreaOfCircle(areas)
            radii_mu = radii*getMicrometersPerPixel(magnification) # mu = mu/px * px
            numberOfParticles = len(areas)
            imaged_area_mu2 = getImagedAreaFromMagnification(magnification) #assuming 512 px by 512 px SEM images

            # Add to lists of data for this sample
            for radi_mu in radii_mu:
                all_radii_mu.append(radi_mu)
            total_imagedArea_mu2    = total_imagedArea_mu2    + imaged_area_mu2
            total_numberOfParticles = total_numberOfParticles + numberOfParticles

    N = total_numberOfParticles / total_imagedArea_mu2
    # Export results of sample #
    CSV_data_export_path = rootpath_statistical_analyzis + sample + "_statistical-analysis-results.csv"
    CSV.print_arrays_to_CSV(CSV_data_export_path,
                            "Radii of counted particles (micrometer)", all_radii_mu,
                            "Number of images analyzed", [numberOfFilesAnalyzed],
                            "Total number of particles counted", [total_numberOfParticles],
                            "Total imaged area (micrometer squared)", [round(total_imagedArea_mu2, 7)],
                            "Areal particle density (particle per square micrometer)", [round(N, 7)],
                            print_message=True)
    
    # PLOT HISTOGRAM #
    fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(fig_width_cm/2.54, fig_height_cm/2.54), sharex=False, sharey=False)

    # Plot your data (axs.plot, .errorbar, .hist, ...)
    axs.hist(all_radii_mu) #, linewidth=1.5, linestyle='', color='k', marker='o', markersize='4.5', label='Measured data')
    #axs.plot(fit_x, fit_y, color='k', linestyle='-', label='Linear fit')

    # Settings for each axis (axs)
    f.set_font_size(axis=font_size_axis, tick=font_size_tick, legend=font_size_legend)
    f.set_axis_scale(   axs, xScale_string='linear', yScale_string='linear')
    f.set_axis_labels(  axs, x_label=x_label, y_label=y_label)
    f.set_axis_invert(  axs, x_invert=False, y_invert=False)
    #f.set_axis_limits(  axs, x_lim[0], x_lim[1], y_lim[0], y_lim[1])
    #f.set_grid(         axs, grid_major_on=grid_major, grid_major_linewidth=0.7, grid_minor_on=grid_minor, grid_minor_linewidth=0.3) # set_grid must be after set_axis_scale for some reason (at least with 'log')
    #f.set_legend(       axs, legend_on=legend_on, alpha=1.0, location='best')

    #loc = plticker.MultipleLocator(base=5) # this locator puts ticks at regular intervals determined by base
    #axs.xaxis.set_major_locator(loc)

    f.align_labels(fig)
    f.set_layout_tight(fig)
    PDF_path = rootpath_statistical_analyzis + sample + "_histogram_particle-size-distribution.pdf"
    f.export_figure_as_pdf(PDF_path)




#plt.show()
