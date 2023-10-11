#!/usr/bin/python3

def roman_to_int(roman_string):
    ones = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7,
            'VIII': 8,
            'IX': 9,
            }
    tens = {'X': 10,
            'XX': 20,
            'XXX': 30,
            'XL': 40,
            'L': 50,
            'LX': 60,
            'LXX': 70,
            'LXXX': 80,
            'XC': 90,
            }
    hundreds = {'C': 100,
                'CC': 200,
                'CCC': 300,
                'CD': 400,
                'D': 500,
                'DC': 600,
                'DCC': 700,
                'DCCC': 800,
                'CM': 900,
                }
    thousands = {'M': 1000,
                 'MM': 2000,
                 'MMM': 3000
                 }
    one, ten, hundred, thousand, count, rom = 0, 0, 0, 0, 0, ''
    for i in roman_string:
        count += 1
        rom += i
        if rom in thousands.keys():
            thousand = thousands[rom]
        elif rom in hundreds.keys():
            hundred = hundreds[rom]
        elif rom in tens.keys():
            ten = tens[rom]
        elif rom in ones.keys():
            one = ones[rom]
        elif count == len(roman_string):
            rom = i
            one = ones[rom]
        else:
            rom = i
    return thousand + hundred + ten + one
