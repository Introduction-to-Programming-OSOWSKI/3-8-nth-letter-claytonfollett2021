def nthLetter(w, n):

    if n > len(w):
        return False 

    else: 
        return w[n-1]

print (nthLetter("dog", 4))