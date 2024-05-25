# قم بعمل مخطط تدفقي يقوم طباعة هذا الشكل للمستخدم     الشكل  <
# *
# * *
# * * *
# * * * *


def triangle_one():

    for i in range(5):
        for j in range(i + 1):
            print("*",end ="  ")
        print()
# triangle_one()


# قم بعمل مخطط تدفقي يقوم طباعة هذا الشكل للمستخدم     الشكل  <

# *******
# ******
# ****
# **
# *

def triangle_two():

    for j in range(5 , 0 , -1):
        for i in range(j):
            print("*",end =" ")
        print()

# triangle_two()

# قم بعمل مخطط تدفقي يقوم طباعة هذا الشكل للمستخدم     الشكل  <
# 1
# 2 1
# 3 2 1
# 4 3 2 1
def triangle_three():
    
    for i in range(5):
        for j in range(1,i + 1):
            print( j ,end ="  ")
        print()
triangle_three()

# def triangle_three():
    
#     for i in range(5+ 1 ):
#         for j in range(i , 0 ,-1):
#             print( i,end ="  ")
#         print()
# triangle_three()


# قم بعمل مخطط تدفقي يقوم طباعة هذا الشكل للمستخدم     الشكل  <
# 2
# 4 2
# 6 4 2
# 8 6 4 2
def triangle_four():
    for i in range(5+1):
        for j in range(i,-1,-1):
            print( j*2 ,end ="  ")
        print()

triangle_four()