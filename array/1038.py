# Problem ID 1038 Celsius to Fahrenheit Table
def printTable(start, end, step):
  for fahr in range(start, end, step):
      print(fahr, int((fahr-32)*5/9), sep='\t')

l = input().strip().split(' ')
start, end, step = (int(i) for i in l)
printTable(start, end, step)
