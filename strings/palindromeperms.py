# problem 1.4

testFilename = "palindromecheck.txt"

def run(intext):
    print(permpal(intext))

def permpal(word):
    word = word.lower()
    print("evaluating [" + word + "]")
    counter = {}
    for c in word:
        if c == " ":
            continue
        if c not in counter:
            counter[c] = 0
        counter[c] += 1
    odds = 0
    for c in counter.keys():
        odds += counter[c] % 2
        if odds > 1:
            return False
    return True

def trial():
    trialword = "tactcoapapa"
    print(permpal(trialword))
    run("trytrywallw")
    run("failfailzkzkwi")

if __name__ == "__main__":
    trial()

