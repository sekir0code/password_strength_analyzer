print("🔐 PASSWORD STRENGTH ANALYZER")
print("-----------------------------")

password = input("Enter a password: ")

has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
has_number = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)
has_good_length = len(password) >= 8

score = 0

if has_good_length:
    score += 1

if has_uppercase:
    score += 1

if has_lowercase:
    score += 1

if has_number:
    score += 1

if has_special:
    score += 1

print()
print("Password Analysis")
print("-----------------")

print("Length:", len(password))

if has_good_length:
    print("8+ characters: ✓")
else:
    print("8+ characters: ✗")

if has_uppercase:
    print("Uppercase: ✓")
else:
    print("Uppercase: ✗")

if has_lowercase:
    print("Lowercase: ✓")
else:
    print("Lowercase: ✗")

if has_number:
    print("Number: ✓")
else:
    print("Number: ✗")

if has_special:
    print("Special character: ✓")
else:
    print("Special character: ✗")

print()
print("Score:", str(score) + "/5")

if score == 5:
    print("Strength: VERY STRONG 🟢")

elif score == 4:
    print("Strength: STRONG 🟢")

elif score == 3:
    print("Strength: MEDIUM 🟡")

elif score == 2:
    print("Strength: WEAK 🟠")

else:
    print("Strength: VERY WEAK 🔴")

print()

if score < 5:
    print("Suggestions:")

    if not has_good_length:
        print("- Make your password at least 8 characters long.")

    if not has_uppercase:
        print("- Add an uppercase letter.")

    if not has_lowercase:
        print("- Add a lowercase letter.")

    if not has_number:
        print("- Add a number.")

    if not has_special:
        print("- Add a special character like ! @ # $ %")
