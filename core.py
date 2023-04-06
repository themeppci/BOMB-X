import os
import time

from phone_bomb import phone_bomb # sms/call bomb

os.system('cls')

def logo():
    print(r'''
  ____    ____   __  __  ____             __   __
 |  _ \  / __ \ |  \/  ||  _ \            \ \ / /
 | |_) || |  | || \  / || |_) |   ______   \ V / 
 |  _ < | |  | || |\/| ||  _ <   |______|   > <  
 | |_) || |__| || |  | || |_) |            / . \ 
 |____/  \____/ |_|  |_||____/            /_/ \_\

    ''')



logo()
time.sleep(1)
print('\nTELEGRAM: @MEPPCI')
time.sleep(3)
os.system('cls')

logo()
print('\n[1] PHONE BOMBER\n[2] ...\n[3] ...')

mode = int(input('[#] Mode: '))
if not mode in range(1, 4):
    print('[!] Wrong mode')
    time.sleep(3)
    exit()

if mode == 1:
    is_error = False
    os.system('cls')
    logo()
    phone = input('[#] Enter phone number (format: 9030001234): ')
    if len(phone) == 10 and phone[0] != 7:
        cyc = int(input('[#] Enter how many cycles (there is no point in more than 3): '))
        if cyc > 0:
            bomb_type = input('[#] Enter bomb type (SMS/CALL): ')
            bomb_type = bomb_type.lower()
            if bomb_type in ['sms', 'call']:
                fx = phone_bomb(phone=phone, bomb_type=bomb_type, cyc=cyc)
            else:
                print('[#] Mode incorrect')
                is_error = True
        else:
            print('[#] Cycles number incorrect')
            is_error = True
    else:
        print('[#] Phone incorrect')
        is_error = True
    if is_error:
        fx = '[!] Error occured.'
    os.system('cls')
    logo()
    print(fx)
    print('[#] Press any key to continue.')
    input()
