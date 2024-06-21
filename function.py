username = input("Enter your username:")
Email = input("Enter your email address:")
password = input("Enter a very strong password:")
digit = input("Enter your phone number:")
year = input("Enter your year of birth:")
def open_account(username,Email,password,digit,year):
    return(f"welcome {username} your information are as follows {username}, {Email},{password},{digit},{year}")
print(open_account(username,Email,password,digit,year))
