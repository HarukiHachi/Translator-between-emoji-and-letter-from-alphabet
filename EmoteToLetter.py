"""Project: this "Emote to Letter" file change every single emote in your sentence to character
-------- This will help you understand each character and emote meaning
    "😀" : "a",
    "😃" = "b"|| "😁" = "c"|| "😅" = "d"|| "🥰" = "e"|| "🤣" = "f"|| "😥" = "g"||
    "😬" = "h"|| "😊" = "i"|| "😛" = "j"|| "😇" = "k"|| "😉" = "l"|| "😒" = "m"||
    "😔" = "n"|| "😙" = "o"|| "🙁" = "p"|| "😕" = "q"|| "🙂" = "r"|| "🙃" = "s"||
    "🤮" = "t"|| "😡" = "u"|| "😍" = "v"|| "😳" = "w"|| "😩" = "x"|| "😭"= "y"||
    "😠"="z"||   "😀" = "A"|| "😃" = "B"|| "😁" = "C"|| "😅" = "D"|| "🥰" = "E"||
    "🤣" = "F"|| "😥" = "G"|| "😬" = "H"|| "😊" = "I"|| "😛" = "J"|| "😇" = "K"||
    "😉" = "L"|| "😒" = "M"|| "😔" = "N"|| "😙" = "O"|| "🙁" = "P"||
    "😕" = "Q"|| "🙂" = "R"|| "🙃" = "S"||"🤮" = "T"|| "😡" = "U"||
    "😍" = "V"|| "😳" = "W"||
    "😩" = "X"|| "😭"= "Y"||
    "😠"="Z"  ||
    "," : ","  ||
    "." : "."  ||
    "[" : "["  ||
    "]" : "]"  ||
    "<" : "<"  ||
    ">" : ">"  ||
    "?" : "?"  ||
    "/" : "/"
"""
etl = {
    "😀" : "a",
    "😃" : "b",
    "😁" : "c",
    "😅" : "d",
    "🥰" : "e",
    "🤣" : "f",
    "😥" : "g",
    "😬" : "h",
    "😊" : "i",
    "😛" : "j",
    "😇" : "k",
    "😉" : "l",
    "😒" : "m",
    "😔" : "n",
    "😙" : "o",
    "🙁" : "p",
    "😕" : "q",
    "🙂" : "r",
    "🙃" : "s",
    "🤮" : "t",
    "😡" : "u",
    "😍" : "v",
    "😳" : "w",
    "😩" : "x",
    "😭": "y",
    "😠":"z",
    "😀" : "A",
    "😃" : "B",
    "😁" : "C",
    "😅" : "D",
    "🥰" : "E",
    "🤣" : "F",
    "😥" : "G",
    "😬" : "H",
    "😊" : "I",
    "😛" : "J",
    "😇" : "K",
    "😉" : "L",
    "😒" : "M",
    "😔" : "N",
    "😙" : "O",
    "🙁" : "P",
    "😕" : "Q",
    "🙂" : "R",
    "🙃" : "S",
    "🤮" : "T",
    "😡" : "U",
    "😍" : "V",
    "😳" : "W",
    "😩" : "X",
    "😭": "Y",
    "😠":"Z",
    "," : ",",
    "." : ".",
    "[" : "[",
    "]" : "]",
    "<" : "<",
    ">" : ">",
    "?" : "?",
    "/" : "/"
}
print("This is Emote translate to Letter")
def ETLL():
  
  word = input("Type or copy sentence of emote you wanted to translate to word: ")
  wordStored = []
  new_list = word.split(" ")
  if word != "exit":
    while len(new_list) > 0:
      pp = new_list.pop()
      tl = ''.join(etl[ele] for ele in pp.strip())
      wordStored.append(tl)
    else:
      wordStored.reverse()
      print("Your translate is:"," ".join(wordStored).lower())
      ETLL()
  else:
    print("Thank you for using this program")
    input("Press anything to close the program")
ETLL()