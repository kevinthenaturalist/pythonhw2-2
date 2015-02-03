file = open("input.txt")
output = open("trimmed.txt", "w") #creates new file to write trimmed sequences to
for seq in file:
    print(seq[14:1000])
for seq in file:
    trimmed_dna = seq[14:1000]
    output.write(trimmed_dna)
for seq in trimmed:
    print("processed sequence with length " + str(len(trimmed_dna)))
    #gets error: File not open for reading. Must be done within a single loop, I guess?
    
for seq in file:
    trimmed_dna = seq[14:1000]
    output.write(trimmed_dna)
    print("sequence length: " + str(len(trimmed_dna))) # this loop works
