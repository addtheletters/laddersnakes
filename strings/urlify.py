# Cracking the Coding Interview 6th ed problem 1.3

testFilename = "strings/urlifytest.txt"

def run(intext):
    splitin = intext.split(",")
    print( urlify( splitin[0], int(splitin[1]) ) )

def urlify(url, truelen):
    url = list(url)
    #print(url)
    spaces = []
    for i in range(truelen):
        if url[i] == ' ':
            spaces.append(i)

    #print(spaces)

    prev = truelen
    for j in range(len(spaces))[::-1]:
        #print("evaluating space at " + str(spaces[j]) + " [" + url[spaces[j] - 1] + url[spaces[j]] + url[spaces[j] + 1] + "]")
        for sind in range(spaces[j]+1, prev):
            #print("shifting index " + str(sind) + "[" + url[sind] + "]")
            url[sind + 2*(j+1)] = url[sind]
        url[spaces[j] + 2*j] = '%'
        url[spaces[j] + 2*j + 1] = '2'
        url[spaces[j] + 2*j + 2] = '0'
        prev = spaces[j]
        #print(url)
        #print("marker moved to " + str(prev))
    
    return ''.join(url)

def trial():
    urlin = "HELLO MY NAME IS SALLY AND I HAVE A CAR                  "
    urld = urlify(urlin, 39)
    print("result is [" + urld + "]")

    infull = "HELLO MY NAME IS SALLY AND I HAVE A CAR                  ,39"
    run(infull)


if __name__ == "__main__":
    trial()
