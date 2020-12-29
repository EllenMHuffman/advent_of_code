def read_passwords():
    file = open("02_passwords.txt")
    lines = file.read().split("\n")
    return lines


def count_letters(req, word):
    qty = 0
    for letter in word:
        if req == letter:
            qty += 1

    return qty

def is_password_valid_sled(requirement, password):
    digits, letter = requirement.split(" ")
    min_num, max_num = digits.split("-")

    letter_qty = count_letters(letter, password)
    if letter_qty >= int(min_num) and letter_qty <= int(max_num):
        return True
    return False

def is_password_valid_toboggan(requirement, password):
    digits, letter = requirement.split(" ")
    first_pos, second_pos = digits.split("-")

    has_first_pos = password[int(first_pos) - 1] == letter
    has_second_pos = password[int(second_pos) - 1] == letter

    if has_first_pos and has_second_pos:
        return False
    elif has_first_pos or has_second_pos:
        return True
    return False


def main():
    lines = read_passwords()

    valid_password_qty = 0
    for line in lines:
        if line:
            requirement, password = line.split(": ")
            if is_password_valid_toboggan(requirement, password):
                valid_password_qty += 1

    print(valid_password_qty)


if __name__ == "__main__":
    main()
