# - Welcome Message

# * Welcome message subroutine
def welcome():
    data = input("Enter your name")
    user = data.capitalize().strip()
    print(f"Welcome - {user}")
    print("Demo cities to choose from --- London - New York - Tokyo - Sydney - Paris ---")

# * Goodby message subroutine
def thank_msg():
    print("Thank you for using our Application")


