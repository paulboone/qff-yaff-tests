#!/usr/bin/env python

from __future__ import print_function


import matplotlib.pyplot as pt

import numpy as np
import h5py as h5

from yaff import angstrom, pascal, electronvolt, boltzmann

# Just to give you an idea, kT at room temperature in electronvolt.
print('kT [eV]', boltzmann*300/electronvolt)

data = np.loadtxt("results/vpe_results.txt")

# units
v_unit = angstrom**3
p_unit = 1e6*pascal
e_unit = electronvolt

# Transform your data into arrays:
v, p, e = data.T
p *= p_unit
v *= v_unit
e *= e_unit

# Select the reference volume.
v_ref = v[abs(p).argmin()]

# Compute the dimensionless volume.
x = v/v_ref

# Define an auxiliary array of dimensionless volumes to facilite the plots of
# the models
x_aux = np.linspace(x.min(), x.max(), 100)


def fit_linear_pv():
    print('Fit linear model to P(V/V_0)')

    # fit p(v), dm=design matrix, ev=expected values
    dm = np.array([x, np.ones(len(v))]).T
    ev = p
    a, b = np.linalg.lstsq(dm, ev)[0]
    print('    Bulk modulus [MPa]', -a/p_unit)

    # plot
    pt.clf()
    pt.plot(x, p/p_unit, 'ko')
    pt.plot(x_aux, (a*x_aux + b)/p_unit, 'r-')
    pt.xlabel('V/V_0')
    pt.ylabel('Pressure [MPa]')
    pt.savefig('pv.png')


def fit_quadratic_ev():
    print('Fit quadratic model to E(V/V_0)')

    # fit e(v), dm=design matrix, ev=expected values
    dm = np.array([0.5*x**2, x, np.ones(len(v))]).T
    ev = e
    a, b, c = np.linalg.lstsq(dm, ev)[0]
    print('    Bulk modulus [MPa]', a/v_ref/p_unit)
    print('    Energy [eV]', (c - a**2/2/b)/e_unit)

    # plot
    pt.clf()
    pt.plot(x, e/e_unit, 'ko')
    pt.plot(x_aux, (0.5*a*x_aux**2 + b*x_aux + c)/e_unit, 'r-')
    pt.xlabel('V/V_0')
    pt.ylabel('Energy [eV]')
    pt.savefig('ev.png')


fit_linear_pv()
fit_quadratic_ev()
