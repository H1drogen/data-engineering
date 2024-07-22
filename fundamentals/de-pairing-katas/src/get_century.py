def get_century(year):
    ending=''
    century=int(year/100)+1
    last_digit=century%10
    if last_digit== 1:
        ending='st'
    elif last_digit== 2:
        ending='nd'
    elif last_digit== 3:
        ending='rd'
    else:
        ending='th'
    return f'{century}{ending}'
