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

    hotel = {floor: {room: None for room in range(1, 21)} for floor in range(1, 11)}

    def get_base_price(suite_type):
        if suite_type == "suite":
            return 100
        elif suite_type == "balcony":
            return 150
        elif suite_type == "penthouse":
            return 300

    def display_room_types():
        print("Available Room Types:")
        print("1. Suite: $100 per night")
        print("2. Balcony Suite: $150 per night")
        print("3. Penthouse Suite: $300 per night\n")

    def display_available_rooms(suite_type):
        print("Available Rooms:")
        base_price = get_base_price(suite_type)
        for floor in range(1, 11):
            print(f"Floor {floor}:")
            room_prices = [f" Room {room}: ${base_price}" for room in range(1, 21) if hotel[floor][room] is None]
            print("".join(room_prices))
            print()

    def CI(name, CIT, floor, RN, card, nights, suite_type):
        if hotel[floor][RN] is None:
            base_price = get_base_price(suite_type)
            total_charge = base_price * nights
            hotel[floor][RN] = (True, name, CIT, card, total_charge, 0)
            print(f"Checked in {name} to room {RN} on floor {floor} for {nights} nights at ${base_price} per night.")
            display_available_rooms(suite_type)
            return True
        else:
            print(f"Room {RN} is already occupied by {hotel[floor][RN][1]}.")
            return False

    def room_service(floor, RN, order):
        if hotel[floor][RN] is not None and hotel[floor][RN][0] == True:
            item = menu[order]["item"]
            price = menu[order]["price"]
            current_info = hotel[floor][RN]
            hotel[floor][RN] = (current_info[0], current_info[1], current_info[2], current_info[3], current_info[4], current_info[5] + price)
            print(f"{item} bought for ${price:.2f}. Added to total charge.")
        else:
            print(f"Room {RN} on floor {floor} is not occupied.")

    def CO(floor, RN):
        if hotel[floor][RN] is not None and hotel[floor][RN][0] == True:
            guest_info = hotel[floor][RN]
            total_stay_charge = guest_info[4]
            room_service_charge = guest_info[5]
            total_due = total_stay_charge + room_service_charge

            name = guest_info[1]
            card = guest_info[3]

            hotel[floor][RN] = None

            if card:
                print(f"{name} has checked out. ${total_due:.2f} has been charged to their card.")
            else:
                print(f"{name} has checked out. Total amount owed: ${total_due:.2f}.")

            feedback = input("Please provide feedback for your stay (1-5): ")
            print(f"Thank you for your feedback: {feedback} stars!")

    print("Welcome to the Hotel Management System!\n")
    display_room_types()
    print("Commands:")
    print("CI <name> <check-in time> <floor> <room number> <has credit card (True/False)> <nights> <suite type>")
    print("CO <floor> <room number>")
    print("RS <floor> <room number> <item number>")
    print("Menu to display menu items")
    print("Exit to leave the system")

    while True:
        cmd = input().strip().split()
        if cmd[0] == "CI":
            try:
                floor = int(cmd[3])
                RN = int(cmd[4])
                nights = int(cmd[6])
                suite_type = cmd[7].lower()
                if CI(cmd[1], cmd[2], floor, RN, cmd[5].lower() == 'true', nights, suite_type):
                    print("Check-in successful!\n")
            except:
                print("To check in input the name, check-in time, floor number, room number, if you have a credit card (True/False), number of nights, and suite type. Ex. (CI Bob 10/20/24 2 2 True 3 suite)\n")
        elif cmd[0] == "CO":
            try:
                CO(int(cmd[1]), int(cmd[2]))
                print()
            except:
                print("To check out input the floor number and room number only. Ex. (CO 2 2)\n")
        elif cmd[0] == "Exit":
            break
        elif cmd[0] == "Menu":
            print(menu)
            print()
        elif cmd[0] == "RS":
            if len(cmd) == 4:
                try:
                    floor = int(cmd[1])
                    RN = int(cmd[2])
                    order = int(cmd[3])
                    room_service(floor, RN, order)
                    print()
                except Exception as e:
                    print("Error in room service:", e)
                    print()
            else:
                print("To order room service, input the floor number, room number, and item number. Ex. (RS 2 2 1)\n")
        else:
            print("Use CI to check in, CO to check out, or exit to leave.\n")

main()
