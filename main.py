import time
import random
from telegraph import Telegraph
from colorama import Fore, Style, init

# Инициализация Colorama
init(autoreset=True)

def generate_glitch_text(length):
    glitch_chars = ['�', '▒', '▓', '░', '█', '▌', '▐', '▖', '▗', '▘', '▝', '▞', '▟', '▃', '▄', '▅', '▆', '▇']
    return ''.join(random.choice(glitch_chars) for _ in range(length))

print(f'https://github.com/Goidaa/telegraph-flooder/')
author_name = input("Enter author name: ")
custom_text = input("Enter text: ")
page_title = input("Enter page title: ")

account_names = ['GFL', 'GFL_GOOON', 'GFL_GONNDYYYY']
accounts = []
for account_name in account_names:
    account = Telegraph()
    account.create_account(short_name=account_name)
    accounts.append(account)
    print(Fore.MAGENTA + f'Created new account: {account_name}')  

i = 1
while True:
    if i % 10 == 0:
        new_account_name = f'Gondy_Fld_{i // 10}'
        new_account = Telegraph()
        new_account.create_account(short_name=new_account_name)
        accounts.append(new_account)
        print(Fore.MAGENTA + f'Created new account: {new_account_name}')  

    account = accounts[i % len(accounts)]
    title = f'{page_title} {i}'
    glitch_text = generate_glitch_text(10000)
    content = f'<p>{custom_text}</p><p>{glitch_text}</p>'

    try:
        response = account.create_page(
            title=title,
            html_content=content,
            author_name=author_name,
            author_url="https://dsc.gg/rcteam"
        )
        print(Fore.LIGHTGREEN_EX + f'Created page {i}: https://telegra.ph/' + response['path'])  
        
    except Exception as e:
        print(Fore.RED + f'Error for account {account_names[i % len(accounts)]}: {e}')  
    
    i += 1
    time.sleep(0.0001)
