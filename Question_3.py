pet_type = input("Enter pet type (dog/cat/bird/hamster): ").lower()
human_age = int(input("Enter your pet's age in human years: "))

pet_years = 0

if pet_type in ["dog", "cat"]:
    if human_years <= 2:
        pet_years = human_years * 12
    else:
        pet_years = 24 + (human_years - 2) * 4
elif pet_type == "bird":
    pet_years = human_years * 9
elif pet_type == "hamster":
    pet_years = human_years * 25
else:
    print("Sorry, that pet type is not supported.")
    exit()

print(f"\n🐾 Your {pet_type} is {pet_years} years old in {pet_type} years!")