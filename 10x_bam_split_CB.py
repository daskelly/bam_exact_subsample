#!/usr/bin/env python

"""
Given a 10X Genomics BAM file, split by cell barcodes into
separate BAMs.
"""
import sys, argparse, pysam, gzip, os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("bamfile", metavar="infile.bam")
    parser.add_argument("barcodes", metavar="barcodes.tsv.gz")
    parser.add_argument("outdir", metavar="/path/to/outdir")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    assert args.barcodes.endswith('.gz')
    assert os.path.exists(args.outdir) and os.path.isdir(args.outdir)
    #
    # Read through barcodes file to capture CBs that we'll be considering
    bc = set()
    f = gzip.open(args.barcodes)
    for line in f:
        this_barcode = line.rstrip().decode("utf-8")
        bc.add(this_barcode)
    f.close()
    #
    # Open handles to CB-specific BAM files
    cb_bams = dict()
    sfile = pysam.AlignmentFile(args.bamfile, 'rb')
    for barcode in bc:
        file_path = "{}/{}_full.bam".format(args.outdir, barcode)
        cb_bams[barcode] = pysam.AlignmentFile(file_path, 'wb' ,template=sfile)
    #
    # Read through args.bamfile and write each read to the proper CB-specific BAM
    failed = 0
    for i, aln in enumerate(sfile):
        if i % 10000000 == 0 and args.verbose:
            print("On read {}".format(i))
        try:
            cb = aln.get_tag('CB')
            cb_bams[cb].write(aln)
        except KeyError:
            failed += 1
            continue
    #
    # Close everything up nice and tidy
    sfile.close()
    for key in cb_bams:
        cb_bams[key].close()
    #
    print("Found {} alignments that \"failed\" due to having no valid filtered CB available".format(failed))

if __name__ == "__main__":
    sys.exit(main())
