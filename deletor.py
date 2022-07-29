import requests
import os
import time
from colorama import Fore



print(f"""{Fore.CYAN}
░██╗░░░░░░░██╗███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗  ███████╗██╗░░░██╗░█████╗░██╗░░██╗███████╗██████╗░
░██║░░██╗░░██║██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝  ██╔════╝██║░░░██║██╔══██╗██║░██╔╝██╔════╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██████╦╝███████║██║░░██║██║░░██║█████═╝░  █████╗░░██║░░░██║██║░░╚═╝█████═╝░█████╗░░██████╔╝
░░████╔═████║░██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔═██╗░  ██╔══╝░░██║░░░██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ██║░░░░░╚██████╔╝╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝


                                                                                    Made by SwiftAU#1000
                                                                            DM if you have any issues with the code
""")




webhook = input(f"{Fore.CYAN}Input the webhook: ")

time.sleep(0.5)
main = input("""Please Select an option:
[+] 2. Delete a webhook
""")

resp = requests.delete(webhook)
def deleter():
    time.sleep(1)
    resp = requests.delete(webhook)
if resp.status_code == 204:
    print(f"{Fore.GREEN}[DELETE] Successfully deleted the webhook!")
if resp.status_code == 404:
    print(f"{Fore.RED}[ERROR] This webhook is either is wrong or invalid")

if main == '1':
    deleter()
