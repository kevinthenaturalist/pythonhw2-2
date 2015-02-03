#Kevin Neal
#EEB234 homework due tuesday 2-3
#read pfb ch. 3, do exercises from pfb ch. 4 p. 97
#submit as github repository with at least one commit per assignment

# Notes:
# open file with fileobject = open("file.txt"); read with fileobject.read(); 
# remove newline with fileobject.rstrip("\n"). 
# combine as fileobject.read().rstrip("\n")

#use open("file.txt", "w") to open file for writing; "a" to append
# then fileobject.write("this text will be written to the file")
# .close() closes the file

#processing DNA in a file - input.txt

# print characters [14:10000] to new file
file = open("input.txt")
output = open("trimmed.txt", "w") #creates new file to write trimmed sequences to
for seq in file:
    print(seq[14:1000])
    trimmed_dna = seq[14:1000]
    output.write(trimmed_dna)
for seq in trimmed:
    print("processed sequence with length " + str(len(trimmed_dna)))
    #gets error: File not open for reading. Must be done within a single loop, I guess?
    
for seq in file:
    trimmed_dna = seq[14:1000]
    output.write(trimmed_dna)
    print("sequence length: " + str(len(trimmed_dna)))
    
# write a program to extract exon segments from genomic_dna.txt,
# concatenate them, and write them to a new file

# why the hell does python "forget" that I've created a file object with the open command?
# if I don't have the fileobject = open('file.txt') immediately before I try to work with
# fileobject, it treats fileobject like it is empty/doesn't exist. Why???
# SOLUTION! using .read() changes the read frame to the end, so when you start
# the fileobject into a for-loop, it is reading from the end and thus does nothing!

exon_locations = open("exons.txt")
for line in exon_locations:
    positions = line.split(',')
    print(line)
    
exon_locations = open("exons.txt")
for line in exon_locations:
    positions = line.split(',')
    start = positions[0]
    stop = positions[1]
    print("start is " + start + ", stop is " + stop)
    
genomic_dna_contents = open("genomic_dna.txt").read()
exon_locations = open("exons.txt")
coding_sequence = "" # creates an empty variable; loop will iteratively add the exons to this
for line in exon_locations:
    positions = line.split(',') # exons.txt has two numbers per line separated by a comma
    start = int(positions[0]) # output of line.split is a string; must convert to int here
    stop = int(positions[1]) 
    exon = genomic_dna_contents[start:stop]
    coding_sequence = coding_sequence + exon # this concatenates all of the exons

concatexons = open("concatexons.txt", "w") # new file to put the output into
concatexons.write(coding_sequence)
concatexons.close()
