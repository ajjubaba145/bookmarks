import os
import sys
import time
import random
import hashlib
from urllib.parse import quote
import requests
from colorama import init, Fore, Style

# Function to install missing modules
def install_modules():
    try:
        import colorama
        import requests
    except ImportError:
        print("Installing required modules...")
        os.system('pip install colorama requests')
        print("Modules installation done.")

# Check and install modules if necessary
install_modules()

# Function to clear terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII art logo with color animation
logo = """
      $$$$$$$\  $$\   $$\  $$$$$$\  $$\       $$\      $$\  $$$$$$\        
      $$  __$$\ $$ |  $$ |$$  __$$\ $$ |      $$ | $\  $$ |$$  __$$\       
      $$ |  $$ |$$ |  $$ |$$ /  $$ |$$ |      $$ |$$$\ $$ |$$ /  $$ |      
      $$$$$$$\ |$$$$$$$$ |$$ |  $$ |$$ |      $$ $$ $$\$$ |$$$$$$$$ |      
      $$  __$$\ $$  __$$ |$$ |  $$ |$$ |      $$$$  _$$$$ |$$  __$$ |      
      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$$  / \$$$ |$$ |  $$ |      
      $$$$$$$  |$$ |  $$ | $$$$$$  |$$$$$$$$\ $$  /   \$$ |$$ |  $$ |      
      \_______/ \__|  \__| \______/ \________|\__/     \__|\__|  \__|      
                                                                           
                                                                           
                                                                           
"""

# Function to print colored logo with animation
def print_colored_logo(logo):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    for i, line in enumerate(logo.split("\n")):
        time.sleep(0.1)
        color = random.choice(colors)
        sys.stdout.write("\033[1m")  # Bold text
        for char in line:
            sys.stdout.write(color + char)
            sys.stdout.flush()
            time.sleep(0.002)
        sys.stdout.write("\n")
        sys.stdout.flush()

# Function to generate unique ID
def get_unique_id():
    try:
        return hashlib.sha256((str(os.getuid()) + os.getlogin()).encode()).hexdigest()
    except Exception as e:
        print(f"Error generating unique ID: {e}")
        exit(1)

# Function to check permission
def check_permission(unique_key):
    while True:
        try:
            response = requests.get("https://pastebin.com/raw/XmhGtu3A")
            if response.status_code == 200:
                data = response.text
                permission_list = [line.strip() for line in data.split("\n") if line.strip().find(unique_key) != -1]
                if not permission_list:
                    print("\033[1;31mChecking Approval.....\033[0m")
                    time.sleep(10)
                else:
                    print("\033[1;92m[√] Permission granted. Your Key Was Approved.\033[0m")
                    break
            else:
                print(f"Failed to fetch permissions list. Status code: {response.status_code}")
                time.sleep(10)
        except Exception as e:
            print(f"Error checking permission: {e}")
            time.sleep(10)

# Function to send approval request
def send_approval_request(unique_key):
    try:
        clear_screen()  # Clear the screen before printing
        print_colored_logo(logo)
        print_key_info(unique_key)  # Display the unique key info
        print("\033[1;97m[•] Sending approval Key...\033[0m")
        input("\033[1;97m[•] Press enter to send approval Key:\033[0m")
        message = f"Hello, Bhola sir! Please Approve My Token is :: {unique_key}"
        os.system(f"am start https://wa.me/+917240213498?text={quote(message)} >/dev/null 2>&1")
        print("\033[1;97mWhatsApp opened with approval request. Waiting for approval...\033[0m")
    except Exception as e:
        print(f"Error sending approval request: {e}")
        exit(1)

# Function to print key information in a box
def print_key_info(unique_key):
    key_info = f"Your Key is :: {unique_key}"
    box_width = len(key_info) + 4  # Adjust box width based on content length
    print(Fore.YELLOW + Style.BRIGHT + "+" + "-"*(box_width-2) + "+")
    print(f"| {key_info} |")
    print("+" + "-"*(box_width-2) + "+" + Style.RESET_ALL)

# Function to handle multi cookies bookmark
def multi_cookies_bookmark():
    os.system('git pull')
    os.system('chmod 777 cookiesbookmark')
    os.system('./cookiesbookmark')

# Function to handle multi token bookmark
def multi_token_bookmark():
    os.system('git pull')
    os.system('chmod 777 tukanbookmark')
    os.system('./tukanbookmark')

# Function to follow owner's Facebook account
def follow_owner_fb_account():
    clear_screen()  # Clear screen before opening owner's profile
    owner()
    input("\nPress Enter to return to the main menu...")
    main_menu()  # Return to main menu after opening owner's profile

# Function to open owner's Facebook profile
def owner():
    os.system("xdg-open https://www.facebook.com/profile.php?id=100083151961248")  # Replace with the actual owner's Facebook profile link

# Function for the main menu
def main_menu():
    clear_screen()  # Clear the screen before printing menu
    print_colored_logo(logo)  # Print the animated and colored logo
    print("[1] Multi Cookies Bookmark")
    print("[2] Multi Token Bookmark")
    print("[3] Follow Owner Fb Account")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        multi_cookies_bookmark()
    elif choice == '2':
        multi_token_bookmark()
    elif choice == '3':
        follow_owner_fb_account()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

# Function to integrate pre-main operations
def pre_main():
    unique_key = get_unique_id()
    send_approval_request(unique_key)  # Send the approval request
    check_permission(unique_key)  # Check for permission after sending request
    clear_screen()  # Clear screen after permission is granted
    main_menu()  # Display the main menu after permission is granted

# Run the pre-main function
pre_main()
