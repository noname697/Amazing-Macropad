import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

# Teclas ligadas diretamente nos pinos D0, D1 e D2
# Cada botão deve fechar contato com GND quando pressionado.
keyboard.matrix = KeysScanner(
    pins=(board.D0, board.D1, board.D2),
    value_when_pressed=False,
    pull=True,
)

# Mapa das teclas:
# Tecla 1: música anterior
# Tecla 2: próxima música
# Tecla 3: play/pause
keyboard.keymap = [
    [
        KC.MPRV,  # Previous track
        KC.MNXT,  # Next track
        KC.MPLY,  # Play/Pause
    ]
]

# LEDs na porta D3
# Esta parte é para LEDs NeoPixel/WS2812.
# Se você não estiver usando LEDs endereçáveis, pode apagar este bloco.
try:
    import neopixel

    NUM_LEDS = 3  # Altere para a quantidade real de LEDs que você colocou

    leds = neopixel.NeoPixel(
        board.D3,
        NUM_LEDS,
        brightness=0.25,
        auto_write=True,
    )

    # Cor inicial dos LEDs: azul
    leds.fill((0, 0, 255))

except Exception:
    # Se a biblioteca neopixel não estiver instalada,
    # o teclado continua funcionando normalmente.
    pass


if __name__ == "__main__":
    keyboard.go()
