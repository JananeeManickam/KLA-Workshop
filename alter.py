import os
import csv
import json
from PIL import Image

def findMajority(lst):
    maxCount = 0
    index = -1
    for i in range(len(lst)):
        count = 1
        for j in range(i+1, len(lst)):
            if(lst[i] == lst[j]):
                count += 1

        if(count > maxCount):
            maxCount = count
            index = i

    if (maxCount > len(lst)//2):
        return(lst[index])

    else:
        return('none')


if __name__ == "__main__":

    with open(r'C:\Users\manik\Desktop\KLA\level-1\input.json') as json_File :
        data=json.load(json_File)


    die = data['die']
    streetWidth = data['street_width']
    careAreaDimentions = data['care_areas']
    exclusionZones = data['exclusion_zones']


    dirPath = r'C:\Users\manik\Desktop\KLA'
    img1=Image.open('wafer_image_1.png')
    img2=Image.open('wafer_image_2.png')
    img3=Image.open('wafer_image_3.png')
    img4=Image.open('wafer_image_4.png')
    img5=Image.open('wafer_image_5.png')

    imagePaths = [img1,img2,img3,img4,img5]
    pixelImages = []

    width, height = die['width'], die['height']

    for imgInput in imagePaths:
        image = Image.open(dirPath+'/'+imgInput, 'r')
        pixelImages.append(image.load())

    anomalies = []
    for y in range(height-1, -1, -1):
        y = height - y - 1
        for x in range(width):
            pixelRows = []
            pixelDimension = []
            for pixel in range(len(pixelImages)):
                r, g, b = pixelImages[pixel][x, height - y - 1]

                pixelRows.append(f'#{r:02x}{g:02x}{b:02x}')
                pixelDimension.append((pixel+1, x, y))
        
            majority = findMajority(pixelRows)

            if majority != 'none':
                for pixel in range(len(pixelRows)):
                    if pixelRows[pixel] != majority:
                        die, x, y = pixelDimension[pixel]
                        anomalies.append([die, x, y])
            else:
                for pixel in range(len(pixelRows)):
                    anomalies.append(pixelDimension[pixel])

    with open('levelOneOutput.csv', 'w', newline='') as f:
        writer = csv.writer(f)

        for anomaly in anomalies:
            writer.writerow(anomaly)
