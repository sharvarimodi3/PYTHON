# 1. Count vowels in a file
with open("sample.txt", "r") as f:
    content = f.read()

count = 0
for ch in content:
    if ch.lower() in "aeiou":
        count += 1

print("Total number of vowels:", count)


# 2. Count lines and display 2nd and 4th lines
with open("sample.txt", "r") as f:
    lines = f.readlines()

print("Total number of lines:", len(lines))

if len(lines) >= 2:
    print("Second line:", lines[1])

if len(lines) >= 4:
    print("Fourth line:", lines[3])


# 3. Find the longest word in a user-entered sentence
sentence = input("Enter a sentence: ")
words = sentence.split()

if words:
    longest = max(words, key=len)
    print("Longest word:", longest)
else:
    print("No words entered.")


# 4. Count total words and print unique words from a file
with open("sample.txt", "r") as f:
    content = f.read()

words = content.split()

print("Total number of words:", len(words))
print("Unique words:")

for word in sorted(set(words)):
    print(word)


# 5. Write data to a file
with open("sample.txt", "w") as f:
    f.write("Hello Python\n")
    f.write("File handling is easy\n")
    f.write("Python programming\n")
    f.write("Learn file operations")

print("Data written successfully.")


# 6. Append data to a file
with open("sample.txt", "a") as f:
    f.write("\nWelcome to Python")

print("Data appended successfully.")


# 7. Read and display the file
with open("sample.txt", "r") as f:
    print(f.read())