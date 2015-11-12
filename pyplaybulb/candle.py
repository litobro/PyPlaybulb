from subprocess import check_output
from gatt import gattpy

class candle:
    mac_address = None
    name = None
    connection = None

    def __init__(self, mac_id):
        self.mac_address = mac_id
        self.connection = gattpy(mac_id)

    def set_colour(self, colour):
        self.connection.char_write('0x0019', colour)

    def get_colour(self):
        return self.connection.char_read('0x0019')


if __name__ == '__main__':
    c = candle('90:CF:4B:0B:AC:E6')
    c.set_colour('00FF0000')
    print(c.get_colour())
