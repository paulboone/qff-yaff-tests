#!/usr/bin/env python

import numpy as np
from yaff import System, angstrom, ForceField

from quickff.tools import set_ffatypes

# system_cluster = System.from_file('system_mbisgauss.chk')

# system_cluster.ffatypes

# rvecs = np.diag([25.832]*3)*angstrom
rvecs = np.identity(3) * 25.832 * angstrom
system = System.from_file('IRMOF-1.xyz', rvecs=rvecs)
system.detect_bonds()
set_ffatypes(system, "high")
# system.set_standard_masses()
system.to_file('init.chk')

# ff = ForceField.generate(system, 'pars_yaff_mbisgauss.txt')
