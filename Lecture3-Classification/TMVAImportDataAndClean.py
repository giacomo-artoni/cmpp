#!/bin/env python
"""
Script to import and clean MiniBooNE dataset from https://archive.ics.uci.edu/ml/datasets/MiniBooNE+particle+identification

Setup on pplxint:

> module load root
> module load python

"""

import ROOT, array, csv

csvfile=open("MiniBooNE_PID.txt")
freader1 = csv.reader(csvfile, delimiter=" ")

tfout=ROOT.TFile("mbdataset.root","RECREATE")
#create ntuple object
ntuple = ROOT.TNtuple("mbdata", "mbdata", ":".join(["f%d"%i for i in range(50)]))

for index, l in enumerate(freader1):  
  if "-0.999000E+03" in l: continue #clean -999 entries
  reduced_l=[float(x) for x in filter(len,l)]
  ntuple.Fill(array.array("f",reduced_l))

tfout.cd()
ntuple.Write()
