import json
from datetime import time
from database.db import get_connection
from .entities.Reservation import Reservation

class ReservationModel():

    @classmethod
    def get_reservations(self):
        try:
            connection=get_connection() 
            reservations=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, reservation_name, date, hour, guest_number, event_type FROM reservation ORDER BY date ASC")
                resultset=cursor.fetchall()
                
                for row in resultset:
                    date_str = row[2].strftime('%Y-%m-%d')
                    hour_str = row[3].strftime('%H:%M:%S')
                    reservation = Reservation(row[0],row[1], date_str, hour_str, row[4], row[5])
                    reservations.append(reservation.to_JSON())
                    
            connection.close()
            return reservations
        
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_reservation(cls, reservation):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO reservation (reservation_name, date, hour, guest_number, event_type) 
                            VALUES (%s, %s, %s, %s, %s)""", (reservation.reservation_name, reservation.date, 
                            reservation.hour, reservation.guest_number, reservation.event_type))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def update_reservation(self, reservation):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE reservation SET reservation_name = %s, date = %s, hour = %s, guest_number = %s, event_type = %s 
                                WHERE id = %s""", (reservation.reservation_name, reservation.date, reservation.hour, reservation.guest_number, reservation.event_type))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
