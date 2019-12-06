#!/usr/bin/env python

import matplotlib.pyplot as plt

import numpy as np
import h5py as h5

meter = 1.0/0.5291772083e-10
angstrom = 1.0e-10*meter
joule = 1/4.35974381e-18
newton = joule/meter
pascal = newton/meter**2
second = 1/2.418884326500e-17
coulomb = 1.0/1.602176462e-19
ampere = coulomb/second
electronvolt = (1.0/coulomb)*joule
boltzmann = 3.1668154051341965e-06

# Just to give you an idea, kT at room temperature in electronvolt.
print('kT [eV]', boltzmann*300/electronvolt)

data = np.loadtxt("nott-300/results/vpe_results.txt")
v, p, e = data[:,0:3].T
# data is already in Å3 and MPa

# Select the reference volume.
v_ref = v[abs(p).argmin()]
v_rel = v/v_ref


fs = 12
# fig = plt.figure(figsize=(2.5,2.0))
fig = plt.figure(figsize=(3.75,3.0))
fig.set_tight_layout(True)
# fig.subplots_adjust(left=0.4,right=0.95, top=0.95, bottom=0.20)
ax = fig.add_subplot(1, 1, 1)
# ax.set_xlim(0.85, 1.1)
# ax.set_ylim(-1.2, 2.2)
ax.set_ylabel('V/V_0', fontsize=fs)
ax.set_xlabel('Pressure [MPa]', fontsize=fs)
ax.grid(linestyle='-', color='0.7', zorder=0)


ax.tick_params(axis='x', which='major', labelsize=fs)
ax.tick_params(axis='y', which='major', labelsize=fs)

print(p)
plt.plot(p, v_rel, 'ko', markersize=3)

# ax.legend(framealpha=1.0, fontsize=fs-2)
fig.savefig("pv.png", dpi=300)
