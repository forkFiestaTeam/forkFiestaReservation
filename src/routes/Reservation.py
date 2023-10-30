from flask import Blueprint, jsonify, request

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
        data = request.json  # Debes obtener los datos del JSON correctamente
        reservation_name = data['reservation_name']
        date = data['date']
        hour = data['hour']
        guest_number = data['guest_number']
        event_type = data['event_type']

        

        # Crea una instancia de Reservation con los datos recibidos
        reservation = Reservation( reservation_name, date, hour, guest_number, event_type)

        # Llama a la función para agregar la reserva en tu modelo
        affected_rows = ReservationModel.add_reservation(reservation)

        if affected_rows == 1:
            return jsonify({'message': 'Reservation added successfully', 'id': reservation.id})
        else:
            return jsonify({'message': 'Error on insert'}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_reservation(id):
    try:
        reservation_name = request.json['reservation_name']
        date = request.json['date']
        hour = request.json['hour']
        guest_number = request.json['guest_number']
        event_type = request.json['event_type']
        reservation = Reservation(id, reservation_name, date, hour, guest_number, event_type)

        affected_rows = ReservationModel.update_reservation(reservation)

        if affected_rows == 1:
            return jsonify(reservation.id)
        else:
            return jsonify({'message': "No reservation updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
