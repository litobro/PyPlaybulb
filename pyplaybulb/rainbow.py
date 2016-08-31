from pyplaybulb.playbulb import Playbulb

EFFECT_FLASH = '00'
EFFECT_PULSE = '01'
EFFECT_RAINBOW = '02'
EFFECT_RAINBOW_FADE = '03'

class Rainbow(Playbulb):
    hexa_set_colour = '0x001b'
    hexa_effect = '0x0019'
    hexa_get_colour = '0x0019'

    def set_colour(self, colour):
        self.connection.char_write(self.hexa_set_colour, colour)

    def get_colour(self):
        return self.connection.char_read(self.hexa_get_colour)

    def set_effect(self, effect_type, color, speed):
        self.connection.char_write(self.hexa_effect, color+effect_type+'00'+speed+'00')