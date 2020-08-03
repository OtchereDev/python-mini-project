class Journey():
    def __init__(self,*movement_list) :
        self.travel= movement_list
    def round_trip(self):
        x_pos, y_pos= 0, 0
        for movement in self.travel:
            x_pos += movement[0]
            y_pos  += movement[1]
        return x_pos==0 and y_pos ==0

oliver_movement=[[10,12],[-16,15],[25,-50]]
olivers_round = Journey(*oliver_movement)
print(olivers_round.round_trip())