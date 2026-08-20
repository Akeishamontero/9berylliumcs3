# Chinese Zodiac

## Requirements
a. Ask the user to enter a year of birth.  The baseline year 1900.
b. Validate user input that it should not be earlier than 1900.
c. If the user enters an invalid year then display an appropriate message then stop or abort the program.

Example:
Enter your birth year: 1800
Invalid Year, it should not be earlier than 1900

d. Otherwise determine the chinese zodiac sign based on the following starting from 1900.  Note: A zodiac sign will recur after each 12 years.

e. CONSIDER only the year of birth.

Example input and output:
Enter your birth year: 2000
Your Chinese Zodiac Sign is: Dragon (龙 / Lóng)

## Code

year_of_birth = int(input("Enter your year of birth: "))


if year_of_birth < 1900:
    print("Invalid year, it should not be earlier than 1900.")
    exit()


else:
    zodiac_signs = [
        "Rat (鼠 / Shǔ)", "Ox (牛 / Niú)",  "Tiger (虎 / Hǔ)",  "Rabbit (兔 / Tù)",  "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)",
        "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"
    ] 
    
    index = (year_of_birth - 1900) % 12
    zodiac_sign = zodiac_signs[index]
    print(f"Your Chinese zodiac sign is: {zodiac_sign}")


## Output

![alt text](image.png)
