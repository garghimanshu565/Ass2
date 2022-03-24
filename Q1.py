from collections import defaultdict
mwjug1, mwjug2, target = 4, 3, 2

final = defaultdict(lambda: False)

def water_jug(wjug1, wjug2):
    if (wjug1 == target and wjug2 == 0) or (wjug2 == target and wjug1 == 0):
        if (wjug1 == target and wjug2==0):
            print(wjug1, wjug2)
        elif (wjug2 == target and wjug1==0):
            print(wjug2,wjug1)
        return True

    if final[(wjug1, wjug2)] == False:
        print(wjug1, wjug2)

        final[(wjug1, wjug2)] = True

        return (water_jug(0, wjug2) or
                water_jug(wjug1, 0) or
                water_jug(mwjug1, wjug2) or
                water_jug(wjug1, mwjug2) or
                water_jug(wjug1 + min(wjug2, (mwjug1 - wjug1)),
                               wjug2 - min(wjug2, (mwjug1 - wjug1))) or
                water_jug(wjug1 - min(wjug1, (mwjug2 - wjug2)),
                               wjug2 + min(wjug1, (mwjug2 - wjug2))))

    else:
        return False


print("Path from initial state to final state")

water_jug(0, 0)
