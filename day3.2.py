with open("input.txt") as f:
  lines = f.read().splitlines()
score = 0
def calcpriority(item):
  # get numeric value of the upper and lower case letters
  priority = ord(item.lower()) - 96
  if item.isupper():
    priority += 26
  #print(priority)
  return(priority)


for x in range(0 , len(lines) , 3):
    print("current index : " , x)
    for char in lines[x]:
        print(lines[x])
        if char in lines[x + 1] and char in lines[x + 2] and char not in u:
            print("found char " + char)
            score = score + calcpriority(char)
            break

print(score)


