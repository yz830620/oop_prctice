# you want to process a series of data, but don't want to insert the data into 
# list set or tuple, which you don't want to comsume memory space 
# The solution for you should be generator

# compare with original tuple version
import sys

inname = sys.argv[1]
outname = sys.argv[2]

def tuple_method(inname, outname):
    with open(inname) as infile:
        with open(outname, 'w') as outfile:
            # count all the warning first, if warning is big and run through million lines
            warnings = (l for l in infile if "WARNING" in l)
            for l in warnings:
                outfile.write(l)

def generator_method(inname, outname):
    with open(inname) as infile:
        with open(outname, 'w') as outfile:
            # count all the warning first, if warning is big and run through million lines
            warnings = (l.replace('\tWARNING', '') for l in infile if "WARNING" in l)
            for l in warnings:
                outfile.write(l)