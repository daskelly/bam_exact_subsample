#!/usr/bin/env python

"""
Sub-sample an exact number of reads from a BAM file
"""
import sys, argparse, pysam, random

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("bamfile", metavar="infile.bam")
    parser.add_argument("outfile", metavar="outfile.bam")
    parser.add_argument("N", metavar="n_reads", type=int)
    parser.add_argument('--seed', help="Seed for random read selection", default=1, metavar="N")
    args = parser.parse_args()
    random.seed(args.seed)
    
    # First read through bam and count reads
    N = 0
    sfile = pysam.AlignmentFile(args.bamfile, 'rb')
    for aln in sfile:
        N += 1
    sfile.close()
    
    # Only continue on if there are enough reads to subsample args.N
    if args.N > N:
        print("Can't subsample {} reads from {}".format(args.N, N), file=sys.stderr)
        sys.exit(1)
    else:
        print("Subsampling {} reads from {}".format(args.N, N), file=sys.stderr)

    # Randomly select the args.N reads we are keeping
    # Write those reads to args.outfile
    keep = random.sample(range(N), k=args.N)
    sfile = pysam.AlignmentFile(args.bamfile, 'rb')
    ofile = pysam.AlignmentFile(args.outfile, 'wb' ,template=sfile)
    for i, aln in enumerate(sfile):
        if i in keep:
            ofile.write(aln)
    sfile.close()
    ofile.close()

if __name__ == "__main__":
    sys.exit(main())
