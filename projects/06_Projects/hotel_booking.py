def main():
    
    menu = {
    1: {"item": "Burger", "price": 8.99},
    2: {"item": "Fries", "price": 3.49},
    3: {"item": "Salad", "price": 5.99},
    4: {"item": "Pizza", "price": 10.99},
    5: {"item": "Pasta", "price": 12.49},
    6: {"item": "Soda", "price": 1.99},
    7: {"item": "Ice Cream", "price": 4.49}
}



    hotel = {1: {1: (False), 2: (False), 3: (False)}, 2: {1: (False), 2: (False), 3: (False)}, 3: {1: (False), 2: (False), 3: (False)}}
    print(hotel)
    def CI(name, CIT, floor, RN, card):
        
        
        
            
        if hotel[floor][RN] == (False):
            hotel[floor][RN] = (True, name, CIT, card)
            
            print(hotel)
            
        else:
            print(f"Occupied by {hotel[floor][RN][1]}")

    def room_service(floor, RN, order):
        if hotel[floor][RN][4] == True:

            item = menu[order]["item"]
            price = menu[order]["price"]
            print(f"{item} bought for {price}")
        

    def CO(floor, RN):
        if hotel[floor][RN][0] == True:
            hotel[floor][RN] = (False)

    while True:
        cmd = input()
        cmd = cmd.split()
        if cmd[0] == "CI":
            try:
                CI(cmd[1], int(cmd[2]), int(cmd[3]), int(cmd[4]), bool(cmd[5]))
            except:
                print("To check in input the name, check in time, floor number, room number, and if you have a credit card or not (True/False). Ex. (CI Bob 10/20/24 2 2 True)")
        elif cmd[0] == "CO":
            try:
                CO(int(cmd[1]), int(cmd[2]))
            except:
                print("To check out input the floor number and room number only. Ex. (CO 2 2)")
        elif cmd[0] == "Exit":

            break

        elif cmd[0] == "Menu":
            print(menu)
        elif cmd[0] == "RS":
            room_service(int(cmd[1]), int(cmd[2]), cmd[3])


        else:
            print("Use CI to check in, CO to check out, or exit to leave")
            
main()

