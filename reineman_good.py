import matplotlib.pyplot as plt
import math
from matplotlib.patches import Rectangle

ln = math.log
sin = math.sin
cos = math.cos 
tan = math.tan

def f(x):
        return (  (-0.34) * x**2 ) -( 5.86 * x ) - 21.76



a = float(input("please enter a value for a : "))
b = float(input("please enter a value for b : "))
N = int(input("please enter a number of how many rectangles you want:  "))
i = 0
dx = (b-a)/N



list = []

while i < N :
    value_2 = f(a+dx*i)
    list.append(value_2)
    i+=1
    if i > N :
        break






list_2 = []
for value in list:
    multiply = value * dx
    list_2.append(multiply)


print(abs(sum(list_2)))



x_value_of_basic_function = []


startt = a 

while startt <= b+dx :
  
    x_value_of_basic_function.append(round(startt,1))
    startt +=dx

y_value_of_basic_function = []
for num in x_value_of_basic_function:
    y_value = f(num)
    y_value_of_basic_function.append(y_value)
print(y_value_of_basic_function)




fig, ax = plt.subplots()


ax.plot(x_value_of_basic_function, y_value_of_basic_function) 



rectangle_num = -1
start_x_point , start_y_point = a-(dx/2)  ,0
rec = 0
while rectangle_num <= N :
    
    ax.add_patch(Rectangle((start_x_point , start_y_point),dx, y_value_of_basic_function[rec],edgecolor = 'red',facecolor = 'green',fill=True))
    start_x_point+=dx
    rectangle_num+=1
    rec+=1
    if rectangle_num == N:
        break

plt.show()

