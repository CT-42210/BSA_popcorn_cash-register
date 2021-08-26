import sys
import time
import os

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)


def instalation_check():
    setup_file = open("setup.txt", "w")
    setup_file.write("setup completion = false \n")
    setup_file.write("\n Version 0.1")
    setup_file.close()


def log_creation():
    setup_log = open("setup_log.txt", "w")
    setup_log.write("logging setup at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()


def pop_type_file_setup():
    profiles_file = open("pop_type.txt", "w")
    profiles_file.write("file test")
    profiles_file.close()

    profiles_file = open("pop_type.txt")
    content = profiles_file.read()

    if content == ("file test"):
        profiles_file.close()
        print("popcorn type file created succesfuly")
        profiles_file = open("pop_type.txt", "w")
        profiles_file.write("Popcorn Types: \n")
        profiles_file.close()
        pop_type_file_complete()
    else:
        pop_type_setup_err()


def pop_type_file_complete():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("popcorn type text file created succesfully at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)


def pop_type_setup_err():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("popcorn type text file failed at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)

    attempt_number = 0
    attempt_number = +1

    print("setup has failed")
    print(attempt_number)
    print("time(s). retrying in 5 seconds")
    time.sleep(5)
    pop_type_file_setup()

    if attempt_number > 3:
        print("Setup has failed more than 3 times; exiting program")
        time.sleep(5)
        sys.exit()
    else:
        pass


def pop_quantity_file_setup():
    profiles_file = open("pop_quantity.txt", "w")
    profiles_file.write("file test")
    profiles_file.close()

    profiles_file = open("pop_quantity.txt")
    content = profiles_file.read()

    if content == ("file test"):
        profiles_file.close()
        print("popcorn quantity file created succesfuly")
        profiles_file = open("pop_quantity.txt", "w")
        profiles_file.write("Popcorn Type Quantity's: \n")
        profiles_file.close()
        pop_quantity_file_complete()
    else:
        pop_quantity_setup_err()


def pop_quantity_file_complete():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("popcorn quantity text file created succesfully at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)


def pop_quantity_setup_err():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("popcorn quantity text file failed at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)

    attempt_number = 0
    attempt_number = +1

    print("setup has failed")
    print(attempt_number)
    print("time(s). retrying in 5 seconds")
    time.sleep(5)
    pop_quantity_file_setup()

    if attempt_number > 3:
        print("Setup has failed more than 3 times; exiting program")
        time.sleep(5)
        sys.exit()
    else:
        pass

def pop_price_file_setup():
    profiles_file = open("pop_price.txt", "w")
    profiles_file.write("file test")
    profiles_file.close()

    profiles_file = open("pop_price.txt")
    content = profiles_file.read()

    if content == ("file test"):
        profiles_file.close()
        print("popcorn price file created succesfuly")
        profiles_file = open("pop_price.txt", "w")
        profiles_file.write("Popcorn Type Prices: \n")
        profiles_file.close()
        pop_price_file_complete()
    else:
        pop_price_setup_err()


def pop_price_file_complete():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("popcorn quantity text file created succesfully at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)


def pop_price_setup_err():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("popcorn quantity text file failed at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)

    attempt_number = 0
    attempt_number = +1

    print("setup has failed")
    print(attempt_number)
    print("time(s). retrying in 5 seconds")
    time.sleep(5)
    pop_price_file_setup()

    if attempt_number > 3:
        print("Setup has failed more than 3 times; exiting program")
        time.sleep(5)
        sys.exit()
    else:
        pass

def sales_file_setup():
    profiles_file = open("sales.txt", "w")
    profiles_file.write("file test")
    profiles_file.close()

    profiles_file = open("sales.txt")
    content = profiles_file.read()

    if content == ("file test"):
        profiles_file.close()
        print("sales file created succesfuly")
        profiles_file = open("sales.txt", "w")
        profiles_file.write("sales: \n")
        profiles_file.close()
        sales_file_complete()
    else:
        sales_setup_err()

def sales_file_complete():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("sales text file created succesfully at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)

def sales_setup_err():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("sales text file failed at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)

    attempt_number = 0
    attempt_number = +1

    print("setup has failed")
    print(attempt_number)
    print("time(s). retrying in 5 seconds")
    time.sleep(5)
    pop_type_file_setup()

    if attempt_number > 3:
        print("Setup has failed more than 3 times; exiting program")
        time.sleep(5)
        sys.exit()
    else:
        pass


def pop_type_exec_file_setup():
    profiles_file = open("pop_type_exec.txt", "w")
    profiles_file.write("file test")
    profiles_file.close()

    profiles_file = open("pop_type_exec.txt")
    content = profiles_file.read()

    if content == ("file test"):
        profiles_file.close()
        print("popcorn type executable file created succesfuly")
        profiles_file = open("pop_type_exec.txt", "w")
        profiles_file.write("pop_type_exec: \n")
        profiles_file.close()
        pop_type_exec_file_complete()
    else:
        pop_type_exec_setup_err()


def pop_type_exec_file_complete():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("popcorn type executable text file created succesfully at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)


def pop_type_exec_setup_err():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("popcorn type executable text file failed at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)

    attempt_number = 0
    attempt_number = +1

    print("setup has failed")
    print(attempt_number)
    print("time(s). retrying in 5 seconds")
    time.sleep(5)
    pop_type_file_setup()

    if attempt_number > 3:
        print("Setup has failed more than 3 times; exiting program")
        time.sleep(5)
        sys.exit()
    else:
        pass


def pop_type_sold_file_setup():
    profiles_file = open("pop_type_sold.txt", "w")
    profiles_file.write("file test")
    profiles_file.close()

    profiles_file = open("pop_type_sold.txt")
    content = profiles_file.read()

    if content == ("file test"):
        profiles_file.close()
        print("popcorn type sold file created succesfuly")
        profiles_file = open("pop_type_sold.txt", "w")
        profiles_file.write("pop_type_sold: \n")
        profiles_file.close()
        pop_type_sold_file_complete()
    else:
        pop_type_sold_setup_err()


def pop_type_sold_file_complete():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("popcorn type sold text file created succesfully at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)


def pop_type_sold_setup_err():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("popcorn type sold text file failed at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)

    attempt_number = 0
    attempt_number = +1

    print("setup has failed")
    print(attempt_number)
    print("time(s). retrying in 5 seconds")
    time.sleep(5)
    pop_type_file_setup()

    if attempt_number > 3:
        print("Setup has failed more than 3 times; exiting program")
        time.sleep(5)
        sys.exit()
    else:
        pass


def account_creation():
    print("Welcome! please create your account below.\n If you wish to start over, type [restart]. \n ")

    time.sleep(1)

    username = "enter the account username: \n $ "
    first_name = "enter your first name: \n $ "
    last_name = "enter your last name: \n $ "
    email = "enter an email. (this is optional.) \n $ "

    account_file = open("Account.txt", "w")
    account_file.write("Account:\n")
    account_file.write(input(str(username)))
    account_file.write("\n")
    time.sleep(1)
    account_file.write(input(str(first_name)))
    account_file.write("\n")
    time.sleep(1)
    account_file.write(input(str(last_name)))
    account_file.write("\n")
    time.sleep(1)
    account_file.write(input(str(email)))
    account_file.write("\n")
    time.sleep(1)
    account_file.close()

    print("are these cridentials correct? \n")
    account_file = open("Account.txt","r")
    confirmation = account_file.read()

    print(confirmation)

    if input(str("type [y] if they are correct, and [n] if they are not.")) == "y":
        account_file.close()

        setup_log = open("setup_log.txt", "a")
        setup_log.write("account set up sucessfuly at:")
        setup_log.write(current_time)
        setup_log.write("\n check [Account.txt] for cridentals. \n")
        setup_log.close()
    elif input == "n":
        setup_log = open("setup_log.txt", "a")
        setup_log.write("account set up restarted at:")
        setup_log.write(current_time)
        setup_log.write("\n credentials are as follows: \n", )
        setup_log.write(confirmation, )
        setup_log.write("\n")
        setup_log.close()
    else:
        print("invalid response,starting again...")
        time.sleep(3)
        account_creation()


def setup():
    instalation_check()
    log_creation()
    pop_type_file_setup()
    pop_quantity_file_setup()
    pop_price_file_setup()
    sales_file_setup()
    account_creation()

    setup_file = open("setup.txt","w")
    setup_file.write("setup completion = \n true")
    setup_file.write("\n Version 0.1")
    print("setup complete! starting full aplication...")
    time.sleep(5)
