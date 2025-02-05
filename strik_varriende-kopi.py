

def generate_pattern(width, height, symbols):
    """
    Generates a simple crochet or knitting pattern based on selected symbols.
    """
    pattern = []
    for _ in range(height):
        row = " ".join(random.choices(symbols, k=width))
        pattern.append(row)
    return "\n".join(pattern)


def generate_knitting_pattern(size, needle_size):
    """
    Generates a simple pattern based on size and needle size.
    """
    base_stitches = 20  # Base stitch count for a small size
    rows = 30  # Base row count

    stitch_multiplier = size / 10  # Adjusts pattern for larger sizes
    needle_adjustment = max(0.5, 1.5 - (needle_size / 10))  # Adjustment based on needle size

    total_stitches = int(base_stitches * stitch_multiplier * needle_adjustment)
    total_rows = int(rows * stitch_multiplier * needle_adjustment)

    return f"Start by casting on {total_stitches} stitches with needle size {needle_size}. Knit {total_rows} rows in any chosen pattern."


def main():
    print("Welcome to the knitting/crochet pattern generator!")
    choice = input("Would you like to generate (1) a pattern or (2) a knitting recipe? ")

    if choice == "1":
        width = int(input("Enter pattern width (e.g., 10): "))
        height = int(input("Enter pattern height (e.g., 5): "))
        symbols = input("Enter symbols separated by spaces (e.g., X O -): ").split()

        pattern = generate_pattern(width, height, symbols)
        print("\nYour generated pattern:")
        print(pattern)
    elif choice == "2":
        size = int(input("Enter desired size (1-100): "))
        needle_size = float(input("Enter needle size (e.g., 4.5): "))
        recipe = generate_knitting_pattern(size, needle_size)
        print("\nYour generated knitting recipe:")
        print(recipe)
    else:
        print("Invalid choice. Please try again.")

patterns = {
    "duck 10x10": [
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
    "crap 20x20": [
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
    "heart 15x15": [
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
        "000000000000000",

    ],
    "penguin 18x22": [
        "000000000000000000",
        "0000000000xxxx0000",
        "000000000xxxxxx000",
        "00000000xxx00xx000"
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
        "000000000000000000",
    ]
}

def get_predefined_pattern(name):
    return "\n".join(patterns.get(name, ["Pattern not found"]))

print(get_predefined_pattern("duck"))


if __name__ == "__main__":
    main()

