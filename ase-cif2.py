#!/usr/bin/env python
import sys

import click
import ase
import ase.io

@click.command()
@click.argument('ciffile_path',  type=click.Path(exists=True))
@click.argument('outfile',  type=click.Path(exists=False))
def ase_cif2(ciffile_path, outfile):
    a = ase.io.read(ciffile_path)
    ase.io.write(outfile, a)

if __name__ == '__main__':
    ase_cif2()
