import re
text = "apple pie, Apple juice, pine apple, an apple."
count = len(re.findall(r"\bapple\b", text, re.IGNORECASE))
print(f"'apple' appears {count} times.")
text = "I like apple pie. Apple juice is tasty.pineapple I ate an apple."
count = text.lower().count("apple")  # Convert to lowercase to count all cases
print(f"'apple' appears {count} times.")



text = "Apple pie is tasty. I love 66 apple juice and an 66 apple a day."
while True:
 word = input("Enter a word to search: or quit 'q' ").lower()
 if word == "q":
     print("Got it End !")
     break# Convert to lowercase
 else:
  count = len(re.findall(rf"\b{word}\b", text, re.IGNORECASE))  # Whole word match
  print(f"'{word}' appears {count} times in the text.")
  print("\n....................")
  print("\n")

