def rec_fabi(n):
    if n<=1:
        return n
    else:
        return (rec_fabi(n-1) + rec_fabi(n-2))

nterms = int(input("Enter number of terms for series (greater than 0 ) :"))

if nterms<=0:
    print("Please enter +ve number ")
else:
    print("Fabinoci series:")
    for i in range(nterms):
        print(rec_fabi(i))