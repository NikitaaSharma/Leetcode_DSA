import math


class ExamRoom:
    def __init__(self, n):
        self.seats = n
        self.room = []

    def seat(self):
        if len(self.room) == 0:
            return 0
        else:
            res = 0
            distance = self.seats.index(1)

            for seat in self.seats:
                if seat:
                    curr_dist = math.ceil(distance/2)
                    distance = 0
                    res = max(res, curr_dist)
                else:
                    distance +=1

            return max(res, distance)

    def leave(self, p):
        pass


examRoom = ExamRoom(10)
examRoom.seat()
examRoom.seat()
examRoom.seat()
examRoom.seat()
