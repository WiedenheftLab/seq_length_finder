#!/usr/bin/python

import argparse
import sys
import os
import subprocess
import textwrap

try:
    from Bio import SeqIO
except ImportError, e:
    print "SeqIO module is not installed! Please install SeqIO and try again."
    sys.exit()

try:
    import tqdm
except ImportError, e:
    print "tqdm module is not installed! Please install tqdm and try again."
    sys.exit()

parser = argparse.ArgumentParser(prog='python seq_length_finder.py',
      formatter_class=argparse.RawDescriptionHelpFormatter,
      epilog=textwrap.dedent('''\

      	Author: Murat Buyukyoruk
      	Associated lab: Wiedenheft lab

        seq_length_finder help:

This script is developed to get the length of sequences in a fasta file. 

SeqIO package from Bio is required to fetch sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain long and many sequences.
        
Syntax:

        python seq_length_finder.py -i demo.fasta -l demo_sub_list.txt -o demo_sub_list.fasta

seq_fetch dependencies:
	Bio module and SeqIO available in this package      refer to https://biopython.org/wiki/Download
	tqdm                                                refer to https://pypi.org/project/tqdm/
	
Input Paramaters (REQUIRED):
----------------------------
	-i/--input		FASTA			Specify a fasta file.

	-o/--output		output file	    Specify a output file.
	
Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.

	
      	'''))
parser.add_argument('-i', '--input', required=True, type=str, dest='filename',
                    help='Specify a fasta file.\n')
parser.add_argument('-o', '--output', required=True, dest='out',
                    help='Specify a output file.\n')

results = parser.parse_args()
filename = results.filename
out = results.out

os.system('> ' + out)

proc = subprocess.Popen("grep -c '>' " + filename, shell=True, stdout=subprocess.PIPE, )
length = int(proc.communicate()[0].split('\n')[0])

with tqdm.tqdm(range(length)) as pbar:
    pbar.set_description('Reading...')
    for record in SeqIO.parse(filename, "fasta"):
        pbar.update()
        f = open(out, 'a')
        sys.stdout = f
        print record.id + '\t' + str(len(record.seq))

