# problem defined here:
# https://www.hackerrank.com/challenges/mandragora

def max_exp(hp, size):
    if size == 0:
        return 0
    if size == 1:
        return hp[0]

    hp = sorted(hp)[::-1]
    #print(hp)
    hpsum = hp[0]
    pmax = size * hp[0]
    for battles in range(0, size):
        s = size - battles
        p = (hpsum + hp[battles+1]) * (s-1)
        #print(p)

        if p < pmax:
            break
        else:
            pmax = p
            hpsum = hpsum + hp[battles+1]

    return int(pmax)


def main():
    cases = int(input())
    for i in range(cases):
        man_num = int(input())
        print(max_exp( [int(hp) for hp in (input()).split()], man_num))

main()
#print(max_exp([3, 2, 2], 3))
