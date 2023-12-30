import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "abcdefghijklmnopqrstuvwxyz".upper()
numbers = "1234567890"
symbols = "!@#$%^&*(_=-+)"


combined_characters = list(lower_case + upper_case + numbers + symbols)

while True:
    try:
        num_of_passwords = int(input("How many passwords do you want? "))
        len_of_password = int(input("How long do you want you password? "))
        if num_of_passwords <= 0 or len_of_password <= 0:
            print("Enter a number higher than zero!")
            continue 


        for _ in range(num_of_passwords):
            random_password = ""
            for i in range(len_of_password):
                generated_password = random.choice(combined_characters)
                random_password += generated_password

            print(random_password)
            print(f"Length: {len(random_password)}")
        break
    except (NameError, ValueError) as e:
        print(f"An error occured {e}")
        print("Please enter a postive number!")
