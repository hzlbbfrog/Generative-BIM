import xlrd
import xlwt
#import cv2
import numpy as np
import copy
from PIL import Image
import matplotlib.pyplot as plt


def RGB_loader(Image_path):
    image = Image.open(Image_path) # image 对象
    image = image.convert('RGB') # RGB channel
    image = np.array(image) # image对象转成数组
    return(image)


def Flip_image(img, H, W):

    img_flip = np.full((H,W,3), 255)

    for i in range(H):
        img_flip[i,:,:] = img[H-1-i,:,:]

    return img_flip


def Is_red(i, j, Image):
    if Image[i,j,0] == 255 and Image[i,j,1] == 0 and Image[i,j,2] == 0:
        return 1
    else:
        return 0


def Line_is_red(line, left, Width, Image):
    for i in range(Width):
        if not Is_red(line, left+i, Image):
            return 0
    return 1
    

def Find_Width_Height(H, W, top, left, Image, Used):
    """_summary_

    Args:
        top (_type_): coordinate
        left (_type_): coordinate
        Image (_type_): Image data
        Used (_type_): Flag data
    """
    Width = 1
    if (left+Width < W):
        while Is_red(top, left+Width, Image):
            Width += 1
            if left+Width >= W:
                break
    
    Height = 1
    if (top+Height < H):
        while Line_is_red(top+Height, left, Width, Image):
            Height += 1
            if top+Height >= H:
                break
    
    return Width, Height    


def From_coordinate_to_Wall(Ratio, top, left, Wall_Width, Wall_Height):
    if Wall_Width <= Wall_Height:
        Wall_direction = 'Y'
    else:
        Wall_direction = 'X'
    
    if Wall_direction == 'Y':
        Start_x = left*Ratio + Wall_Width/2*Ratio
        Start_y = top*Ratio + 0.5*Ratio
        End_x = Start_x
        End_y = Start_y + (Wall_Height-1)*Ratio              
        Length = End_y - Start_y
    else:
        Start_x = left*Ratio + 0.5*Ratio
        Start_y = top*Ratio + Wall_Height/2*Ratio
        End_x = Start_x + (Wall_Width-1)*Ratio
        End_y = Start_y
        Length = End_x - Start_x
    return (Start_x, Start_y), (End_x, End_y), (Wall_direction, Length)


def From_Wall_to_text(StartPoint, EndPoint, Direction):
    
    # Line(StartPoint = Point(X = -22050.199, Y = -5635.206, Z = 29800.000), EndPoint = Point(X = -22050.199, Y = 5314.794, Z = 29800.000), Direction = Vector(X = 0.000, Y = 10950.000, Z = 0.000, Length = 10950.000))
         
    StartPoint_string = f"Line(StartPoint = Point(X = {StartPoint[0]:f}, Y = {StartPoint[1]:f}, Z = 0.0), "
    EndPoint_string = f"EndPoint = Point(X = {EndPoint[0]:f}, Y = {EndPoint[1]:f}, Z = 0.0), "
    
    if Direction[0] == 'X':
        Direction_string = f"Direction = Vector(X = {Direction[1]:f}, Y = 0.000, Z = 0.000, Length = {abs(Direction[1]):f}))"
    else:
        Direction_string = f"Direction = Vector(X = 0.000, Y = {Direction[1]:f}, Z = 0.000, Length = {abs(Direction[1]):f}))"
    
    text = StartPoint_string + EndPoint_string + Direction_string
    return text


def Save_Excel_file(File_name, Wall_List):
    Wall_book = xlwt.Workbook(encoding='utf-8')
    Wall_sheet = Wall_book.add_sheet('Sheet1')
    
    for i in range(len(Wall_List)):
        Wall_sheet.write(i,0,Wall_List[i])
    
    Wall_book.save(File_name)


if __name__ =="__main__":
    Folder = './'
    Image_name = 'test (1)_7degree.png'
    Image = RGB_loader(Folder+Image_name) # print(Image_selected.shape) # (352, 352, 3)
    H = Image.shape[0]
    W = Image.shape[1]
    
    Image = Flip_image(Image, H, W)
    
    Ratio = 30 # Real distance = pixel * Ratio
    Used = np.zeros((H,W))
    Wall_List = []
    
    for i in range(H):
        for j in range(W):
            if (Is_red(i, j, Image)) and (not Used[i,j]):
                top = i
                left = j
                Block_Width, Block_Height = Find_Width_Height(H, W, top, left, Image, Used)
                Used[i:i+Block_Height, j:j+Block_Width] = 1
                StartPoint, EndPoint, Direction = From_coordinate_to_Wall(Ratio, top, left, Block_Width, Block_Height)
                Wall_List.append(From_Wall_to_text(StartPoint, EndPoint, Direction))

    # Excel file
    Excel_file_name = 'Shear_walls.xls'
    Save_Excel_file(Folder+Excel_file_name, Wall_List)

    
              

                
        
                
                
                