##====================================================================##
##     Project: SUMMER JOB 2024 MATERIALS PHYSICS
##        File: positions-of-SEM-image-sampling-coordinates-calculator
##      Author: GOTTFRID OLSSON 
##     Created: 2024-06-10
##     Updated: 2024-06-10
##       About: Calculates positions where SEM images
##              should be taken for the sampling.
##====================================================================##


import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import circle_fit
import plot_functions as f

f.set_LaTeX_and_CMU(True) #must run before plotting

# VARIABLES #
alpha = 1.05


# FUNCTIONS #
def add_rectangle_to_ax(width, height, x_pos, y_pos, ax):
    x_pos_center = x_pos - width/2
    y_pos_center = y_pos - height/2
    ax.add_patch(Rectangle((x_pos_center, y_pos_center), width, height, linewidth=1, edgecolor='r', facecolor='none'))

def add_square_to_ax(side_length, x_pos, y_pos, ax):
    add_rectangle_to_ax(side_length, side_length, x_pos, y_pos, ax)

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
    print(f"\nResidual error of circle fit: {sigma_residual_fit}")
    if view_fit:
        circle_fit.plot_data_circle(data, x_center_fit, y_center_fit, r_fit)
    return  x_center_fit, y_center_fit, r_fit, sigma_residual_fit

def add_3_by_3_matrix_of_squares_to_ax(square_side_length, x0_matrix, y0_matrix, distance_between_squares, ax):
    a = square_side_length
    d = distance_between_squares
    b = a + d
    x0 = x0_matrix
    y0 = y0_matrix

    xy_coordinates_3_by_3_matrix_squares_numbers = []

    counter = 1
    for i in range(0,3):
        if i==0: deltaY = b
        if i==1: deltaY = 0
        if i==2: deltaY = -b

        for j in range(0,3):
            if j==0: deltaX = -b
            if j==1: deltaX = 0
            if j==2: deltaX = b
            add_square_to_ax(square_side_length, x0+deltaX, y0+deltaY, ax)
            ax.text(x0+deltaX, y0+deltaY+a*1.1/2, str(counter), horizontalalignment='center')
            xy_coordinates_3_by_3_matrix_squares_numbers.append((counter, x0+deltaX, y0+deltaY))
            counter = counter + 1
        
    return xy_coordinates_3_by_3_matrix_squares_numbers
        




# MEASURED VALUES OF POINTS AND CIRCLE FIT #

A=(10, 0)
B=(0, 10)
C=(-10, 0)
D=(0, -10)

x_center_fit, y_center_fit, r_fit, sigma_residual_fit = find_circle_center_and_radius_from_ABCD(A, B, C, D, view_fit=True)
x0 = x_center_fit
y0 = y_center_fit
print(f"Circle origo: ({x0:.2f}, {y0:.2f})\n")

r_real = 2.5 # mm (the punched Li has diameter 5 mm, or r = 2.5 mm in reality)
xAndy_distance_between_SEM_images = 1 # mm, say we want to have this distance (cartesian) between each square in the sampled matrix on the Cu
distance_between_squares = (r_fit/r_real) * xAndy_distance_between_SEM_images # gives the same unit that r_fit is in
square_side_length = r_fit/10



# PLOT #
figure, axs = plt.subplots(1, 2, figsize=(8, 5))
add_circle_to_ax(r_fit, x0, y0, axs[0], edgecolor='black', faceolor='gray', alpha=0.6)
xy_coordinates_3_by_3_matrix_squares_numbers = add_3_by_3_matrix_of_squares_to_ax(square_side_length, x0, y0, distance_between_squares, axs[0])
for (i, x,y) in xy_coordinates_3_by_3_matrix_squares_numbers:
    print(f"Position {i} of 9: ({x:.2f}, {y:.2f})")


axs[0].set_aspect(1)
axs[0].set_xlim(-alpha*r_fit, alpha*r_fit)
axs[0].set_ylim(-alpha*r_fit, alpha*r_fit)
axs[0].set_xlabel("$x$")
axs[0].set_ylabel("$y$")
#ax.axis('off')

axs[1].axis('tight')
axs[1].axis('off')
the_table = axs[1].table(xy_coordinates_3_by_3_matrix_squares_numbers, colLabels=('Square \\#', '$x$', '$y$'), fontsize=19, loc='center', edges='open', colLoc ='center', rowLoc='center', cellLoc='center')

plt.show()