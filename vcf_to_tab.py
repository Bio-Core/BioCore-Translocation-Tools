import vcf
import argparse

#bcf_in = VariantFile("Mx-9.BND.bcf")
vcf_reader = vcf.Reader(open("Mx-9.BND.vcf"))

f = open("Mx-9.BND.filtered.tab", 'w')
for rec in vcf_reader:
    if len(rec.FILTER) == 0:
        f.write(" ".join([str(rec.CHROM).replace("chr", "hs"), str(rec.POS), str(rec.POS + 1), str(rec.INFO["CHR2"]).replace("chr", "hs"), str(rec.INFO["END"]), str(rec.INFO["END"] + 1)]) + "\n")

f.close()

