##====================================================================##
##     Project: SUMMER JOB 2024 MATERIALS PHYSICS
##        File: positions-of-SEM-image-sampling-coordinates-calculator-from-center-point
##      Author: GOTTFRID OLSSON 
##     Created: 2024-06-10
##     Updated: 2024-06-12
##       About: Calculates positions where SEM images
##              should be taken for the sampling.
##====================================================================##



# LIBRARIES #
import circle_fit
import plot_functions as f
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle



# FUNCTIONS #
def add_rectangle_to_ax(width, height, x_pos, y_pos, ax, edgecolor='red', faceolor='none'):
    x_pos_center = x_pos - width/2
    y_pos_center = y_pos - height/2
    ax.add_patch(Rectangle((x_pos_center, y_pos_center), width, height, linewidth=1, edgecolor=edgecolor, facecolor=faceolor))
def add_square_to_ax(side_length, x_pos, y_pos, ax, edgecolor='red', faceolor='none'):
    add_rectangle_to_ax(side_length, side_length, x_pos, y_pos, ax, edgecolor=edgecolor, faceolor=faceolor)
def add_circle_to_ax(radius, x_pos, y_pos, ax, edgecolor='gray', faceolor='gray', alpha=1):
    ax.add_artist(plt.Circle((x_pos,y_pos), radius=radius, edgecolor=edgecolor, facecolor=faceolor, alpha=alpha))
def find_circle_center_and_radius_from_ABCD(points_along_circle, view_fit=False):
    # fit circle equation to four points
    x_center_fit, y_center_fit, r_fit, sigma_residual_fit = circle_fit.least_squares_circle(points_along_circle)
    if view_fit:
        circle_fit.plot_data_circle(points_along_circle, x_center_fit, y_center_fit, r_fit)
    return  x_center_fit, y_center_fit, r_fit, sigma_residual_fit
def calculate_3_by_3_matrix_of_squares_from_center_coordinates(x_center, y_center, distance_between_squares, n_decimals=3):
    d = distance_between_squares
    x0 = x_center
    y0 = y_center

    xy_coordinates_3_by_3_matrix_squares = []
    for i in range(0,3):
        if i==0: deltaY = d
        if i==1: deltaY = 0
        if i==2: deltaY = -d

        for j in range(0,3):
            if j==0: deltaX = -d
            if j==1: deltaX = 0
            if j==2: deltaX = d
            
            center_position_square_ij = (round(x0+deltaX, n_decimals), round(y0+deltaY, n_decimals))
            xy_coordinates_3_by_3_matrix_squares.append(center_position_square_ij)

    return xy_coordinates_3_by_3_matrix_squares
def add_3_by_3_matrix_of_squares_to_ax(square_side_length, x0_matrix, y0_matrix, distance_between_squares, ax, n_decimals=3, draw_numbers=True, edgecolor='red', faceolor='none'):
    a = square_side_length
    d = distance_between_squares
    x0 = x0_matrix
    y0 = y0_matrix

    xy_coordinates_3_by_3_matrix_squares_numbers = []

    counter = 1
    for i in range(0,3):
        if i==0: deltaY = d
        if i==1: deltaY = 0
        if i==2: deltaY = -d

        for j in range(0,3):
            if j==0: deltaX = -d
            if j==1: deltaX = 0
            if j==2: deltaX = d
            add_square_to_ax(square_side_length, x0+deltaX, y0+deltaY, ax, edgecolor=edgecolor, faceolor=faceolor)
            if draw_numbers:
                ax.text(x0+deltaX, y0+deltaY+a*1.1/2, str(counter), horizontalalignment='center')
            xy_coordinates_3_by_3_matrix_squares_numbers.append((counter, round(x0+deltaX, n_decimals), round(y0+deltaY, n_decimals)))
            counter = counter + 1
        
    return xy_coordinates_3_by_3_matrix_squares_numbers
def calculate_4_by_4_matrix_of_square_from_center_coordinates(x_center, y_center, distance_between_squares, n_decimals=3):
    d = distance_between_squares
    x0 = x_center
    y0 = y_center

    xy_coordinates_4_by_4_matrix_squares = []

    for i in range(0, 4):
        if i==0: deltaY =  3*d/2
        if i==1: deltaY =  1*d/2
        if i==2: deltaY = -1*d/2
        if i==3: deltaY = -3*d/2
        
        for j in range(0, 4):
            if j==0: deltaX = -3*d/2
            if j==1: deltaX = -1*d/2
            if j==2: deltaX =  1*d/2
            if j==3: deltaX =  3*d/2
            
            center_position_square_ij = (round(x0+deltaX, n_decimals), round(y0+deltaY, n_decimals))
            xy_coordinates_4_by_4_matrix_squares.append(center_position_square_ij)

    return xy_coordinates_4_by_4_matrix_squares
