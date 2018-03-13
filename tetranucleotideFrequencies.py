import sys

try:
    file1 = open(sys.argv[1],"r")
    file2 = open(sys.argv[2],"r")

except(IndexError):
    print("Too few arguments. Please input 2 fasta files.")
    exit(1)
except(FileNotFoundError):
    print("File not found, please try again.")
    exit(1)
except:
    print("Something went wrong. Please try again.")
    exit(1)

# Throw out the first line of the fasta
file1.readline()
file2.readline()

# let's get all tetranucleotides from the first file
tetra1 = {}
num1 = 0.0
for line in file1:
    #for all tetranucleotides in each contig...
    if line[0] != ">":
        for n in range(4, len(line)):
            num1 += 1.0
            if line[n-4:n] not in tetra1:
                tetra1[line[n-4:n]] = 1
            else:
                tetra1[line[n-4:n]] += 1

# same thing but for the second file
tetra2 = {}
num2 = 0.0
for line in file2:
    if line[0] != ">":
        for n in range(4, len(line)):
            num2 += 1.0
            if line[n-4:n] not in tetra2:
                tetra2[line[n-4:n]] = 1
            else:
                tetra2[line[n-4:n]] += 1


# divide all the numbers of tetranucleotides by the number of total tetranucleotides, giving us a %.
for key in tetra1:
    tetra1[key] = tetra1[key]/num1
for key in tetra2:
    tetra2[key] = tetra2[key]/num2

# add up all the differences between the 2.
# to go through both dicts completely, we did the union of the 2 as sets.
perDiff = 0
for key in set(tetra1.keys()).union(tetra2.keys()):
    if key not in tetra1:
        perDiff += tetra2[key]
    elif key not in tetra2:
        perDiff += tetra1[key]
    else:
        perDiff += abs(tetra1[key] - tetra2[key])

# output!
print(perDiff)