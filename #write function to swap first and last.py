#write function to swap first and last elements of a given tuple.#t = (10, 20, 30 , 40 ,50)
#t = (10, 20, 30, 40, 50)

#def swap_first_last(t):
#    if len(t) < 2:
 #       return t
  #  return (t[-1],) + t[1:-1] + (t[0],)
#print(swap_first_last(t))  # Output: (50, 20, 30, 40, 10)

#write a function to rotate a tuple by n positions to the right.
#t = (10, 20, 30, 40, 50)
#def rotate(t, n):
 #   n = n % len(t)
  #  return t[-n:] + t[:-n]
#print(rotate(t, 2))


#write a function to move all the zero of the give list of the end.
#test case:
#[0,1,0,3,12]
#output[1,3,12,0,0]

def move_zero(l):
    for i in l:
        if i != 0:
            print(i, end=" ")
    for i in l:
        if i == 0:
            print(i, end=" ")

l = [1, 0, 2, 0, 3, 4]
move_zero(l)
  
   