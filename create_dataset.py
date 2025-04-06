# create_dataset.py

import csv

data = [
    ["This phone is super fast and cool!", "Teen"],
    ["Love how light this laptop is. Great for college.", "Young Adult"],
    ["I bought this as a gift for my granddaughter. She loved it!", "Senior"],
    ["Very durable shoes, great for long walks.", "Middle-aged"],
    ["This tablet helps me with my online classes.", "Teen"],
    ["Stylish headphones, perfect for commuting.", "Young Adult"],
    ["I use this massager every evening for my back pain.", "Senior"],
    ["This washing machine makes laundry so much easier.", "Middle-aged"],
    ["Perfect for gaming!", "Teen"],
    ["Great addition to my kitchen appliances.", "Middle-aged"]
]

with open("age_group_dataset.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["review", "age_group"])
    writer.writerows(data)

print("Dataset created successfully.")
