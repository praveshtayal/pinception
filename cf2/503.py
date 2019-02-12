# Problem ID 503 Trailing Zeros in Factorial
def trailingZerosInFact():
  result=0
  power=5
  n=int(input())
  while(n>=power):
    result = result + (n//power)
    power *= 5
  print(result)

trailingZerosInFact()
