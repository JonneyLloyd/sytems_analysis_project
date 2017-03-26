from app.models.room import Room
from app.models.room import RoomPrice

class RoomManager(object):

        @staticmethod
        def get_room(number):
        	room = Room.query.filter(Room.number == number).first()
        	result = {'number': room.number,
            'type':room.type,
            'occupancy':room.occupancy,
            'availability':room.availability,
            'clean':room.clean,
            'weekday_price':room.room_price.price_weekday,
            'weekend_price':room.room_price.price_weekend}
        	if not room:
        		return False
        	else:
        		return result


        @staticmethod
        def get_room_price_from_number(number):
        	room = Room.query.filter(Room.number == number).first()
        	result = {
            'weekday_price':room.room_price.price_weekday,
            'weekend_price':room.room_price.price_weekend}
        	if not room:
        		return False
        	else:
        		return result

        @staticmethod
        def get_room_price_from_type(room_type):
            room = RoomPrice.query.filter(RoomPrice.type == room_type).first()
            if not room:
                return False
            result = {
            'weekday_price':room.price_weekday,
            'weekend_price':room.price_weekend}
            return result