def add_4_by_4_matrix_of_squares_to_ax(square_side_length, x0_matrix, y0_matrix, distance_between_squares, ax, n_decimals=3, draw_numbers=True, edgecolor='red', faceolor='none'):
    xy_coordinates_4_by_4_matrix_squares = calculate_4_by_4_matrix_of_square_from_center_coordinates(x0_matrix, y0_matrix, distance_between_squares, n_decimals=n_decimals)

    xy_coordinates_4_by_4_matrix_squares_numbers = []
    for i in range(0, 16):
        add_square_to_ax(square_side_length, xy_coordinates_4_by_4_matrix_squares[i][0], xy_coordinates_4_by_4_matrix_squares[i][1], ax, edgecolor=edgecolor, faceolor=faceolor)
        if draw_numbers:
            ax.text(xy_coordinates_4_by_4_matrix_squares[i][0], xy_coordinates_4_by_4_matrix_squares[i][1]+square_side_length*1.1/2, str(i+1), horizontalalignment='center')
            xy_coordinates_4_by_4_matrix_squares_numbers.append((i+1, round(xy_coordinates_4_by_4_matrix_squares[i][0], n_decimals), round(xy_coordinates_4_by_4_matrix_squares[i][1], n_decimals)))

    return xy_coordinates_4_by_4_matrix_squares_numbers
def get_current_date_and_time_as_ISO8601_string():
    import datetime
    date_and_time = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
    return date_and_time



# SEM-COORDINATES OF THE CENTER OF LI DEPOSITION #
x0 = 1 #mm 
y0 = 1  #mm
r_Li = 2.5 #mm
distance_between_SEM_images = 1 # mm, distance (x or y) between each square in the sampled grid on the Cu
square_side_length = distance_between_SEM_images/3


# PLOT #
f.set_LaTeX_and_CMU(True) #must run before plotting
figure, axs = plt.subplots(1, 2, figsize=(8, 5))
add_circle_to_ax(r_Li, x0, y0, axs[0], edgecolor='black', faceolor='gray', alpha=0.5) #gray circle = area of deposited Li
    
# Squares to take SEM images for analysis
xy_coordinates_3_by_3_matrix_squares_numbers = add_3_by_3_matrix_of_squares_to_ax(square_side_length, x0, y0, distance_between_SEM_images, axs[0], n_decimals=3)
axs[1].table(xy_coordinates_3_by_3_matrix_squares_numbers, colLabels=('Square \\#', '$x$', '$y$'), fontsize=19, loc='center', edges='open', colLoc ='center', rowLoc='center', cellLoc='center')
for (i, x, y) in xy_coordinates_3_by_3_matrix_squares_numbers:
    if i==1: print(f"\nPositions for the squares for analysis of SEM images (x, y):")
    print(f"Position {i} of 9: ({x:.3f}, {y:.3f})")

# Axis settings
axs[0].set_aspect(1)
alpha = 1.1
axs[0].set_xlim(x0-r_Li*alpha, x0+r_Li*alpha)
axs[0].set_ylim(y0-r_Li*alpha, y0+r_Li*alpha)
axs[0].set_xlabel("$x$-coordinate")
axs[0].set_ylabel("$y$-coordinate")
axs[1].axis('tight')
axs[1].axis('off')


# Print relative coordinate changes
print(f"\nFor center ({x0:.3f}, {y0:.3f}) of 3x3 grid with spacing {distance_between_SEM_images:.2f}, relative coordinates from previous point:")
print(f"Point 5 of 9: no change to coordinates; ({x0:.3f}, {y0:.3f})")
print(f"Point 6 of 9:   x+{distance_between_SEM_images:.2f};    ({x0+distance_between_SEM_images:.3f}, {y0:.3f})")
print(f"Point 3 of 9:   y+{distance_between_SEM_images:.2f};    ({x0+distance_between_SEM_images:.3f}, {y0+distance_between_SEM_images:.3f})")
print(f"Point 2 of 9:   x-{distance_between_SEM_images:.2f};    ({x0:.3f}, {y0+distance_between_SEM_images:.3f})")
print(f"Point 1 of 9:   x-{distance_between_SEM_images:.2f};    ({x0-distance_between_SEM_images:.3f}, {y0+distance_between_SEM_images:.3f})")
print(f"Point 4 of 9:   y-{distance_between_SEM_images:.2f};    ({x0-distance_between_SEM_images:.3f}, {y0:.3f})")
print(f"Point 7 of 9:   y-{distance_between_SEM_images:.2f};    ({x0-distance_between_SEM_images:.3f}, {y0-distance_between_SEM_images:.3f})")
print(f"Point 8 of 9:   x+{distance_between_SEM_images:.2f};    ({x0:.3f}, {y0-distance_between_SEM_images:.3f})")
print(f"Point 9 of 9:   x+{distance_between_SEM_images:.2f};    ({x0+distance_between_SEM_images:.3f}, {y0-distance_between_SEM_images:.3f})")




if False:
    f.export_figure_as_pdf("C:\\SUMMER-JOB-2024-MATERIALS-PHYSICS\\PYTHON\\Example_positions_SEM-images-for-analysis_on-Cu-surface_" + get_current_date_and_time_as_ISO8601_string() +".pdf")
plt.show()