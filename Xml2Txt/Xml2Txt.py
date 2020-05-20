import os
import glob
import xml.etree.ElementTree as ET

classes = ['Enemy']


def convert(size, box):
    print(size)
    print(box)
    dw = 1./size[0]
    dh = 1./size[1]
    print('dw,dh',dw,dh)
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


def convert_annotation(xml):
    inFile = open(xml,encoding='UTF-8')
    #outFile = open(xml.replace('xml', 'txt'), 'w', encoding='UTF-8')
    
    tree = ET.parse(inFile)

    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    
    if w == 0:
        print(xml)
        return

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        outFile = open(xml.replace('xml', 'txt'), 'a+', encoding='UTF-8')
        outFile.write(" ".join([str(a) for a in bb]) + '\n')


xmlDir = 'D:\\sample\\test'

xmlList = glob.glob(os.path.join(xmlDir, '*.xml'))

listFile = open('train-2.txt', 'w', encoding='UTF-8' )
for xml in xmlList:
    listFile.write(xml.replace('xml', 'png')+'\n')
    convert_annotation(xml)
listFile.close()
