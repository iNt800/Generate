import random
import cv2
import numpy as np
from PIL import Image, ImageDraw

photo = np.zeros((600, 600, 3), dtype='uint8')

photo[:] = 255, 255, 255

one = random.randint(1, 5)

two = random.randint(1, 5)

three = random.randint(1, 5)

four = random.randint(1, 5)
    
five = random.randint(1, 5)

generate = {
    'one': one,
    'two': two,
    'three': three,
    'four': four,
    'five': five,
}

def final_result():
        if str(generate['one']) == '1':
            photo[200:300, 250:400] = 54, 16, 53
            s1 = "A"
        elif str(generate['one']) == '2':
            photo[370:480, 400:550] = 204, 57, 57
            s1 = "L"
        elif str(generate['one']) == '3':
            photo[300:500, 200:300] = 53, 43, 102
            s1 = "P"
        elif str(generate['one']) == '4':
            photo[100:300, 200:400] = 65, 99, 94
            s1 = "/"
        elif str(generate['one']) == '5':
            photo[200:300, 400:550] = 48, 35, 79
            s1 = "z"
            
        if str(generate['two']) == '1':
            photo[100:150, 200:280] = 119, 201, 105
            s2 = "A"
        elif str(generate['two']) == '2':
            photo[250:400, 300:450] = 57, 123, 204
            s2 = "L"
        elif str(generate['two']) == '3':
            photo[200:400, 150:500] = 152, 204, 214
            s2 = "P"
        elif str(generate['two']) == '4':
            photo[410:580, 250:400] = 0, 162, 250
            s2 = "/"
        elif str(generate['two']) == '5':
            photo[200:280, 200:310] = 255, 0, 136
            s2 = "z"
            
        if str(generate['three']) == '1':
            photo[400:500, 400:550] = 20, 128, 38
            s3 = "A"
        elif str(generate['three']) == '2':
            photo[370:480, 200:300] = 35, 130, 103
            s3 = "L"
        elif str(generate['three']) == '3':
            photo[370:480, 140:322] = 93, 0, 255
            s3 = "P"
        elif str(generate['three']) == '4':
            photo[167:310, 300:450] = 51, 133, 16
            s3 = "/"
        elif str(generate['three']) == '5':
            photo[170:350, 200:400] = 255, 247, 0
            s3 = "z"
            
        if str(generate['four']) == '1':
            photo[150:300, 300:450] = 30, 37, 176
            s4 = "A"
        elif str(generate['four']) == '2':
            photo[200:280, 150:300] = 227, 157, 188
            s4 = "L"
        elif str(generate['four']) == '3':
            photo[167:310, 100:300] = 69, 49, 62
            s4 = "P"
        elif str(generate['four']) == '4':
            photo[100:150, 150:300] = 143, 186, 0
            s4 = "/"
        elif str(generate['four']) == '5':
            photo[300:450, 410:580] = 255, 115, 0
            s4 = "z"
            
        if str(generate['five']) == '1':
            photo[370:480, 200:280] = 0, 0, 0
            s5 = "A"
        elif str(generate['five']) == '2':
            photo[400:550, 100:150] = 84, 0, 3
            s5 = "L"
        elif str(generate['five']) == '3':
            photo[410:580, 100:150] = 22, 46, 25
            s5 = "P"
        elif str(generate['five']) == '4':
            photo[140:322, 200:280] = 0, 255, 187
            s5 = "/"
        elif str(generate['five']) == '5':
            photo[500:600, 240:500] = 60, 37, 194
            s5 = "z"

        space = 'Sid: '
        
        s = space + s1 + s2 + s3 + s4 + s5
    
        result = ''

        result += str(generate['one']) + ' ' + str(generate['two']) + ' ' + str(generate['three']) + ' ' +  str(generate['four']) + ' ' +  str(generate['five'])

        sid = s
    
        print(result, sid)

def check_sel():
    if sel == 'г':
        final_result()
    elif sel == 'с':
        (first, *(f, m, l), last) = input('Введите сид: ')
        if first.format(*vars()) == 'A':
            photo[200:300, 250:400] = 54, 16, 53
            gen1 = '1'
        elif first.format(*vars()) == 'L':
            photo[370:480, 400:550] = 204, 57, 57
            gen1 = '2'
        elif first.format(*vars()) == 'P':
            photo[300:500, 200:300] = 53, 43, 102
            gen1 = '3'
        elif first.format(*vars()) == '/':
            photo[100:300, 200:400] = 65, 99, 94
            gen1 = '4'
        elif first.format(*vars()) == 'z':
            photo[200:300, 400:550] = 48, 35, 79
            gen1 = '5'
            
        if f.format(*vars()) == 'A':
            photo[100:150, 200:280] = 119, 201, 105
            gen2 = '1'
        elif f.format(*vars()) == 'L':
            photo[250:400, 300:450] = 57, 123, 204
            gen2 = '2'
        elif f.format(*vars()) == 'P':
            photo[200:400, 150:500] = 152, 204, 214
            gen2 = '3'
        elif f.format(*vars()) == '/':
            photo[410:580, 250:400] = 0, 162, 250
            gen2 = '4'
        elif f.format(*vars()) == 'z':
            photo[200:280, 200:310] = 255, 0, 136
            gen2 = '5'
            
        if m.format(*vars()) == 'A':
            photo[400:500, 400:550] = 20, 128, 38
            gen3 = '1'
        elif m.format(*vars()) == 'L':
            photo[370:480, 200:300] = 35, 130, 103
            gen3 = '2'
        elif m.format(*vars()) == 'P':
            photo[370:480, 140:322] = 93, 0, 255
            gen3 = '3'
        elif m.format(*vars()) == '/':
            photo[167:310, 300:450] = 51, 133, 16
            gen3 = '4'
        elif m.format(*vars()) == 'z':
            photo[170:350, 200:400] = 255, 247, 0
            gen3 = '5'
            
        if l.format(*vars()) == 'A':
            photo[150:300, 300:450] = 30, 37, 176
            gen4 = '1'
        elif l.format(*vars()) == 'L':
            photo[200:280, 150:300] = 227, 157, 188
            gen4 = '2'
        elif l.format(*vars()) == 'P':
            photo[167:310, 100:300] = 69, 49, 62
            gen4 = '3'
        elif l.format(*vars()) == '/':
            photo[100:150, 150:300] = 143, 186, 0
            gen4 = '4'
        elif l.format(*vars()) == 'z':
            photo[300:450, 410:580] = 255, 115, 0
            gen4 = '5'
            
        if last.format(*vars()) == 'A':
            photo[370:480, 200:280] = 0, 0, 0
            gen5 = '1'
        elif last.format(*vars()) == 'L':
            photo[400:550, 100:150] = 84, 0, 3
            gen5 = '2'
        elif last.format(*vars()) == 'P':
            photo[410:580, 100:150] = 22, 46, 25
            gen5 = '3'
        elif last.format(*vars()) == '/':
            photo[140:322, 200:280] = 0, 255, 187
            gen5 = '4'
        elif last.format(*vars()) == 'z':
            photo[500:600, 240:500] = 60, 37, 194
            gen5 = '5'
        
        gen = f'{gen1} {gen2} {gen3} {gen4} {gen5} Если вы забыли то сид: {first.format(*vars())}{f.format(*vars())}{m.format(*vars())}{l.format(*vars())}{last.format(*vars())}'
            
        print(gen)
    else:
        print('Вы ввели не то!')

if __name__ == '__main__':
    
    sel = input('Генерировать или ввести сид? г или с: ')
    
    check_sel()
    
    cv2.imshow('photo', photo)
    cv2.waitKey(0)