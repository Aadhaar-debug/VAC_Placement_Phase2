# iterations = int(input())
# # for j in range (iterations+1):
# #     print("*  " * iterations)
# #     iterations=iterations-1

# # for i in range(iterations):
# #     print(" "*i+"*"*2*(iterations-(i)))

# # for i in range(iterations):
# #     print(" "*i+"*")



# for i in range (1,iterations+1):
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(iterations-i):
#         print(" " , end= " ")
#     for j in range(iterations-i):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     print()


# print("\n\n")

# for j in range (iterations+1):
#     print("*  " * j)

# # write a python program to print the pyramid shape ?

# print("\n\n")

# def print_pyramid(iterations):
#   for i in range(iterations):
#     for j in range(iterations-i-1):
#       print(" ", end="")
#     for j in range(i+1):
#       print("*", end="")
#     print()

# print()


# write a pytohn program to print the diamond shape ?

def print_diamond(n):
  for i in range(n):
    for j in range(n-i-1):
      print(" ", end="")
    for j in range(i+1):
      print("*", end="")
    print()

  for i in range(n-1, 0, -1):
    for j in range(n-i):
      print(" ", end="")
    for j in range(i):
      print("*", end="")
    print()

print_diamond(5)