# Prompt the user for input
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
clothing_item = input("Enter a clothing item: ")
silly_object = input("Enter a silly object: ")
exclamation = input("Enter an exclamation: ")
verb1 = input("Enter a verb: ")
silly_noise = input("Enter a silly noise: ")
verb2 = input("Enter another verb: ")
verb3 = input("Enter one more verb: ")
verb4 = input("Enter the FINAL verb")

# Capitalize the exclamation to start the sentence
exclamation = exclamation.capitalize()

# Fill the story with the user's input
story = f"One day, I was walking down the street when I stumbled upon a very {adjective} {animal}. It was wearing a {clothing_item} and carrying a {silly_object}. I couldn’t believe my eyes! The {animal} looked at me and said, \"{exclamation}!\" It then started to {verb1} in circles while making {silly_noise} sounds. I was so confused, I had to IMMMEDIETLY {verb2} to escape obviously. But just then, the {animal} began to {verb3}. Thankfully, I finally {verb4} just in time to avoid a {silly_object} being thrown at my face. I must go to bed!"

# Display the completed story
print("\nHere is your story:")
print(story)
