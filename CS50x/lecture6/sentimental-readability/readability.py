text = input("Text: ").upper()
letter = 0
space = 1
sentences = 0
for i in range(len(text)):
    if text[i] >= "A" and text[i] <= "Z":
        letter = letter + 1
    if text[i] == " ":
        space = space + 1
    if text[i] == "!" or text[i] == "." or text[i] == "?":
        sentences = sentences + 1
L = letter / space * 100
S = sentences / space * 100
index = 0.0588 * L - 0.296 * S - 15.8
if index >= 1 and index <= 16:
    print(f"Grade {index:.0f}")
elif index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
