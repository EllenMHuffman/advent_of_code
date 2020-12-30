from string import hexdigits

def validate_number(value, min_num, max_num):
    return value.isnumeric() and int(value) >= min_num and int(value) <= max_num


def validate_birth_year(value):
    return validate_number(value, 1920, 2002)


def validate_issue_year(value):
    return validate_number(value, 2010, 2020)


def validate_expiration_year(value):
    return validate_number(value, 2020, 2030)


def validate_height(value):
    if value.endswith("cm"):
        return validate_number(value[:-2], 150, 193)
    elif value.endswith("in"):
        return validate_number(value[:-2], 59, 76)
    return False


def validate_hair_color(value):
    if not value.startswith("#") or len(value) != 7:
        return False
    for char in value[1:]:
        if char not in hexdigits:
            return False
    return True


def validate_eye_color(value):
    valid_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    if value not in valid_colors:
        return False
    return True


def validate_passport_id(value):
    return len(value) == 9 and value.isnumeric()


required_fields = {
    "byr": validate_birth_year,
    "iyr": validate_issue_year,
    "eyr": validate_expiration_year,
    "hgt": validate_height,
    "hcl": validate_hair_color,
    "ecl": validate_eye_color,
    "pid": validate_passport_id,
}

def read_passports():
    file = open("04_passports.txt")
    lines = file.read().split("\n")
    return lines


def validate_passport(passport):
    for field, validator in required_fields.items():
        if field not in passport.keys():
            return 0
        if not validator(passport[field]):
            return 0
    return 1


def count_valid_passports(lines):
    valid_passport_ct = 0

    passport = {}
    for line in lines:
        if not line:
            valid_passport_ct += validate_passport(passport)
            print(passport)
            passport = {}
        else:
            fields = line.split(" ")
            for field in fields:
                k, v = field.split(":")
                passport[k] = v

    return valid_passport_ct


def main():
    lines = read_passports()

    valid_passport_ct = count_valid_passports(lines)

    print(valid_passport_ct)

if __name__ == "__main__":
    main()
