bools = [0, 1]

for a in range(2):
    for b in range(2):
        for c in range(2):
            # (A || B) || ((!A && C) && !(B || C))

            expression = (bool) ( (bools[a] or bools[b]) or ( (not bools[a] and bools[c]) and not (bools[b] or bools[c]) ) )

            print(f"A: {bools[a]}, B: {bools[b]}, C: {bools[c]}, Result: {expression}\n")