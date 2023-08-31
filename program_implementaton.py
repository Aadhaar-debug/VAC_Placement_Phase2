# primary_string  = ['s' , 't' , 'o' , 'n' , 'e']
# secondary_string = ['l' , 'o' , 'n' , 'g' , 'e' , 's' , 't']

# def function(i , j):
#     for (j in primary_string[i]):
#         for (i in secondary_string[j]):

#             if(primary_string[i] == secondary_string[j]):
#                 return 1+[function(primary_string-1)(secondary_string-1)]

#             elif (primary_string[i] != secondary_string[j]):
#                 return 0


                
primary_string = ['s', 't', 'o', 'n', 'e']
secondary_string = ['l', 'o', 'n', 'g', 'e', 's', 't']

def lcs_length(i, j):
    if i == -1 or j == -1:
        return 0

    if primary_string[i] == secondary_string[j]:
        return 1 + lcs_length(i - 1, j - 1)
    else:
        return max(lcs_length(i - 1, j), lcs_length(i, j - 1))

result = lcs_length(len(primary_string) - 1, len(secondary_string) - 1)
print("Length of LCS:", result)



