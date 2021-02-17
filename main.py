from functions import add, listAll

#add("verb", "être", "to be, to exist", "Je suis polonais")


while True:
  mode = input("\nadd / test / list all\n")
  if mode == "add":
    print("1. noun, 2. verb, 3. adj")
    wortart = input("4. adv, 5. prep, 6. conj\n")
    fr = input("french:\n")
    en = input("english:\n")
    bsp = input("example:\n")
    add(wortart, fr, en, bsp)
  elif mode == "test":
    pass
  elif mode == "list all":
    listAll()