# /usr/bin/python
# Author: Nur Syatila Ab Ghani
# Function: Convert GenBank to FASTA (Bio module is required)

import argparse
from Bio import SeqIO

def convert_gb_fasta(inputfile,outputfile):
    with open(inputfile, "r") as input_handle:
        with open(outputfile, "w") as output_handle:
            sequences = SeqIO.parse(input_handle, "genbank")
            count = SeqIO.write(sequences, output_handle, "fasta")

    print("Converted %i records" % count)

my_parser = argparse.ArgumentParser(description='Function: Convert GenBank (.gb) to fasta (.fa)')
my_parser.add_argument('input',type=str,help='Input file (GenBank)')
my_parser.add_argument('output',type=str,help='Output file (FASTA)')

args = my_parser.parse_args()
inputfile = args.input
outputfile = args.output
convert_gb_fasta(inputfile,outputfile)
