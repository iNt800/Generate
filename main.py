import random
import cv2

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

class Purpose:
    
    def __distribution():
        if str(generate['one']) == '1':
            s1 = "A"
        elif str(generate['one']) == '2':
            s1 = "L"
        elif str(generate['one']) == '3':
            s1 = "P"
        elif str(generate['one']) == '4':
            s1 = "/"
        elif str(generate['one']) == '5':
            s1 = "z"
            
        if str(generate['two']) == '1':
            s2 = "A"
        elif str(generate['two']) == '2':
            s2 = "L"
        elif str(generate['two']) == '3':
            s2 = "P"
        elif str(generate['two']) == '4':
            s2 = "/"
        elif str(generate['two']) == '5':
            s2 = "z"
            
        if str(generate['three']) == '1':
            s3 = "A"
        elif str(generate['three']) == '2':
            s3 = "L"
        elif str(generate['three']) == '3':
            s3 = "P"
        elif str(generate['three']) == '4':
            s3 = "/"
        elif str(generate['three']) == '5':
            s3 = "z"
            
        if str(generate['four']) == '1':
            s4 = "A"
        elif str(generate['four']) == '2':
            s4 = "L"
        elif str(generate['four']) == '3':
            s4 = "P"
        elif str(generate['four']) == '4':
            s4 = "/"
        elif str(generate['four']) == '5':
            s4 = "z"
            
        if str(generate['five']) == '1':
            s5 = "A"
        elif str(generate['five']) == '2':
            s5 = "L"
        elif str(generate['five']) == '3':
            s5 = "P"
        elif str(generate['five']) == '4':
            s5 = "/"
        elif str(generate['five']) == '5':
            s5 = "z"

        space = 'Sid: '
        
        s = space + s1 + s2 + s3 + s4 + s5
        
        return s
    
    final_sid = __distribution()

def final_result():
    
    result = ''

    result += str(generate['one']) + ' ' + str(generate['two']) + ' ' + str(generate['three']) + ' ' +  str(generate['four']) + ' ' +  str(generate['five'])

    sid = Purpose.final_sid
    
    print(result, sid)

def check_sel():
    if sel == 'г':
        final_result()
    elif sel == 'с':
        (first, *(f, m, l), last) = input('Введите сид: ')
        if first.format(*vars()) == 'A':
            gen1 = '1'
        elif first.format(*vars()) == 'L':
            gen1 = '2'
        elif first.format(*vars()) == 'P':
            gen1 = '3'
        elif first.format(*vars()) == '/':
            gen1 = '4'
        elif first.format(*vars()) == 'z':
            gen1 = '5'
        if f.format(*vars()) == 'A':
            gen2 = '1'
        elif f.format(*vars()) == 'L':
            gen2 = '2'
        elif f.format(*vars()) == 'P':
            gen2 = '3'
        elif f.format(*vars()) == '/':
            gen2 = '4'
        elif f.format(*vars()) == 'z':
            gen2 = '5'
        if m.format(*vars()) == 'A':
            gen3 = '1'
        elif m.format(*vars()) == 'L':
            gen3 = '2'
        elif m.format(*vars()) == 'P':
            gen3 = '3'
        elif m.format(*vars()) == '/':
            gen3 = '4'
        elif m.format(*vars()) == 'z':
            gen3 = '5'
        if l.format(*vars()) == 'A':
            gen4 = '1'
        elif l.format(*vars()) == 'L':
            gen4 = '2'
        elif l.format(*vars()) == 'P':
            gen4 = '3'
        elif l.format(*vars()) == '/':
            gen4 = '4'
        elif l.format(*vars()) == 'z':
            gen4 = '5'
        if last.format(*vars()) == 'A':
            gen5 = '1'
        elif last.format(*vars()) == 'L':
            gen5 = '2'
        elif last.format(*vars()) == 'P':
            gen5 = '3'
        elif last.format(*vars()) == '/':
            gen5 = '4'
        elif last.format(*vars()) == 'z':
            gen5 = '5'
        
        gen = f'{gen1} {gen2} {gen3} {gen4} {gen5} Если вы забыли то сид: {first.format(*vars())}{f.format(*vars())}{m.format(*vars())}{l.format(*vars())}{last.format(*vars())}'
            
        print(gen)
    else:
        print('Вы ввели не то!')


if __name__ == '__main__':
    
    sel = input('Генерировать или Ввести сид? (г или с): ')
    
    check_sel()
    