#!/usr/bin/env python3

"""
A Python tool for splitting a BCF file from Delly's translocation output (BND)
and creating two individual BED files that will be used for gene annotation.
"""

from pysam import VariantFile
import argparse
import os
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--vcf", help="file to process in Variant Call Format (required)")
    parser.add_argument("-s", "--sample", help="name of the sample to process in VCF file (required)")
    parser.add_argument("--score", default="100", help="score for the entry (default: 100)")
    parser.add_argument("--strand", default="+", help="strand for the entry (default: ")
    args = parser.parse_args()

    print("Convert BCF to BED files for each end of the translocation...\n")
    bcf_in = VariantFile(args.vcf)

    for rec in bcf_in.fetch():
        strand = "+"
        score = "100"

if __name__ == "__main__":
    main()

