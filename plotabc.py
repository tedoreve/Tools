# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 09:52:49 2018

@author: tedoreve
"""

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import AxesGrid


def get_demo_image():
    import numpy as np
    from matplotlib.cbook import get_sample_data
    f = get_sample_data("axes_grid/bivariate_normal.npy", asfileobj=False)
    z = np.load(f)
    # z is a numpy array of 15x15
    return z, (-3, 4, -4, 3)


def demo_right_cbar(fig):
    """
    A grid of 2x2 images. Each row has its own colorbar.
    """

    grid = AxesGrid(F, 111,  # similar to subplot(122)
                    nrows_ncols=(1, 1),
                    axes_pad=0.0,
                    label_mode="1",
                    share_all=True,
                    cbar_location="right",
                    cbar_mode="edge",
                    cbar_size="7%",
                    cbar_pad="0%",
                    )
    Z, extent = get_demo_image()
    cmaps = [plt.get_cmap("spring"), plt.get_cmap("winter")]

    im = grid[0].imshow(Z, extent=extent, interpolation="nearest",
                        cmap=cmaps[0])

    grid.cbar_axes[0].colorbar(im)

    for cax in grid.cbar_axes:
        cax.toggle_label(True)
        cax.axis[cax.orientation].set_label('Foo')

    # This affects all axes because we set share_all = True.
    grid.axes_llc.set_xticks([-2, 0, 2])
    grid.axes_llc.set_yticks([-2, 0, 2])


if 1:
    F = plt.figure(111)

    F.subplots_adjust(left=0.05, right=0.93)

    demo_right_cbar(F)

    plt.draw()
    plt.show()