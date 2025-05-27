import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
from functools import partial
import numpy as np

def plot_field(
        ax,
        x,
        y,
        z,
        title,
        cmap,
        norm,
        levels,
        pos_ticks,
        ticks,
        extend,
        drone_pos,
        drone_color,
        font_size):
    im = ax.contourf(x, y, z, cmap=cmap, norm=norm, levels=levels)
    ax.scatter(*drone_pos, c=drone_color)
    sm = cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, extend=extend, ax=ax)
    cbar.set_ticks(ticks)
    cbar.ax.tick_params(labelsize=font_size)
    ax.set_title(title, fontsize=font_size)
    ax.set_xlabel("x", fontsize=font_size)
    ax.set_ylabel("y", fontsize=font_size)
    ax.set_xticks(pos_ticks)
    ax.set_yticks(pos_ticks)
    ax.tick_params(labelsize=font_size)

# Let's define some constants for plot rendering

# Normalize so that:
# -1 → blue (low),  0 → white (mid),  1 → red (high)
norm = mcolors.TwoSlopeNorm(vmin=-1, vcenter=0, vmax=1)
var_norm = mcolors.TwoSlopeNorm(vmin=0, vcenter=0.5, vmax=1)
levels=100
cmap = 'coolwarm'
var_cmap = 'OrRd'
drone_color = 'yellow'
font_size = 14
pos_ticks = [0, 100]
pred_ticks = [-1, 0, +1]
var_ticks = [0, +1]

def plot_var_free(
        ax,
        x,
        y,
        z,
        title,
        drone_pos):
    limit = np.max(z)
    plot_field(
        ax,
        x,
        y,
        z,
        title,
        cmap=var_cmap,
        norm=mcolors.TwoSlopeNorm(vmin=0, vcenter=limit/2, vmax=limit),
        levels=levels,
        pos_ticks=pos_ticks,
        ticks=[0,limit],
        extend='max',
        drone_pos=drone_pos,
        drone_color=drone_color,
        font_size=font_size
    )

plot_mean = partial(
    plot_field,
    cmap=cmap,
    norm=norm,
    levels=levels,
    pos_ticks=pos_ticks,
    ticks=pred_ticks,
    extend='both',
    drone_color=drone_color,
    font_size=font_size
)

plot_var = partial(
    plot_field,
    cmap=var_cmap,
    norm=var_norm,
    levels=levels,
    pos_ticks=pos_ticks,
    ticks=var_ticks,
    extend='max',
    drone_color=drone_color,
    font_size=font_size
)