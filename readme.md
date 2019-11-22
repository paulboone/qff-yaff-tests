# README



## Steps


1: make ff

```bash
cd irmof1/irmof1-b3lyp-3-21g/
./../make_ff.sh
```

2: make yaff system from cif

```bash

./ase-cif2 IRMOF-1.cif IRMOF-1.xyz
./irmof1-system.py
```

3: run yaff pressure sweep

```

cd irmof1/irmof1-b3lyp-3-21g/
cp ../../init.chk ./
mkdir results
python ../../yaff-pressure-sweep.py > yaff-pressure-sweep.out
python ../../yaff-analyze-bulk-modulus.py  > yaff-analyze-bulk-modulus.out

```
