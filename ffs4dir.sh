#!/usr/bin/env bash

ffdir=$1
startdir=`pwd`

for d in $ffdir*/ ; do
  cd $startdir/$d
  ls -l
done
