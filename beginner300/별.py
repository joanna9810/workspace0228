'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
N = int(input())
for i in range(1,N):
    print(' '*(N-i) + '*'*(i*2-1))
for j in range(N,0,-1):
    print(' '*(N-j) + '*'*(j*2-1))