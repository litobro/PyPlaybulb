from gatt import gattpy

class Playbulb:
    hexa_name= '0x0003'
    hexa_application_version = '0x0023'
    hexa_microprocessor_version= '0x0021'
    hexa_manufacturer= '0x0025'
    hexa_brightness= '0x0010'
    hexa_set_colour= ''
    hexa_get_colour= ''
      
    def __init__(self, mac_id):
        self.mac_address = mac_id
        self.connection = gattpy(mac_id)

    def set_colour(self, colour):
        raise NotImplementedError

    def get_colour(self):
        raise NotImplementedError

    def get_name(self):
        string_hexa = self.connection.char_read(self.hexa_name)
        return bytes.fromhex(string_hexa).decode('utf-8')

    def get_application_version(self):
        string_hexa = self.connection.char_read(self.hexa_application_version)
        return bytes.fromhex(string_hexa).decode('utf-8')

    def get_microprocessor_version(self):
        string_hexa = self.connection.char_read(self.hexa_microprocessor_version)
        return bytes.fromhex(string_hexa).decode('utf-8')

    def get_manufacturer(self):
        string_hexa = self.connection.char_read(self.hexa_manufacturer)
        return bytes.fromhex(string_hexa).decode('utf-8')

if __name__ == '__main__':
    c = Playbulb('94:FC:4B:0A:AC:E6')
    print(c.get_name())
    print(c.get_application_version())
