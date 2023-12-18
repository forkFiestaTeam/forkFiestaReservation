from flask import Blueprint, jsonify, request
from datetime import time, datetime
#Entities
from models.entities.Reservation import Reservation

#Models
from models.ReservationModel import ReservationModel

main=Blueprint('reservation_blueprint',__name__)

@main.route('/')
def get_resevation():
    try:
        reservations=ReservationModel.get_reservations()
        return jsonify(reservations)
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500
    
@main.route('/add', methods=['POST'])
def add_reservation():
    try:
        data = request.json
        reservation_name = data['reservation_name']
        uid = data['uid']
        date = data['date']
        hour = data['hour']
        guest_number = data['guest_number']
        event_type = data['event_type']
        # Create an instance of Reservation with the parsed data
        reservation = Reservation(0,reservation_name,uid, date, hour, guest_number, event_type)

        # Call the function to add the reservation in your model
        affected_rows = ReservationModel.add_reservation(reservation)

        if affected_rows == 1:
            return jsonify({'message': 'Reservation added successfully'})
        else:
            return jsonify({'message': 'Error on insert'}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update/<int:id>', methods=['PUT'])
def update_reservation(id):
    try:
        data = request.json
        if 'reservation_name' in data and 'uid' in data and'date' in data and 'hour' in data and 'guest_number' in data and 'event_type' in data:
            reservation_name = data['reservation_name']
            uid = data['uid']
            date = data['date']
            hour = data['hour']
            guest_number = data['guest_number']
            event_type = data['event_type']

            reservation = Reservation(id, reservation_name,uid, date, hour, guest_number, event_type)

            affected_rows = ReservationModel.update_reservation(reservation)

            if affected_rows == 1:
                return jsonify(reservation.id)
            else:
                return jsonify({'message': "No reservation updated"}), 404
        else:
            return jsonify({'message': "Invalid request data"}), 400

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/delete/<int:id>', methods=['DELETE'])
def delete_reservation(id):
    try:
        affected_rows = ReservationModel.delete_reservation(id)
        if affected_rows == 1:
            return jsonify({'message': 'Reservation deleted successfully'})
        else:
            return jsonify({'message': 'Reservation not found'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/<int:id>')
def get_reservation_by_id(id):
    try:
        reservation = ReservationModel.get_reservation_by_id(id)
        if reservation:
            return jsonify(reservation)
        else:
            return jsonify({'message': 'Reservation not found'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<string:date>')
def get_reservation_by_date(date):
    try:
        reservation = ReservationModel.get_reservation_by_date(date)
        if reservation:
            return jsonify(reservation)
        else:
            return jsonify({'message': 'Reservation not found'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/<string:date>/<string:hour>')
def get_reservation_by_hour(date, hour):
    try:
        reservation = ReservationModel.get_reservation_by_hour(date, hour)
        if reservation:
            return jsonify(reservation)
        else:
            return jsonify({'message': 'Reservation not found'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
