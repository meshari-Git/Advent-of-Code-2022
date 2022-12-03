lines = open("input.txt")
score = 0
z = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(len(z))

for line in lines:
    line = line.strip()
    mid = len(line) // 2
    l = line[0 : mid] 
    r = line[mid : ]
    u = set()
    for char in l:
        if char in r and char not in u:
            u.add(char) 
            #print(z.index(char) + 1)
            score = score + z.index(char) + 1
            

            
print(score)                      
