class Reservation():

    def __init__(self,id,reservation_name,date,hour,guest_number,event_type=None) -> None:
        self.id=id
        self.reservation_name=reservation_name
        self.date=date
        self.hour=hour
        self.guest_number=guest_number
        self.event_type=event_type
    
    def to_JSON(self):
        return {
            'id': self.id,
            'reservation_name':self.reservation_name,
            'date': self.date,
            'hour': self.hour,
            'guest_number': self.guest_number,
            'event_type': self.event_type       
        }
