# Problem ID: 966 Celsius to Fahrenheit Table
l = input().strip().split(' ')
start, end, step = (int(i) for i in l)
for fahr in range(start, end, step):
      print(fahr, int((fahr-32)*5.0/9.0), sep='\t')
