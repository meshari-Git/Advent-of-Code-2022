cal = open('input.txt')
globalMax = 0
local = 0
for line in cal:
    if len(line) > 2:
        local += int(line)
    else:
        globalMax = max(globalMax , local) 
        local = 0
       

print(globalMax)




