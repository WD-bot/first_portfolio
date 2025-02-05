import random


def generate_pattern(width, height, symbols):
    """
    Generates a simple crochet or knitting pattern based on selected symbols.
    """
    pattern = []
    for _ in range(height):
        row = " ".join(random.choices(symbols, k=width))
        pattern.append(row)
    return "\n".join(pattern)


def make_bucket_hat_pattern(size):
    """
    Generates a crochet pattern for a bucket hat based on size.
    """
    sizes = {
        "0-1 years": (50, 10),
        "1-3 years": (52, 11),
        "3-7 years": (54, 12),
        "7-14 years": (56, 13),
        "Small": (58, 14),
        "Medium": (60, 15),
        "Large": (62, 16)
    }

    if size not in sizes:
        return "Invalid size. Choose from: " + ", ".join(sizes.keys())

    circumference, height = sizes[size]

    return (f"For a {size} bucket hat:\n- Start with a magic ring and increase until reaching {circumference} stitches."
            f"\n- Crochet in rounds until {height} cm high.\n- Add a brim/shade as desired.")


def colorize_pattern(pattern):
    """
    Colorizes the pattern by replacing 'x' with a red color and '0' with blue.
    """
    colored_pattern = []
    for row in pattern:
        colored_row = row.replace('x', '\033[94m0\033[0m')
        colored_pattern.append(colored_row)
    return "\n".join(colored_pattern)


def main():
    print("Welcome to the bucket hat crochet pattern maker!")
    size = input("Enter the size 0-1 years, 1-3 years, 3-7 years, 7-14 years, Small, Medium, Large: ")
    recipe = make_bucket_hat_pattern(size)
    print("\nYour bucket hat pattern:")
    print(recipe)

    pattern_choice = input("Would you like to select a pre-made pattern? (yes/no): ").strip().lower()
    if pattern_choice == "yes":
        print("Available patterns:")
        for key in patterns.keys():
            print(f"- {key}")
        selected_pattern = input("Enter the pattern name: ").strip()
        if selected_pattern in patterns:
            print("\nYour selected pattern:")
            pattern = patterns[selected_pattern]
            pattern_width = pattern[0]
            colored_pattern = colorize_pattern(pattern[1:])
            print(colored_pattern)

            sizes = {
                "0-1 years": 50,
                "1-3 years": 52,
                "3-7 years": 54,
                "7-14 years": 56,
                "Small": 58,
                "Medium": 60,
                "Large": 62
            }
            if size in sizes:
                circumference = sizes[size]
                repeats = circumference // pattern_width
                remainder = circumference % pattern_width
                print(f"\nPattern repeats {repeats} times with {remainder} stitches left over.")
                print("")
        else:
            print("Invalid pattern name.")
    else:
        print("Thank you for using the generator!")


patterns = {
    "duck": [10,
             "OOOOOOOOOO",
             "OOXXXOOOOO",
             "OXXXXXOOOO",
             "000XXX0000",
             "0000X00000",
             "000XXX00X0",
             "OOXXXXXXXO",
             "OOXXXXXXXO",
             "OOOXXXXXOO",
             "OOOOOOOOOO"
             ],
    "crab": [20,
             "00000000000000000000",
             "000000xx0000xx000000",
             "00000xx000000xx00000",
             "0000xx00x00x00xx0000",
             "000xxxxxx00xxxxxx000",
             "000xxxx000000xxxx000",
             "000xx0000000000xx000",
             "000x0000x00x0000x000",
             "000xxx0xxxxxx0xxx000",
             "0000xxxxxxxxxxxx0000",
             "000xxxxxxxxxxxxxx000",
             "00xxxxxxxxxxxxxxxx00",
             "00x0xxxxxxxxxxxx0x00",
             "0000xxxxxxxxxxxx0000",
             "000xxxxxxxxxxxxxx000",
             "000x00xxxxxxxx00x000",
             "00000xx0x00x0xx00000",
             "00000x00000000x00000",
             "00000000000000000000",
             "00000000000000000000"
             ],
    "heart": [15,
              "000000000000000",
              "000000000000000",
              "000000000000000",
              "0000xx000xx0000",
              "000xxxx0xxxx000",
              "000xxxxxxxxx000",
              "000xxxxxxxxx000",
              "000xxxxxxxxx000",
              "0000xxxxxxx0000",
              "00000xxxxx00000",
              "000000xxx000000",
              "0000000x0000000",
              "000000000000000",
              "000000000000000",
              "000000000000000"
              ],
    "penguin": [18,
                "000000000000000000",
                "0000000000xxxx0000",
                "000000000xxxxxx000",
                "00000000xxx00xx000",
                "0000000xxx00x0x000",
                "000000xxx000xxxx00",
                "00000xxxxx00xx0000",
                "0000xxxxxxxxx00000",
                "000xxxxxxxxxxx0000",
                "00xxxxxxxx00xxx000",
                "00xxxxxx00000xxx00",
                "00xxxxx0000000xxx0",
                "0xx0xx00000000xxx0",
                "xxx0x000000000xxxx",
                "xx0xx000000000x0xx",
                "x00xx000000000x00x",
                "000xx000000000x000",
                "000xx00000000xx000",
                "0000xxx00000xx0000",
                "0000xxxxxxxxxx0000",
                "000xxxxxx0xxxxx000",
                "000000000000000000"
                ],
    "elephants":[
                33,
                "000000000000000000000000000000000",
                "000000000000000xxxx00000000000000",
                "00000000000000xxxxxxxxxxxx0000000",
                "00000000000000xxxxxxxxxxxxx000000",
                "0000000000000xxx0xxxxxxxxxxx00000",
                "0000000000000x0x0xxxxxxxxxxxx0000",
                "0000000000000xxxx0x0xxxxxxxxx0000",
                "0000000000000xxxxx0xxxxxxxxxx0000",
                "0000000000000xxxxxxxxxxxxxxxxx000",
                "000xx00000000xxxxxxxxxxxxxxxxx000",
                "00xxxx0000000xxx0xxxxxxxxxxxxx000",
                "0xxxxxxx00000xx00xxxxxxxxxxx00x00",
                "0x0xxxxxx0000xx00xxxxxxxxxxx00x00",
                "0xxxxxxxx0000x00xxxxxxxxxxxx00x00",
                "0xxxxxxx0x00xx00xxx0xx000xxxxx00x",
                "xx0xxxxx00xxx00xxx00xxx00xx0xxx00",
                "000xx0xx0000000xx0000xx00xx00xxx0",
                "000xx0xx000000xxx000xxx0xxx000xx0",
                "000000000000000000000000000000000",
                ]

}

if __name__ == "__main__":
    main()
