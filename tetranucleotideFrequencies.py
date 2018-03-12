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

file1.readline()
file2.readline()

tetra1 = {}

for line in file1:
    for n in range(4, len(line)):
        if line[n-4:n] not in tetra1:
            tetra1[line[n-4:n]] = 1
        else:
            tetra1[line[n-4:n]] += 1

for key in tetra.keys():
    print(key, tetra[key])
    
