class Office:
    def __init__(self, hours, days, roomNum, building):
        self.Location = {"RoomNumber": roomNum, "Building": building}
        self.Days = days
        self.Hours = hours
    