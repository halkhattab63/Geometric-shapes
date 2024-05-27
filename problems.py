# قم بعمل مخطط تدفقي يأخذ ثلاث قيم لأضلاع مثلث ومن ثم يطبع نوع المثلث للمستخدم.
# (إذا كانت جميع الأضلاع متساوية يكون المثلث متساوي الأضلاع
#  وإذا كان ضلعان فقط متساويان يكون متساوي الساقين وإلا يكون مختلف الأضلاع)

def triangle(x , y , z) : 
    if x == y and y == z: 
        return f"equilateral triangle"
    
    elif x == y or y == z or x == z: 
        return f"isosception triangle"
    
    elif x**2 + y**2  == z**2 or x**2 + z**2 == y**2 or y**2 + z**2 == x**2:
        return f"right triangle "
    else: 
        return f"normal triangle"

print(triangle(5,7,3))