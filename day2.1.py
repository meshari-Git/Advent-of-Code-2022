lines = open("input.txt")
score = 0
for line in lines:
    op = line[0]
    g = line[2]
    if op == "A":
        if g == "X":
            score = score + 3 + 0
        elif g == "Y":
            score = score + 1 + 3
        elif g == "Z":
            score = score + 2 + 6  
    elif op == "B":
        if g == "X":
            score = score + 1 + 0
        elif g == "Y":
            score = score + 2 + 3
        elif g == "Z":
            score = score + 3 + 6  
    elif op == "C":
        if g == "X":
            score = score + 2 + 0
        elif g == "Y":
            score = score + 3 + 3
        elif g == "Z":
            score = score + 1 + 6
    
            
print(score)                      
