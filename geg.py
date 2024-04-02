import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 60) # 0 ถึง 60
y = x
def in1(x):     #ปริมาณจำกัดนมวัว
  return (16 - (0.6* x)) / 0.2

def in2(x):     #ปริมาณจำกัดถั่วเหลือง
  return (24 - (0.4* x)) / 0.8

def in3(x):     #เวลาในการผลิตสินค้า
   return (20 - (0.5* x)) / 0.5
y1 = in1(x)
y2 = in2(x)
y3 = in3(x)
plt.plot(x, y1, label="Limit cow'milk")
plt.plot(x, y2, label="Limit soybeans")
plt.plot(x, y3, label="time")
plt.axvline(x=3, color="black", linestyle="-", label="Demand Hight protein")   #ความต้องการของ Hight protein
plt.axhline(y=5, color="black", linestyle="-", label="Demand Nor protein")   #ความต้องการของ normal protein
plt.axhline(y=0, color="purple", linestyle="-", label="Positive value")             #พิจารณาค่าที่เป็นบวก
plt.xlim(0, None)
plt.ylim(0, None)
plt.xlabel("Hight protein")
plt.ylabel("Normal protein")
plt.title("Product Plan")
plt.legend() 
 
plt.show()