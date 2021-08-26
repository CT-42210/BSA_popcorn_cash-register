import time
import os

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)


def buffering():
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)


def sell():

    print("what item is being sold?")
    pop_type = open("pop_type.txt", "r")
    items = pop_type.read()
    print(items)
    item_number = input(str("enter the items number \n \n $"))

    with open("pop_type_exec.txt", "r") as executable:
        executable_read = executable.readlines()
        executable_string = int(item_number)
        executable_to_read = executable_read[executable_string]

    if executable_to_read != "ORDER":

        with open("pop_type.txt", "r") as item_1:
            item_read_1 = item_1.readlines()
            item_string_1 = int(item_number)
            item_to_read_1 = item_read_1[item_string_1]

        with open("pop_price.txt", "r") as item_2:
            item_read_2 = item_2.readlines()
            item_string_2 = int(item_number)
            item_to_read_2 = item_read_2[item_string_2]

        with open("pop_quantity.txt", "r") as item_3:
            item_read_3 = item_3.readlines()
            item_string_3 = int(item_number)
            item_to_read_3 = item_read_3[item_string_3]

        with open("pop_type_sold.txt", "r") as item_4:
            item_read_4 = item_4.readlines()
            item_string_4 = int(item_number)
            item_to_read_4 = item_read_4[item_string_4]

        print("Item:")
        print(item_to_read_1)
        print("Price:")
        print("$" + item_to_read_2)
        print("Ammount avalible to sell:")
        print(item_to_read_3)
        print("Ammount sold:")
        print(item_to_read_4)

        print("How many are you selling?")
        item_quantity = input("Enter the number here: \n \n $")

        with open("pop_quantity.txt", "r") as item_5:
            item_read_5 = item_5.readlines()
            item_string_5 = int(item_number)
            item_to_read_5 = item_read_5[item_string_5]

        with open("pop_type_sold.txt", "r") as item_6:
            item_read_6 = item_6.readlines()
            item_string_6 = int(item_number)
            item_to_read_6 = item_read_6[item_string_6]

        int_item_quantity = int(item_quantity)
        int_item_stock = int(item_to_read_5)
        int_item_sold = int(item_to_read_6)
        new_item_quantity = int_item_stock - int_item_quantity
        new_item_total_sold = int_item_sold + int_item_quantity

        with open("pop_quantity.txt", 'r') as f:
            get_all = f.readlines()

        with open("pop_quantity.txt", 'w') as f:
            for i, line in enumerate(get_all):
                if i == int(item_number):
                    f.writelines(str(new_item_quantity) + "\n")
                else:
                    f.writelines(line)

        with open("pop_type_sold.txt", 'r') as f:
            get_all = f.readlines()

        with open("pop_type_sold.txt", 'w') as f:
            for i, line in enumerate(get_all):
                if i == int(item_number):
                    f.writelines(str(new_item_total_sold) + "\n")
                else:
                    f.writelines(line)

        path = os.getcwd()
        name = "totals.txt"
        total_dollars_sold = 1
        total_products_sold = 2

        for root, dirs, files in os.walk(path):
            if name in files:
                with open(name, "r") as item_7:
                    item_read_7 = item_7.readlines()
                    item_string_7 = total_dollars_sold
                    item_to_read_7 = item_read_7[item_string_7]

                with open(name, "r") as item_8:
                    item_read_8 = item_8.readlines()
                    item_string_8 = total_products_sold
                    item_to_read_8 = item_read_8[item_string_8]

                    new_total = int(item_to_read_7) + int(item_to_read_2) * int(item_quantity)
                    new_sold = int(item_to_read_8) + int(item_quantity)

                with open(name, 'r') as f:
                    get_all = f.readlines()

                with open(name, 'w') as f:
                    for i, line in enumerate(get_all):
                        if i == int(total_dollars_sold):
                            f.writelines(str(new_total) + "\n")
                        else:
                            f.writelines(line)

                with open(name, 'r') as f:
                    get_all = f.readlines()

                with open(name, 'w') as f:
                    for i, line in enumerate(get_all):
                        if i == int(total_products_sold):
                            f.writelines(str(new_sold))
                        else:
                            f.writelines(line)
                break
            else:
                with open(name, "w") as item_9:
                    item_9.write("Totals: \n")
                    item_9.write("0\n")
                    item_9.write("0")

                new_total = int(item_to_read_2) * int(item_quantity)
                new_sold = int(item_quantity)

                with open(name, 'r') as f:
                    get_all = f.readlines()

                with open(name, 'w') as f:
                    for i, line in enumerate(get_all):
                        if i == int(total_dollars_sold):
                            f.writelines(str(new_total) + "\n")
                        else:
                            f.writelines(line)

                with open(name, 'r') as f:
                    get_all = f.readlines()

                with open(name, 'w') as f:
                    for i, line in enumerate(get_all):
                        if i == int(total_products_sold):
                            f.writelines(str(new_sold))
                        else:
                            f.writelines(line)
                break

        total_sale_price = int(item_to_read_2) * int(item_quantity)

        with open("sales.txt", "a") as sales:
            sales.write(f"\n ------------------------------------------------------------------ \n"
                        f"At {current_time}, \n {item_quantity} '{item_to_read_1}' was/were sold. \n "
                        f"Total is ${total_sale_price}. Total sales is ${new_total}. \n --------------------------- \n"
                        f"{new_item_quantity} of {item_to_read_1} have been sold, total items sold is {new_sold}"
                        f"\n --------------------------- \n")

    elif executable_to_read == "ORDER":

        with open("pop_type.txt", "r") as item_10:
            item_read_10 = item_10.readlines()
            item_string_10 = int(item_number)
            item_to_read_10 = item_read_10[item_string_10]

        with open("pop_type_sold.txt", "r") as item_11:
            item_read_11 = item_11.readlines()
            item_string_11 = int(item_number)
            item_to_read_11 = item_read_11[item_string_11]

        print("Item:")
        print(item_to_read_10)
        print("Orders placed:")
        print(item_to_read_11)

        print("Please list the description and abbreviations for what the customer is ordering.")
        item_description = input("for example, [ MM ] Please only do one item at a time: \n \n $")

        print("Please list the price for what the customer is ordering.")
        item_prices = input("do not put the dollar sign in this number: \n \n $")

        with open("pop_type_sold.txt", "r") as item_12:
            item_read_12 = item_12.readlines()
            item_string_12 = int(item_number)
            item_to_read_12 = item_read_12[item_string_12]

        int_item_quantity = 1
        int_item_sold = int(item_to_read_12)
        new_item_total_sold = int_item_sold + int_item_quantity

        with open("pop_type_sold.txt", 'r') as f:
            get_all = f.readlines()

        with open("pop_type_sold.txt", 'w') as f:
            for i, line in enumerate(get_all):
                if i == int(item_number):
                    f.writelines(str(new_item_total_sold) + "\n")
                else:
                    f.writelines(line)

        path = os.getcwd()
        name = "totals.txt"
        total_dollars_sold = 1
        total_products_sold = 2

        for root, dirs, files in os.walk(path):
            if name in files:
                with open(name, "r") as item_7:
                    item_read_7 = item_7.readlines()
                    item_string_7 = total_dollars_sold
                    item_to_read_7 = item_read_7[item_string_7]

                with open(name, "r") as item_8:
                    item_read_8 = item_8.readlines()
                    item_string_8 = total_products_sold
                    item_to_read_8 = item_read_8[item_string_8]

                    new_total = int(item_to_read_7) + int(item_prices)
                    new_sold = int(item_to_read_8) + 1

                with open(name, 'r') as f:
                    get_all = f.readlines()

                with open(name, 'w') as f:
                    for i, line in enumerate(get_all):
                        if i == int(total_dollars_sold):
                            f.writelines(str(new_total) + "\n")
                        else:
                            f.writelines(line)

                with open(name, 'r') as f:
                    get_all = f.readlines()

                with open(name, 'w') as f:
                    for i, line in enumerate(get_all):
                        if i == int(total_products_sold):
                            f.writelines(str(new_sold))
                        else:
                            f.writelines(line)
                break
            else:
                with open(name, "w") as item_9:
                    item_9.write("Totals: \n")
                    item_9.write("0\n")
                    item_9.write("0")

                new_total = int(item_prices)
                new_sold = 1

                with open(name, 'r') as f:
                    get_all = f.readlines()

                with open(name, 'w') as f:
                    for i, line in enumerate(get_all):
                        if i == int(total_dollars_sold):
                            f.writelines(str(new_total) + "\n")
                        else:
                            f.writelines(line)

                with open(name, 'r') as f:
                    get_all = f.readlines()

                with open(name, 'w') as f:
                    for i, line in enumerate(get_all):
                        if i == int(total_products_sold):
                            f.writelines(str(new_sold))
                        else:
                            f.writelines(line)
                break

        with open("sales.txt", "a") as sales:
            sales.write(f"\n ------------------------------------------------------------------ \n"
                        f"At {current_time}, \n '{item_description}' was/were sold. \n "
                        f"Total is ${item_prices}. Total sales is ${new_total}. \n --------------------------- \n"
                        f"Total items sold is {new_sold}"
                        f"\n --------------------------- \n")

    print("What is the customers first name?")
    question_1 = input("Please enter their full name, first and last: \n \n $")

    print("What is the customers adress?")
    question_2 = input("Please enter their full adress: \n \n $")

    print("What is the customers phone number?")
    question_3 = input("Please enter here: \n \n $")

    print("What is the customers email?")
    question_4 = input("Please enter here: \n \n $")

    print("Did the customer allready pay?")
    question_5 = input("Please enter [ yes ] or [ no ]: \n \n $")

    print("How did the customer pay?")
    question_6 = input("Please type the method of payment: \n \n $")

    print("Who entered this customer into the machine?")
    question_7 = input("Please enter your name: \n \n $")

    with open("sales.txt", "a") as sales:
        sales.write(f"Customer Information: \n Name: {question_1} | Adress: {question_2} \n"
                    f"Phone: {question_3} | Email: {question_4} \n Customer Paid: {question_5} | "
                    f"Payment Method: {question_6} \n --------------------------- \n Order completed by: {question_7}"
                    f"\n ------------------------------------------------------------------ \n \n")

    print("Purchase completed successfully.")
    buffering()
