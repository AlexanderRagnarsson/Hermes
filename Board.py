class Board:
    def __init__(self) -> None:
        self.__board_arr = []
        for _ in range(8):
            self.__board_arr.append([0]*8)

    def contains_piece_on(self,x,y):
        return 0 <= x < 8 and 0 <= y < 8 and self.__board_arr[y][x] != 0

    def get_piece_on(self,x,y):
        if not (0 <= x < 8 and 0 <= y < 8):
            return -1
        return self.__board_arr[y][x]

    def move_piece(self,x1,y1,x2,y2):
        self.__board_arr[y2][x2] = self.__board_arr[y1][x1]
        self.__board_arr[y1][x1] = 0

    def add_piece(self,piece,x,y):
        self.__board_arr[y][x] = piece

    def remove_piece(self,x,y):
        self.__board_arr[y][x] = 0

    def get_arr(self):
        return self.__board_arr

    def is_valid(self,x,y):
        return 0 <= x < 8 and 0 <= y < 8

    def __copy__(self):
        board = Board()
        board_arr = board.get_arr()
        for i in range(8):
            for j in range(8):
                board_arr[i][j] = self.__board_arr[i][j].copy()

    def __eq__(self, o: object) -> bool:
        if type(o) != Board:
            return False
        for i in range(8):
            for j in range(8):
                if self.__board_arr[i][j] != o.__board_arr[i][j]:
                    return False
        return True

    def __str__(self) -> str:
        return "\n".join([" ".join([str(j) if j != 0 else "0 " for j in i]) for i in self.__board_arr])
