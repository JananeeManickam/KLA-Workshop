from PIL import Image
import csv
import json

img1=Image.open('wafer_image_1.png','r')
img2=Image.open('wafer_image_2.png','r')
img3=Image.open('wafer_image_3.png','r')
img4=Image.open('wafer_image_4.png','r')
img5=Image.open('wafer_image_5.png','r')


coordinate_list=[]
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]

d1=[]
d2=[]
d3=[]
d4=[]
d5=[]
# a12 = list(set(l1).symmetric_difference(set(l2)))
# print(a12)

# final_img = list[l1,l2,l3,l4,l5]
# print(final_img)

# diff = ImageChops.difference(img1, img2)
# diff.show()


#-----------------------------  JSON INPUTS -----------------------------------
# die = data['die']
# streetWidth = data['street_width']
# careAreaDimentions = data['care_areas']
# exclusionZones = data['exclusion_zones']

# print(die)
# print(streetWidth)
# print(careAreaDimentions)
# print(exclusionZones)


with open('input.json') as json_file:
    data=json.load(json_file)
    care_areas=data['care_areas']
    care_areas=care_areas[0]
    top_left=care_areas['top_left']
    bottom_right=care_areas['bottom_right']
    width=data['die']['width']
    height=data['die']['height']
    # die = data['die']
    # streetWidth = data['street_width']
    # careAreaDimentions = data['care_areas']
    # exclusionZones = data['exclusion_zones']

    # print(die)
    # print(streetWidth)
    # print(careAreaDimentions)
    # print(exclusionZones)
    for x in range(top_left['x'],bottom_right['x']):
        for y in range(bottom_right['y'],top_left['y']):
            coordinate_list.append([x,y])
        
for i in coordinate_list:
    c=i[0],i[1]
    l1.append(img1.getpixel(c))
    l2.append(img2.getpixel(c))
    l3.append(img3.getpixel(c))
    l4.append(img4.getpixel(c))
    l5.append(img5.getpixel(c))
  
    
#checking for defects
def find_defect(j,image1,image2,image3):
    defect=[]
    for i in range(len(image1)):
        if image1[i]!=image2[i] and image1[i]!=image3[i]:
            defect.append((j,coordinate_list[i][0],height-coordinate_list[i][1]-1))
    return defect
  

# mismatch12 = [i for i, j in zip(l1, l2) if i != j]
# #print(mismatch12)
# print(len(mismatch12))

# mismatch13 = [i for i, j in zip(l1, l3) if i != j]
# #print(mismatch13)
# print(len(mismatch13))

# mismatch14 = [i for i, j in zip(l1, l4) if i != j]
# #print(mismatch14)
# print(len(mismatch14))

# mismatch15 = [i for i, j in zip(l1, l5) if i != j]
# #print(mismatch15)
# print(len(mismatch15))
         
d1=find_defect(1,l1,l2,l3)
d2=find_defect(2,l2,l3,l4)
d3=find_defect(3,l3,l4,l5)
d4=find_defect(4,l4,l5,l1)
d5=find_defect(5,l5,l1,l2)

# #write into csv files

with open('two_output.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerows(d1)
    writer.writerows(d2)
    writer.writerows(d3)
    writer.writerows(d4)
    writer.writerows(d5)