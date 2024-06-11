##======================================================================##
##     Project: SUMMER JOB 2024 MATERIALS PHYSICS
##        File: plot_I-cell_passivation.py
##      Author: GOTTFRID OLSSON 
##     Created: 2023-05-27
##     Updated: 2024-06-11
##       About: Plot data from .txt of passivaition in the I-cell.
##======================================================================##



# LIBRARIES #
import plot_functions as f
import CSV_handler as CSV
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.ticker as plticker



# FUNCTIONS #

def shift_df_column_to_start_at_zero(df_column):
    df_column_shift_value = df_column[0]
    return df_column - df_column_shift_value


def try_get_column_from_df(df, column_name_string):
    try:
        column = df.loc[:,column_name_string]
    except:
        print("EXCEPTION: No column with name {column_name_string} (instead returns value None).")
        column = None
    return column


def get_t_V_I_error_from_Biologic_file_root_path(root_path, shift_t_to_zero=False):
    df = CSV.read(root_path, delimiter='\t') #tab separated from Biologic

    t = try_get_column_from_df(df, "time/s")
    if shift_t_to_zero:
        try:
            t = shift_df_column_to_start_at_zero(t)
        except:
            print("EXCEPTION: Could not perform shift_df_column_to_start_at_zero().")

    V = try_get_column_from_df(df, "Ewe/V")
    I = try_get_column_from_df(df, "I/mA")
    e = try_get_column_from_df(df, "error")

    return [t, V, I, e]
    

def calculate_deposited_amount_mAhcm2_from_t_I(t, I):
    # assumes data in units 'time/s' and 'current/mA' as well as an electrode area of 0.196 cm2 (Li, 5 mm diameter)
    A = 0.196       # cm2
    t_hour = t/3600 # h (hour)
    J = np.abs(I)/A # mA/cm2; abs to avoid negative capacity
    C = J*t_hour    # mAh/cm2
    return C    


def get_current_date_and_time_as_ISO8601_string():
    import datetime
    date_and_time = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
    return date_and_time



# READ CSV #
# Change these:
filename_csv = 'testdata1.csv' 
filename_pdf = 'testdata1.pdf'

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
CSV_path = CURRENT_PATH + "\\CSV\\" + filename_csv
PDF_path = CURRENT_PATH + "\\PDF\\" + filename_pdf

CSV_data   = CSV.read(CSV_path)
CSV_header = CSV.get_header(CSV_data)









# DATA ANLYSIS / CALCULATIONS #


# Select data
x_data = CSV_data[CSV_header[0]]
y_data = CSV_data[CSV_header[1]]
LSPR_peaks = x_data
concentrations = y_data
fit_x = CSV_data[CSV_header[2]]
fit_y = CSV_data[CSV_header[3]]
fit_y_oneSigma = CSV_data[CSV_header[4]]





# PLOT SETTINGS #
fig_width_cm = 16
fig_height_cm = 9

font_size_axis = 13
font_size_tick = 11
font_size_legend = 9

x_label = "$t$ \ minute"
y_label = "$I$ \ $\\textmu$A"

x_lim = [np.min(x_data), np.max(x_data)]
y_lim = [np.min(y_data), np.max(y_data)]

grid_major = True
grid_minor = False
legend_on = True

f.set_LaTeX_and_CMU(True) #must run before plotting






# PLOT # 

# Create figure on which axis lives, one axis per subplot
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(fig_width_cm/2.54, fig_height_cm/2.54), sharex=False, sharey=False)

# Plot your data (axs.plot, .errorbar, .hist, ...)
axs.plot(x_data, y_data, linewidth=1.5, linestyle='', color='k', marker='o', markersize='4.5', label='Measured data')
axs.plot(fit_x, fit_y, color='k', linestyle='-', label='Linear fit')

# Settings for each axis (axs)
f.set_font_size(axis=font_size_axis, tick=font_size_tick, legend=font_size_legend)
f.set_axis_scale(   axs, xScale_string='linear', yScale_string='linear')
f.set_axis_labels(  axs, x_label=x_label, y_label=y_label)
f.set_axis_invert(  axs, x_invert=False, y_invert=False)
f.set_axis_limits(  axs, x_lim[0], x_lim[1], y_lim[0], y_lim[1])
f.set_grid(         axs, grid_major_on=grid_major, grid_major_linewidth=0.7, grid_minor_on=grid_minor, grid_minor_linewidth=0.3) # set_grid must be after set_axis_scale for some reason (at least with 'log')
f.set_legend(       axs, legend_on=legend_on, alpha=1.0, location='best')

#loc = plticker.MultipleLocator(base=5) # this locator puts ticks at regular intervals determined by base
#axs.xaxis.set_major_locator(loc)

f.align_labels(fig)
f.set_layout_tight(fig)
f.export_figure_as_pdf(PDF_path)
plt.show()