title: matplotlib polar clock line plot
date: 2019-02-14
description: functional Python code for generating a matplotlib polar clock line plot 
tags: python, matplotlib, time series, polar, cyclic

### When plotting a line with a time (24 hour) cycle across the x-axis like...
![timeseries_lineplot]({filename}/images/timeseries_lineplot.svg)
...a polar plot that cycles back onto itself like a clock makes a lot more sense.

Below is a simple example with subplots. The data here is downsampled into hours, so a binned histogram would be fine, but a line plot is utilized here to increase sense of area-under-the-curve and relationship between points. Ideally, this could be generalized to much smaller binned time increments that might otherwise be too fine for histograms. For that, the tick axis should be intelligently redesigned with `matplotlib.dates`
![polarplot_timeseries]({filename}/images/total_time_polar_plots.svg)

```python
data = [time_data.n_stops, time_data.n_searches] #see https://github.com/ACiDS-NU/nu_open_policing/blob/master/Visualization%20of%20IL%20Highway%20Policing%20Data.ipynb
colors = ['#32CD32', '#1D951B']
super_title = 'Illinois Traffic Policing Data (2004-2015)'
titles = ['Total Traffic Stops vs Time of Day', 
          'Total Searches (after Stop) vs Time of Day']


def polar_time_lineplot(dat, colr, titl, super_title, nrow, ncol, num_tick=8):
    """
    Creates a series of polar subplots to mimic a 24-hour clock (cyles back onto itself)
    dat -> list of y-data (can be list of arrays, Series, etc.)
    colr -> list of colors (should be same length as number of data arrays)
    titl -> list of titles (should be same length as number of data arrays)
    super_title -> title to go above subplots (describe data source, for ex.)
    nrow, ncol -> dimensions of subplots, (nrow) x (ncol) <= len(dat)
    """
    fig, axs = plt.subplots(nrow, ncol, 
                            figsize = (14, 8), subplot_kw=dict(projection='polar'))
    for i, ax in enumerate(fig.axes):
        # 'radian' array for time segements
        theta = np.linspace(0, 2 * np.pi, len(dat[i])+1)
        # duplicate startpt for line continuous w/ endpt
        dat[i] = dat[i].append(pd.Series(dat[i][0]))
        # plot
        ax.plot(theta, dat[i], linewidth=5.0, color=colr[i], alpha=0.6)
        # Polar clock formating
        ax.set_theta_zero_location("N") #0:00 at top ('north')
        ax.set_theta_direction(-1) #clockwise polarity
        ticks = [str(int(hr)) + ':00' for hr in np.linspace(0,24,hr_tick_int+1)][:-1]
        ax.set_xticklabels(ticks) #more elegant solution might use matplotlib.dates
        # General formatting
        ax.yaxis.get_major_formatter().set_powerlimits((-2,4))
        ax.get_yaxis().get_offset_text().set_position([0.75, 0]) # hard-coded, not smart
        ax.set_title(titl[i])

    fig.tight_layout(h_pad=1)
    fig.suptitle(super_title)
    plt.show()
    
polar_time_lineplot(data, colors, titles, super_title, 1, 2)
```
