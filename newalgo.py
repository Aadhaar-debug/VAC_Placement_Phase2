# Algorithm for the dynamic priblem approcach
def miet(i,j):
    if(a[i] == b[j]):
        return 1+miet(i+1 , j+1)
    else:
        return(miet(i+1 , j+1), miet(i,j+1))

# algorithm for recursion :

def miet(i , j):
    if (a[i] == '\0' || b[j] == '\0') 
    {
            return 0
            
        else:
            a([i]+b[j]):
                return 1+miet(i+1 , j+1)
        else:
            return max(miet(i-1 , j), miet(i,j-1))
    }