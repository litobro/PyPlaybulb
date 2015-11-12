from subprocess import check_output

class gattpy:
    mac_address = None
    def __init__(self, mac_id):
        self.mac_address = mac_id

    def char_write(self, hnd, data):
        data = check_output(['gatttool', '-b', self.mac_address, '--char-write', '-a', hnd, '-n', data])
        return data.decode('utf-8')

    def char_read(self, hnd):
        data = check_output(['gatttool', '-b', self.mac_address, '--char-read', '-a', hnd])
        return data.decode('utf-8').split(':')[1].strip()
