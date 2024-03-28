#def FibonacciSequence  (n):
#  fibo_seq=[0,1]
 # if n == 0:
 #   return 0
  #elif n == 1:
  #  return 1
  #else:
  #  for i in range [2,n]:
    #      fibo_seq.append(fibo_seq[n-1] +       fibo_seq[n-2])
    #return fibo_seq[-1]+fibo_seq[-2]
                    
#print(FibonacciSequence(10))

#while n <=5:
 # print(n-1 + n-2)
#n+=1
def FibonacciSequence(n):
    fibo_seq = [0, 1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n):
            fibo_seq.append(fibo_seq[-1] + fibo_seq[-2])
        return fibo_seq[-1]

print(FibonacciSequence(20))

