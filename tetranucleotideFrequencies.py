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
num1 = 0.0
for line in file1:
    for n in range(4, len(line)):
        num1 += 1.0
        if line[n-4:n] not in tetra1:
            tetra1[line[n-4:n]] = 1
        else:
            tetra1[line[n-4:n]] += 1

tetra2 = {}
num2 = 0.0
for line in file2:
    for n in range(4, len(line)):
        num2 += 1.0
        if line[n-4:n] not in tetra2:
            tetra2[line[n-4:n]] = 1
        else:
            tetra2[line[n-4:n]] += 1

for key in tetra1:
    tetra1[key] = tetra1[key]*100.0/num1/256.0
for key in tetra2:
    tetra2[key] = tetra2[key]*100.0/num2/256.0


perDiff = 0
for key in set(tetra1.keys()).union(tetra2.keys()):
    if key not in tetra1:
        perDiff += tetra2[key]
    elif key not in tetra2:
        perDiff += tetra1[key]
    else:
        perDiff += abs(tetra1[key] - tetra2[key])

print(perDiff)
    
