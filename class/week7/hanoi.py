def hanoi(level, A, C, B):
    """
        A is source
        B is destination
        C is helper
    """
    if level == 0:
        return
    hanoi(level - 1, A, B, C)
    print "from %s to %s: %d" % (A, C, level)
    hanoi(level - 1, B, C, A)

hanoi(3, "A", "C", "B")









