import json
from datetime import time, datetime
from database.db import get_connection
from .entities.Reservation import Reservation

class ReservationModel():

    @classmethod
    def get_reservations(self):
        try:
            connection=get_connection() 
            reservations=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, reservation_name,uid, date, hour, guest_number, event_type FROM reservation ORDER BY date ASC")
                resultset=cursor.fetchall()
                
                for row in resultset:
                    date_str = row[3].strftime('%Y-%m-%d')
                    hour_str = row[4].strftime('%H:%M:%S')
                    reservation = Reservation(row[0],row[1],row[2], date_str, hour_str, row[5], row[6])
                    reservations.append(reservation.to_JSON())
            print(reservations)       
            connection.close()
            return reservations
        
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_reservation(cls, reservation):
        try:
            connection = get_connection()
            print(reservation.reservation_name)
            print(reservation.uid)
            print(reservation.date)
            print(reservation.hour)
            print(reservation.guest_number)
            print(reservation.event_type)
            with connection.cursor() as cursor:
                cursor.execute(f"""INSERT INTO reservation (reservation_name, uid,date, hour, guest_number, event_type) 
                            VALUES ('{reservation.reservation_name}','{reservation.uid}', '{reservation.date}', '{reservation.hour}', {reservation.guest_number}, '{reservation.event_type}')""",
                            )

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
            print(reservation.id)

            with connection.cursor() as cursor:
                cursor.execute(f"""UPDATE reservation SET reservation_name = '{reservation.reservation_name}',uid = '{reservation.uid}', date ='{reservation.date}', hour ='{reservation.hour}' , guest_number = {reservation.guest_number}, event_type = '{reservation.event_type}' 
                                WHERE id = {reservation.id}""")
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def delete_reservation(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(f"""DELETE FROM reservation WHERE id = {id}""")
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_reservation_by_id(self, id):
        try:
            connection=get_connection() 
            reservations=[]

            with connection.cursor() as cursor:
                cursor.execute(f"SELECT id, reservation_name,uid, date, hour, guest_number, event_type FROM reservation WHERE id = {id}")
                resultset=cursor.fetchall()
                
                for row in resultset:
                    date_str = row[3].strftime('%Y-%m-%d')
                    hour_str = row[4].strftime('%H:%M:%S')
                    reservation = Reservation(row[0],row[1],row[2], date_str, hour_str, row[5], row[6])
                    reservations.append(reservation.to_JSON())
                    
            connection.close()
            return reservations
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_reservation_by_date(self, date):
        try:
            connection=get_connection() 
            reservations=[]

            with connection.cursor() as cursor:
                cursor.execute(f"SELECT id, reservation_name,uid, date, hour, guest_number, event_type FROM reservation WHERE date = '{date}'")
                resultset=cursor.fetchall()
                
                for row in resultset:
                    date_str = row[3].strftime('%Y-%m-%d')
                    hour_str = row[4].strftime('%H:%M:%S')
                    reservation = Reservation(row[0],row[1], row[2],date_str, hour_str, row[5], row[6])
                    reservations.append(reservation.to_JSON())
                    
            connection.close()
            return reservations
        
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_reservation_by_hour(self,date, hour):
        try:
            connection=get_connection() 
            reservations=[]

            with connection.cursor() as cursor:
                cursor.execute(f"SELECT id, reservation_name,uid, date, hour, guest_number, event_type FROM reservation WHERE hour = '{hour}' and date = '{date}'")
                resultset=cursor.fetchall()
                
                for row in resultset:
                    date_str = row[3].strftime('%Y-%m-%d')
                    hour_str = row[4].strftime('%H:%M:%S')
                    reservation = Reservation(row[0],row[1],row[2], date_str, hour_str, row[5], row[6])
                    reservations.append(reservation.to_JSON())
                    
            connection.close()
            return reservations
        
        except Exception as ex:
            raise Exception(ex)
    

