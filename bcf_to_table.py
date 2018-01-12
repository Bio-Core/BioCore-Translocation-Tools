#!/usr/bin/env python3

"""
A Python3 script to convert BCF files from Delly2 (v0.7.7) to a Circos
tab separated fields file.
"""

__version__ = "$Revision: 0.1 $"

from pysam import VariantFile
import argparse
import os
import re
from yaml import load, dump

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--vcf", help="file to process in Variant Call Format (required)")
    parser.add_argument("--filter", help="flag to filter the data", action="store_true")
    parser.add_argument("-s", "--sample", help="name of the sample to process (required)")
    args = parser.parse_args()

    print("Converting file", args.vcf, "to Circos compatible link file...\n\n")
    bcf_in = VariantFile(args.vcf)
    output_file = ".".join([os.path.splitext(args.vcf)[0], "translocations", "tab"])
    f = open(output_file, 'w')
    f.write(get_header() + "\n")
    
    for rec in bcf_in.fetch():
        data_array = [
            str(rec.contig),
            str(rec.pos),
            str(rec.info["CHR2"]),
            str(rec.stop),
            str(rec.id),
            str(rec.info["MAPQ"]),
            str(rec.info["PE"])
            ]
        if "SR" in rec.info.keys():
            data_array.append(str(rec.info["SR"]))
        else:
            data_array.append("0")

        f.write("\t".join(data_array)+ "\n")
#            str(rec.contig),
#            str(rec.pos),
#            str(rec.info["CHR2"]),
#            str(rec.stop),
#            str(rec.id),
#            str(rec.info["MAPQ"]),
#            str(rec.info["PE"])])
#            + "\n")
    f.close()

def get_header():
    return "\t".join([
        "ChromosomeA",
        "PositionA",
        "ChromosomeB",
        "PositionB",
        "ID",
        "MAPQ",
        "PairedEndReadCount",
        "SplitReadCount"
        ])

if __name__ == "__main__":
    main()

