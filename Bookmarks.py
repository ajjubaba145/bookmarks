import os

def multi_cookies_bookmark():
    os.system('git pull')
    os.system('chmod 777 cookiesbookmark')
    os.system('./cookiesbookmark')

def multi_token_bookmark():
    os.system('git pull')
    os.system('chmod 777 tukanbookmark')
    os.system('./tukanbookmark')

# Main menu function
def main_menu():
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

# Function placeholder for follow_owner_fb_account
def follow_owner_fb_account():
    print("Follow Owner Fb Account logic goes here.")

# Run the main menu
main_menu()
          
