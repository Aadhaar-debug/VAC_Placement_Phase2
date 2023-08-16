def miet(i,j):
    if(A[j]=='\0' | B[j] == '\0'):
        return 0
    elif (A[j]==B[j]):
        return 1+miet(i+1,j+1)
    else:
        return max(miet(i+1,j),miet(i,j+1))


