##====================================================================##
##     Project: SUMMER JOB 2024 MATERIALS PHYSICS
##        File: positions-of-SEM-image-sampling-coordinates-calculator
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
def find_circle_center_and_radius_from_ABCD(A, B, C, D, view_fit=False):
    # A, B, C, D are tuples (x_i, y_i) of the coordinates of the SEM
    # taken at the theta=0, theta=90deg, theta=180deg, and theta=270deg of the Li deposition circle
    # This function returns the radius and the coordinates (x,y) of the center of the deposition circle
    data = [[A[0], A[1]],
            [B[0], B[1]],
            [C[0], C[1]],
            [D[0], D[1]]]
    # fit circle equation to four points
    x_center_fit, y_center_fit, r_fit, sigma_residual_fit = circle_fit.least_squares_circle(data)
    if view_fit:
        circle_fit.plot_data_circle(data, x_center_fit, y_center_fit, r_fit)
    return  x_center_fit, y_center_fit, r_fit, sigma_residual_fit
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
def calculate_3_by_3_matrix_of_squares_from_center_coordinates(x_center, y_center, distance_between_squares, n_decimals=3):
    d = distance_between_squares
    x0 = x_center
    y0 = y_center

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
            
            center_position_square_ij = (round(x0+deltaX, n_decimals), round(y0+deltaY, n_decimals))
            xy_coordinates_3_by_3_matrix_squares_numbers.append(center_position_square_ij)

    return xy_coordinates_3_by_3_matrix_squares_numbers



# MEASURED VALUES OF POINTS AND CIRCLE FIT #

A=(-10, 0)
B=(0.3, -10)
C=(-20, -10.3)
D=(-10, -20.7)

distance_between_SEM_images = 1 # mm, say we want to have this distance (cartesian) between each square in the sampled matrix on the Cu
include_AI_squares = True
view_circle_fit = True


# Circle fit
x_center_fit, y_center_fit, r_fit, sigma_residual_fit = find_circle_center_and_radius_from_ABCD(A, B, C, D, view_circle_fit)
x0 = x_center_fit
y0 = y_center_fit
print(f"\nCircle with radius {r_fit:.2f} at origo: ({x0:.2f}, {y0:.2f})")
print(f"Residual error of circle fit: {sigma_residual_fit:.5f}\n")

# Plot values
r_real = 2.5 # mm (the punched Li has diameter 5 mm, or r = 2.5 mm in reality)
distance_between_squares = (r_fit/r_real) * distance_between_SEM_images # gives the same unit that r_fit is in
square_side_length = r_fit/20 #just to see the squares in the plot
distance_between_squares_AI_training = distance_between_squares/2.1 # extra images for AI-training, value arbitrarily chosen



# PLOT #
f.set_LaTeX_and_CMU(True) #must run before plotting
figure, axs = plt.subplots(1, 2, figsize=(8, 5))

add_circle_to_ax(r_fit, x0, y0, axs[0], edgecolor='black', faceolor='gray', alpha=0.5) #gray circle = area of deposited Li
    
if include_AI_squares: # Squares for SEM images to train AI (optional)
    xy_coordinates_3_by_3_matrix_squares_numbers_AI_squares = add_3_by_3_matrix_of_squares_to_ax(square_side_length, x0, y0, distance_between_squares_AI_training, axs[0], n_decimals=3, draw_numbers=0, edgecolor='k')
    for (i, x,y) in xy_coordinates_3_by_3_matrix_squares_numbers_AI_squares:
        if i==1:
            print(f"Positions for the squares for images to train AI:")
        print(f"Position {i} of 9: ({x:.3f}, {y:.3f})")

# Squares to take SEM images for analysis
xy_coordinates_3_by_3_matrix_squares_numbers = add_3_by_3_matrix_of_squares_to_ax(square_side_length, x0, y0, distance_between_squares, axs[0], n_decimals=3)
axs[1].table(xy_coordinates_3_by_3_matrix_squares_numbers, colLabels=('Square \\#', '$x$', '$y$'), fontsize=19, loc='center', edges='open', colLoc ='center', rowLoc='center', cellLoc='center')
for (i, x,y) in xy_coordinates_3_by_3_matrix_squares_numbers:
    if i==1: print(f"\nPositions for the squares for analysis of SEM images:")
    print(f"Position {i} of 9: ({x:.3f}, {y:.3f})")


## if there is a problem clearly seeing where the points A, B, C, and D is, take a point that is at the center of the Li-deposition and put that in as x0, y0 below
'''
Li_center_x = -9.85 
Li_center_y = -10.35
xy_coordinates_3_by_3_matrix_squares_numbers_test=calculate_3_by_3_matrix_of_squares_from_center_coordinates(Li_center_x, Li_center_y, distance_between_squares, n_decimals=3)
print(xy_coordinates_3_by_3_matrix_squares_numbers_test)
'''

# Axis settings
axs[0].set_aspect(1)
alpha=1.1
axs[0].set_xlim(x0-r_fit*alpha, x0+r_fit*alpha)
axs[0].set_ylim(y0-r_fit*alpha, y0+r_fit*alpha)
axs[0].set_xlabel("$x$-coordinate")
axs[0].set_ylabel("$y$-coordinate")
axs[1].axis('tight')
axs[1].axis('off')

plt.show()