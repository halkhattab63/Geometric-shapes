# قم بعمل مخطط تدفقي يقوم طباعة هذا الشكل للمستخدم     الشكل  <

# ********
# ********
# ********

def square_one():

    for i in range(5):
        for j in range(5):
            print("*",end ="  ")
        print()

# square_one()

def square_two(): 
    matrix = [[0 for _ in range(3)]for _ in range(3)]

    value = 1 
    for i in range(3):
        for j in range(3):
            matrix[i][j] = value*5
            value +=1
    for row in matrix: 
        for element in row:  
            print(f"{element}",end =" ")
        print()

# square_two()



# قم بعمل مخطط تدفقي يقوم طباعة هذا الشكل للمستخدم     الشكل  <
# a a a
# b b b
# c c c


def square_three():
    alfa = 'a'
    for i in range(3):
        for j in range(3):
            print(alfa , end="  ")
        print()
        value = ord(alfa)
        alfa = chr(value + 1)

# square_three()



# قم بعمل مخطط تدفقي يقوم طباعة هذا الشكل للمستخدم     الشكل  <
# 1 2 3
# 1 2 3
# 1 2 3


def square_four():
    value = 1
    for i in range(3):
        for j in range(3):
            print(value , end="  ")
            value +=1
        print()
        value = 1

# square_four()


