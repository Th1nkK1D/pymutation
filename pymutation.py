import math

source = ['1','2','3','4','5','6','7','8']
target = []

f = open('output.txt','w')

def permutate(source, target):
    if len(source) > 0:
        for num in source:
            newTarget = target.copy()
            newTarget.append(num)
            newSource = source.copy()
            newSource.remove(num)
            permutate(newSource,newTarget)
    else:
        f.write(",".join(target))
        f.write("\n")

print(len(source),"items ->",math.factorial(len(source)),"probabilities")
print("processing...")

permutate(source,target)

print("done")