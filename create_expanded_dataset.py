import csv

# Expanded dataset with 10 samples per age group
expanded_data = [
    # Teen
    ["This phone has cool games!", "Teen"],
    ["I'm obsessed with these sneakers!", "Teen"],
    ["This app is amazing for social media.", "Teen"],
    ["I love the camera on this phone for selfies.", "Teen"],
    ["These wireless earbuds are great for music.", "Teen"],
    ["Best gadget for gaming on the go!", "Teen"],
    ["This smartwatch helps me stay active.", "Teen"],
    ["The design is super trendy and stylish.", "Teen"],
    ["Helps with my online classes.", "Teen"],
    ["Awesome graphics for mobile games!", "Teen"],

    # Young Adult
    ["Great for my university projects.", "Young Adult"],
    ["This backpack is stylish and holds everything I need.", "Young Adult"],
    ["Perfect for working remotely.", "Young Adult"],
    ["This laptop is lightweight and fast.", "Young Adult"],
    ["I use this tablet for reading and note-taking.", "Young Adult"],
    ["Great for watching lectures and YouTube.", "Young Adult"],
    ["Stylish and efficient kitchen appliance.", "Young Adult"],
    ["Best value for money I've spent recently.", "Young Adult"],
    ["Makes my daily commute more enjoyable.", "Young Adult"],
    ["Love how compact and powerful this gadget is.", "Young Adult"],

    # Middle-aged
    ["Helps me with home office work.", "Middle-aged"],
    ["This dishwasher saved me so much time.", "Middle-aged"],
    ["My kids love this educational toy.", "Middle-aged"],
    ["Great for managing work and family tasks.", "Middle-aged"],
    ["This vacuum cleaner is powerful and quiet.", "Middle-aged"],
    ["Easy to set up and use for the whole family.", "Middle-aged"],
    ["Really helps me organize home chores.", "Middle-aged"],
    ["Perfect for family movie nights.", "Middle-aged"],
    ["Reliable product for everyday use.", "Middle-aged"],
    ["The smart features are very handy.", "Middle-aged"],

    # Senior
    ["Very helpful for my arthritis.", "Senior"],
    ["This device reminds me to take my medicine.", "Senior"],
    ["Easy to read screen for my eyes.", "Senior"],
    ["Comfortable to use and lightweight.", "Senior"],
    ["This heating pad relieves my back pain.", "Senior"],
    ["Perfect for keeping in touch with grandkids.", "Senior"],
    ["Great sound quality for my hearing.", "Senior"],
    ["Love how simple and easy this is.", "Senior"],
    ["This phone has big buttons I can see.", "Senior"],
    ["Helpful for monitoring my blood pressure.", "Senior"],
]

# Write to CSV
with open("age_group_dataset.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["review", "age_group"])
    writer.writerows(expanded_data)

print("Expanded dataset saved to age_group_dataset.csv.")
