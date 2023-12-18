class Reservation():

    def __init__(self,id,reservation_name,uid,date,hour,guest_number,event_type) -> None:
        self.id=id
        self.reservation_name=reservation_name
        self.uid=uid
        self.date=date
        self.hour=hour
        self.guest_number=guest_number
        self.event_type=event_type
    
    def to_JSON(self):
        return {
            'id': self.id,
            'reservation_name':self.reservation_name,
            'uid':self.uid,
            'date': self.date,
            'hour': self.hour,
            'guest_number': self.guest_number,
            'event_type': self.event_type       
        }
