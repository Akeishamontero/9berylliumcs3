# a. Ask the user to enter a year of birth and store it in a variable called year_of_birth.
year_of_birth = int(input("Enter your year of birth: "))

# b. Validate user input that it should be not earlier that 1900.
# c. If the user enters an invalid year then display an appropriate message then stop or abort the program.
if year_of_birth < 1900:
    print("Invalid year, it should not be earlier than 1900.")
    exit()

# d. Otherwise determine the chinese zodiac sign based on the following starting from 1900.
else:
    zodiac_signs = [
        "Rat (鼠 / Shǔ)", "Ox (牛 / Niú)",  "Tiger (虎 / Hǔ)",  "Rabbit (兔 / Tù)",  "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)",
        "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"
    ] 
    # e. CONSIDER only the year of birth.
    index = (year_of_birth - 1900) % 12
    zodiac_sign = zodiac_signs[index]
    print(f"Your Chinese zodiac sign is: {zodiac_sign}")
