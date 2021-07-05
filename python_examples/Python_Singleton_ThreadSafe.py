import threading

class ParkingLot:

    __instance = None

    @staticmethod
    def getInstance(self):
        if not ParkingLot.__instance:
            with threading.Lock():
                if not ParkingLot.__instance:
                    ParkingLot()
        return ParkingLot.__instance

    def __init__(self):

        if ParkingLot.__instance:
            raise Exception(' Parking Lot already created ')

        ParkingLot.__instance = self








