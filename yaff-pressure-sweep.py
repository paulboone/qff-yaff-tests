#!/usr/bin/env python

import numpy as np
from yaff import System, ForceField, ForcePartPressure, CGOptimizer, StrainCellDOF
from yaff import angstrom, pascal, electronvolt

# from quickff.tools import set_ffatypes

p_unit = 1e6*pascal
e_unit = electronvolt
p = 100

chk_file = 'init.chk'
ff_file = 'pars_yaff_mbisgauss.txt'

# system = System.from_file()
# ff = ForceField.generate(system, )
# ff.add_part(ForcePartPressure(system, p*p_unit))
#
# opt = CGOptimizer(StrainCellDOF(ff, gpos_rms=1e-6, grvecs_rms=1e-6))
# opt.run(500)
# system.to_file('opt%d.chk' % p)
#
# print(system.cell.volume/angstrom**3, ff.part_press.pext/p_unit, ff.energy/e_unit)


pressures = np.linspace(-1000, 2000, 31, endpoint=True)
print(pressures)

results = np.zeros((len(pressures), 3), dtype=np.float32)

for i, p in enumerate(pressures):
    system = System.from_file(chk_file)
    ff = ForceField.generate(system, ff_file, rcut=20*angstrom, alpha_scale=4.0,
                         gcut_scale=2.0, smooth_ei=True, reci_ei='ewald')

    ff.add_part(ForcePartPressure(system, p*p_unit))


    opt = CGOptimizer(StrainCellDOF(ff, gpos_rms=1e-6, grvecs_rms=1e-6))
    opt.run(2000)

    system.to_file('results/opt%d.chk' % p)
    system.to_file('results/opt%d.xyz' % p )
    system.to_file('results/opt%d.cif' % p )
    results[i, :] = (system.cell.volume/angstrom**3, ff.part_press.pext/p_unit, ff.energy/e_unit)

print(results)
np.savetxt("results/vpe_results.txt", results)
