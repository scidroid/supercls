def cls():
    print("\033[%d;%dH\033[2J" % (0, 0), end="")
