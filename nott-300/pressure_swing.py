#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("nott-300/results/vpe_results.txt")
v, p, e = data[:,0:3].T # data is already in Å3 and MPa


# Select the reference volume.
v_ref = v[abs(p).argmin()]
v_rel = v/v_ref

fs = 12
fig = plt.figure(figsize=(3.75,3.0))
fig.set_tight_layout(True)
ax = fig.add_subplot(1, 1, 1)

ax.set_ylabel('V/V_0', fontsize=fs)
ax.set_xlabel('Pressure [MPa]', fontsize=fs)
ax.grid(linestyle='-', color='0.7', zorder=0)

ax.tick_params(axis='x', which='major', labelsize=fs)
ax.tick_params(axis='y', which='major', labelsize=fs)

plt.plot(p, v_rel, 'ko', markersize=3)

fig.savefig("pv.png", dpi=300)
