import time

def main():
    seconds = time.time()
    
    hotel = {1: {1: (False), 2: (False), 3: (False)}, 2: {1: (False), 2: (False), 3: (False)}, 3: {1: (False), 2: (False), 3: (False)}}
    print(hotel)
    def CI(name, CIT, floor, RN):
        if hotel[floor][RN] == (False):
            hotel[floor][RN] = (True, name, CIT)
            print(hotel)
            
        else:
            print(f"Occupied by {hotel[floor][RN][1]}")

    def CO(floor, RN):
        if hotel[floor][RN][0] == True:
            hotel[floor][RN] = (False)
            print(0.1 * (time.time() - hotel[floor][RN][2]))

    while True:
        cmd = input()
        cmd = cmd.split()
        if cmd[0] == "CI":
            CI(cmd[1], time.time(), int(cmd[2]), int(cmd[3]))
        elif cmd[0] == "CO":
            CO(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "exit":
            break
            

    

main()

