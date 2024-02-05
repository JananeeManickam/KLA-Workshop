import json
import csv
from PIL import Image, ImageChops

with open(r'C:\Users\manik\Desktop\KLA\level-1\input.json') as json_File :
    data=json.load(json_File)

coordinates = x, y = 799, 599

#-------------------------------- GREY SCALE ----------------------------------

l1=[]
img1 = Image.open("wafer_image_1.png") 
a1 = img1.convert('L')
#a1.show()
for i in range (0,x):
    for j in range (0,y):
        l1.append(a1.getpixel((i,j)))
# print(l1)

l2=[]
img2 = Image.open("wafer_image_2.png") 
a2 = img2.convert('L')
#a2.show()
for i in range (0,x):
    for j in range (0,y):
        l2.append(a2.getpixel((i,j)))
# print(l2)


l3=[]
img3 = Image.open("wafer_image_3.png") 
a3 = img3.convert('L')
#a3.show()
for i in range (0,x):
    for j in range (0,y):
        l3.append(a3.getpixel((i,j)))
# print(l3)

l4=[]
img4 = Image.open("wafer_image_4.png") 
a4 = img4.convert('L')
#a4.show()
for i in range (0,x):
    for j in range (0,y):
        l4.append(a4.getpixel((i,j)))
# print(l4)


l5=[]
img5 = Image.open("wafer_image_5.png") 
a5 = img5.convert('L')
#a5.show()
for i in range (0,x):
    for j in range (0,y):
        l5.append(a5.getpixel((i,j)))
# print(l5)


d1=[]
d2=[]
d3=[]
d4=[]
d5=[]



mismatch12 = [i for i, j in zip(l1, l2) if i != j]
print(len(mismatch12))

mismatch13 = [i for i, j in zip(l1, l3) if i != j]
#print(mismatch13)
print(len(mismatch13))

mismatch14 = [i for i, j in zip(l1, l4) if i != j]
#print(mismatch14)
print(len(mismatch14))

mismatch15 = [i for i, j in zip(l1, l5) if i != j]
#print(mismatch15)
print(len(mismatch15))

def1 = [1,mismatch12,mismatch13,mismatch14,mismatch15]

print("Comp with 2 img")
mismatch23 = [i for i, j in zip(l2, l3) if i != j]
#print(mismatch13)
print(len(mismatch23))

mismatch24 = [i for i, j in zip(l2, l4) if i != j]
#print(mismatch14)
print(len(mismatch24))

mismatch25 = [i for i, j in zip(l2, l5) if i != j]
#print(mismatch15)
print(len(mismatch25))

def2 = [2,mismatch23,mismatch24,mismatch25]

print("Comp with 3 img")
mismatch34 = [i for i, j in zip(l3, l4) if i != j]
#print(mismatch14)
print(len(mismatch34))

mismatch35 = [i for i, j in zip(l3, l5) if i != j]
#print(mismatch15)
print(len(mismatch35))

def3 = [3,mismatch34,mismatch35]


print("Comp with 4 img")
mismatch45 = [i for i, j in zip(l4, l5) if i != j]
#print(mismatch15)
print(len(mismatch45))

def4 = [4,mismatch45]


with open('defect.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerows(def1)
    writer.writerows(def2)
    writer.writerows(def3)
    writer.writerows(def4)

# a12 = list(set(l1).symmetric_difference(set(l2)))
# print(a12)

# final_img = list[l1,l2,l3,l4,l5]
# print(final_img)

# diff = ImageChops.difference(img1, img2)
# diff.show()

#----------------------------- RGB VALUE --------------------------------------
# l2=[]
# img2 = Image.open("wafer_image_2.png") 
# #img2.show()
# px2 = img2.load()
# for i in range(0,x):
#     for j in range(0,y):
#         l2.append(list(img2.getpixel(coordinates)))
        
        
# l3=[]
# img3 = Image.open("wafer_image_3.png") 
# #img3.show()
# px3 = img3.load()
# for i in range(0,x):
#     for j in range(0,y):
#         l3.append(list(img3.getpixel(coordinates)))

# print(l1[1])
# count = 0
# for i in range(len(l1)):
#     for j in range(len(l2)):
#         for k in range(len(l3)):
#             while((l1[i] == l2[j]) and l1[i]==l3[j]):
#                 count+=1
# print(count)



#-----------------------------  JSON INPUTS -----------------------------------
# die = data['die']
# streetWidth = data['street_width']
# careAreaDimentions = data['care_areas']
# exclusionZones = data['exclusion_zones']

# print(die)
# print(streetWidth)
# print(careAreaDimentions)
# print(exclusionZones)


#-------------------------------- CSV FILE ------------------------------------
# Opening a file
# file1 = open('myfile.txt', 'w')
# for coordinate in diff_coordinates:
#     x, y = coordinate
#     file1.write(f'{x,y}')
#     print("\n")

# # Closing file
# file1.close()

# # Checking if the data is
# # written to file or not
# file1 = open('myfile.txt', 'r')
# print(file1.read())
# file1.close()
