import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner, DiodeOrientation
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.row_pins = (board.GP27, board.GP28, board.GP29, board.GP6, board.GP7)
keyboard.col_pins = (board.GP3, board.GP4, board.GP2, board.GP1)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        # row 1
        KC.NLCK, KC.PSLS, KC.PAST, KC.PMNS,

        # row 2
        KC.P7, KC.P8, KC.P9, KC.PPLS, 

        # row 3
        KC.P4, KC.P5, KC.P6, KC.PDOT,

        # row 4
        KC.P1, KC.P2, KC.P3, KC.PENT,
        
        # row 5
        KC.P0, KC.NO, KC.NO, KC.NO
    ]
]

if __name__ == '__main__':
    keyboard.go()