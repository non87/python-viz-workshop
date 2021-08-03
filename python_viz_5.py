# In this script we will create and save a figure outside of a jupyter notebook environment

# Start with usual importing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# We load the data
# Load the data directly from the repository on github
barack_data_url = r'https://raw.githubusercontent.com/non87/python-viz-workshop/main/data/barack.csv'
barack = pd.read_csv(barack_data_url)

# Same with Ronald data
ronald_data_url = r'https://raw.githubusercontent.com/non87/python-viz-workshop/main/data/ronald.csv'
ronald = pd.read_csv(ronald_data_url)

# Show the first 5 rows of the barack data
barack.head()

# ylimit for the data
y_lim = [1, ronald['Count'].max()]
span_y = y_lim[1]- y_lim[0]
y_lim = [y_lim[0], y_lim[1] + (0.1*span_y)]
# xlimit for the data
x_lim = [ronald['Year'].min(), ronald['Year'].max()]
span_x = x_lim[1] - x_lim[0]
x_lim = [x_lim[0] - (0.05*span_x), x_lim[1] + (0.05*span_x)]

# Beginning/end of presidency as point coordinate
first_reagan_point = (1980, 0.1)
second_reagan_point = (1980, y_lim[1])
third_reagan_point = (1988, 0.1)
fourth_reagan_point = (1988, y_lim[1])
first_obama_point = (2008, 0.1)
second_obama_point = (2008, y_lim[1])

'''
Plot code
'''


# Create rectangles to be added
import matplotlib.patches as patches
rect_reagan = patches.Rectangle(xy=first_reagan_point, width=8, height=y_lim[1], color=(1,0,0,0.2),
                                label='Reagan Presidency')
rect_obama = patches.Rectangle(first_obama_point, 15, y_lim[1], color=(0,0,1,0.2), label='Obama Presidency')


'''
constrained_layout automatically adjusts subplots and decorations like legends and colorbars 
so that they fit in the figure window while still preserving, as best they can, 
the logical layout requested by the user.
'''
fig, ax = plt.subplots(nrows=2, ncols=1, figsize= (10,8), constrained_layout=True)
fig.suptitle("Obama Vs Reagan", fontsize=24)

# Obama call as in the workshop
ax[0].set_yscale('log')
ax[0].plot(barack['Year'], barack['Count'], color=(0.5, 0.5, 0.5, 0.5), linestyle='dashdot', linewidth=1.)
ax[0].plot(barack['Year'], barack['Count'], color='black', linestyle='None', marker='.', ms=10)
ax[0].set_title('The Obama Effect')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of newborns named "Obama"')
# Pass the same xlim and ylim to the axis
ax[0].set_xlim(x_lim)
ax[0].set_ylim(y_lim)
# This command draw the line. Notice the usual color, etc. to style the line as we want
ax[0].add_patch(rect_obama)

# New Ronald call
ax[1].set_yscale('log')
ax[1].plot(ronald['Year'], ronald['Count'], color=(0.5, 0.5, 0.5, 0.5), linestyle='dashdot', linewidth=1.)
ax[1].plot(ronald['Year'], ronald['Count'], color='black', linestyle='None', marker='.', ms=10)
ax[1].set_title('The Reagan Effect')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of newborns named "Ronald"')
# Pass the same xlim and ylim to the axis
ax[1].set_xlim(x_lim)
ax[1].set_ylim(y_lim)
# Draw the rectangle
ax[1].add_patch(rect_reagan)

'''
You can choose these parameters from the pop-up
'''
fig.subplots_adjust(
    top=0.89,
    bottom=0.07,
    left=0.09,
    right=0.99,
    hspace=0.305,
    wspace=0.235
)

'''
Check dimensions of the resulting file:
dpi * figure dimension
'''
fig.savefig('my_figure_at_200.png', dpi=200)
