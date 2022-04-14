def increment_decrement(operations):
    res = 0
    for i in range(len(operations)):
        if (operations[i] == "++X") | (operations[i] == "X++"):
            res += 1
        elif (operations[i] == "--X") | (operations[i] == "X--"):
            res -= 1
    return res


increment_decrement(["X++", "++X", "--X", "X--"])
