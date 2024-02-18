class Star_Cinema:
    Hall_List = []

    @classmethod
    def Entry_Hall(self, obj):
        self.Hall_List.append(obj)


class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self._seats = {} # protected attribute
        self.__show_list = [] #private attribute
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def Entry_show(self, id, movie_name, time):
        item = (id, movie_name, time)
        self.__show_list.append(item)
        self._seats[id] = [[0] * self.cols for _ in range(self.rows)]

    def seats_booking(self, movie_id, row, col):
        valid_id = False
        for chk in self.__show_list:
            if chk[0] == movie_id:
                valid_id = True
                break

        if not valid_id:
            print(
                "Error: Invalid ID. You can select option 1 to view available movie IDs.")
            return
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            print(f'You information is wrong! plz again you check you row/col! ')
            return
        show_seats = self._seats.get(movie_id)
        if show_seats[row][col] == 1:
            print(f'Seat row ={row} & col ={col}) is already booked!')
        else:
            show_seats[row][col] = 1
            print(f'Booked seat successfully.')

    def view_movie_list(self):
        print("Available Movies:\n")
        print(f'     Movie Id : \t Moive Name : \t Time : ')
        print(f'_________________________________________________')
        for show in self.__show_list:
            print(f'\t{show[0]}\t\t  {show[1]}\t{show[2]}')

    def view_available_seats(self, id):
        if id not in self._seats:
            print("Invalid show ID.")
            return
        print(f"Available seats for this {id} number id : {id}")
        for row in self._seats[id]:
            print("{ ", end="")
            for seat in row:
                if seat == 0:
                    print("O", end=" ")
                else:
                    print("1", end=" ")
            print("}")


hall = Hall(rows=5, cols=5, hall_no=1)
hall.Entry_show(11, "Avatar", "10:00")
hall.Entry_show(13, "Dorodi", "1:00")
hall.Entry_show(12, "Osomoy", "2:00")
Star_Cinema.Entry_Hall(hall)


while True:
    print("\nMenu:")
    print("1. View Movie Name")
    print("2. View Available Seats")
    print("3. Book Seats")
    print("4. Exit")

    choice = int(input("Enter Option :"))
    if (choice == 1):
        hall.view_movie_list()

    elif choice == 2:
        id = int(input("which movie do you want see,Write  this Movie id: "))
        hall.view_available_seats(id)

    elif choice == 3:
        id = int(input("Enter your movie id : "))
        t = int(input("How much of a ticket do you want to buy? :"))
        for _ in range(t):
            row = int(input("Enter the number of row : "))
            col = int(input("Enter the number of col : "))
            row -= 1
            col -= 1
            hall.seats_booking(id, row, col)
    elif choice == 4:
        print("Exited Program. Thank You ")
        break
    else:
        print("Please checke your input again. And select right option! ")
