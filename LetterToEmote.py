"""This "Letter To Emote" file change every single character in your sentence to emote
-------- This will help you understand each character and emote meaning
    "a" = "😀"|| "b" = "😃"|| "c" = "😁"|| "d" = "😅"|| "e" = "🥰"|| "f" = "🤣"||
    "g" = "😥"|| "h" = "😬"|| "i" = "😊"|| "j" = "😛"|| "k" = "😇"|| "l" = "😉"||
    "m" = "😒"|| "n" = "😔"|| "o" = "😙"|| "p" = "🙁"|| "q" = "😕"|| "r" = "🙂"||
    "s" = "🙃"|| "t" = "🤮"|| "u" = "😡"|| "v" = "😍"|| "w" = "😳"|| "x" = "😩"||
    "y" = "😭"|| "z" = "😠"|| "A" = "😀"|| "B" = "😃"|| "C" = "😁"|| "D" = "😅"||
    "E" = "🥰"|| "F" = "🤣"|| "G" = "😥"|| "H" = "😬"|| "I" = "😊"|| "J" = "😛"||
    "K" = "😇"|| "L" = "😉"|| "M" = "😒"|| "N" = "😔"|| "O" = "😙"|| "P" = "🙁"||
    "Q" = "😕"|| "R" = "🙂"|| "S" = "🙃"|| "T" = "🤮"|| "U" = "😡"|| "V" = "😍"||
    "W" = "😳"|| "X" = "😩"|| "Y" = "😭"|| "Z" = "😠"|| "," = ",",
    "." = "."  ||
    "[" = "["  ||
    "]" = "]"  ||
    "<" = "<"  ||
    ">" = ">"  ||
    "?" = "?"  ||
    "/" = "/"
"""
lte = {
    "a" : "😀",
    "b" : "😃",
    "c" : "😁",
    "d" : "😅",
    "e" : "🥰",
    "f" : "🤣",
    "g" : "😥",
    "h" : "😬",
    "i" : "😊",
    "j" : "😛",
    "k" : "😇",
    "l" : "😉",
    "m" : "😒",
    "n" : "😔",
    "o" : "😙",
    "p" : "🙁",
    "q" : "😕",
    "r" : "🙂",
    "s" : "🙃",
    "t" : "🤮",
    "u" : "😡",
    "v" : "😍",
    "w" : "😳",
    "x" : "😩",
    "y" : "😭",
    "z" : "😠",
    "A" : "😀",
    "B" : "😃",
    "C" : "😁",
    "D" : "😅",
    "E" : "🥰",
    "F" : "🤣",
    "G" : "😥",
    "H" : "😬",
    "I" : "😊",
    "J" : "😛",
    "K" : "😇",
    "L" : "😉",
    "M" : "😒",
    "N" : "😔",
    "O" : "😙",
    "P" : "🙁",
    "Q" : "😕",
    "R" : "🙂",
    "S" : "🙃",
    "T" : "🤮",
    "U" : "😡",
    "V" : "😍",
    "W" : "😳",
    "X" : "😩",
    "Y" : "😭",
    "Z" : "😠",
    "," : ",",
    "." : ".",
    "[" : "[",
    "]" : "]",
    "<" : "<",
    ">" : ">",
    "?" : "?",
    "/" : "/"
}
print("This will translate Letter to Emote")

def translate():
  word = input("Type the sentence you wanted to translate to emote: ")
  wordStored = []
  new_list = word.split(" ")
  if word != "exit":
    while len(new_list) > 0:
      pp = new_list.pop()
      tl = ''.join(lte[ele] for ele in pp.strip())
      wordStored.append(tl)
    else:
      wordStored.reverse()
      print("Your translate is:"," ".join(wordStored))
      translate()
  else:
    print("Thank you for using this program")
    input("Press anything to close the program")
translate()
