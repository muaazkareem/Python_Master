# 1. Create the text you want to save
entry = "Today I mastered Python functions and loops!"

# 2. Open the file in WRITE mode ("w") to save the text
with open("diary.txt", "w") as file:
    file.write(entry)
    print("File saved successfully!")

# 3. Open the same file in READ mode ("r") to view the content
with open("diary.txt", "r") as file:
    content = file.read()

# 4. Print the content outside the file block to see it on screen
print(f"Inside diary.txt: {content}")