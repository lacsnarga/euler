import pandas as pd

def area(x1, y1, x2, y2, x3, y3):
    return abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))

df = pd.read_csv("0102_triangles.txt", header = None)
df.columns = ["X1", "Y1", "X2", "Y2", "X3", "Y3"]
count = 0
for row in range(999):
    x1 = df.iloc[row, 0]
    y1 = df.iloc[row, 1]
    x2 = df.iloc[row, 2]
    y2 = df.iloc[row, 3]
    x3 = df.iloc[row, 4]
    y3 = df.iloc[row, 5]     
    area_0 = area(x1, y1, x2, y2, x3, y3)
    print(area_0)
    print(area_1)
    print(area_2)
    print(area_3)
    if area_0 == area_1 + area_2 + area_3:
        count+=1

print(count)
