#!/usr/bin/env bash




if [ ! -f gaussian_mbis.h5 ]; then
  echo "creating MBIS charges using horton"

  source ~/venv/qffpy2/bin/activate
  horton-wpart.py gaussian.fchk gaussian_mbis.h5 mbis --grid=ultrafine > horton.out
  deactivate
fi



source ~/venv/qff/bin/activate
# qff.py --ffatypes=high --suffix=_noei gaussian.fchk

# with electrostatics
if [ ! -f pars_ei_mbisgauss.txt ]; then
  echo "creating qff ei input"
  qff-input-ei.py  -v --ffatypes=high --gaussian gaussian.fchk gaussian_mbis.h5:charges pars_ei_mbisgauss.txt > qff-ei.out
fi


if [ ! -f pars_yaff_mbisgauss.txt ]; then
  echo "creating qff ff"
  qff.py --ffatypes=high --ei=pars_ei_mbisgauss.txt --suffix=_mbisgauss gaussian.fchk > qff.out
fi
deactivate
