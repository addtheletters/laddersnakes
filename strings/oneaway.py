# CTCI 6th ed, problem 1.5

def oneAway(stA, stB):
    lendiff = False
    if abs(len(stA) - len(stB)) > 1:
        return False
    else:
        lendiff = len(stA) != len(stB) 
    inconst = 0
    dexA = 0
    dexB = 0
    while dexA < len(stA) and dexB < len(stB):
        if stA[dexA] == stB[dexB]:
            dexA += 1
            dexB += 1
            continue
        else:
            inconst += 1
            if inconst > 1:
                print("Found second inconsistent ")
                return False
            if not lendiff:
                dexA += 1
                dexB += 1
                continue
            if dexA < len(stA) - 1 and stA[dexA+1] == stB[dexB]:
                dexA += 1
                continue
            elif dexB < len(stA) - 1 and stB[dexB+1] == stA[dexA]:
                dexB += 1
                continue
            elif dexA + 1 == len(stA) and dexB + 1 == len(stB): 
                #print("Drat")
                return True
    return True

pairs = {
    ("pale", "ple"):True,
    ("pales", "pale"):True,
    ("pale", "bale"):True,
    ("pale", "bake"):False
}
for pair in pairs.keys():
    print( str(pair) + "\t gives \t" + str(oneAway(pair[0], pair[1])) + "\tvs:\t" + str(pairs[pair]) )

# postmortem
# Foolishly ignored the case where they are the same length, resulting in need for ballooning of conditions and flags.
# Smart thing: Record which of the strings is longer, use that to greatly simplify logic.
