# seq_length_finder


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


