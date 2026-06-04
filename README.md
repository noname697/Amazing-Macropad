# ⌨️ Custom Tecladinho Macropad

This project consists of the complete development of a custom macropad keyboard, integrating the electronic circuit design in **KiCad** and the mechanical case modeling in **Autodesk Fusion 360**. The project was parametrically dimensioned to ensure precise fits and proper holes for threaded inserts (heatsets).

---

## 📸 Project Demo

### Render / Screenshot of the Macropad Design

![Closed case](./images/box.png)

### Technical Drawing and 3D Modeling of the Case

![Opened case](./images/opened_box.png)

---

## ⚡ Electronic Development (KiCad)

The circuit was designed to be compact and functional, using a centralized microcontroller and mounting holes strategically positioned in the four corners of the board.

### Electrical Schematic

![Electrical Schematic in KiCad](./images/electric_schema.png)

### PCB Layout (Edge Cuts and Traces)

![PCB Layout](./images/PCB_layout.png)

---

## 🛠️ Case Specifications (Fusion 360)

The bottom case was modeled using parametric design techniques based on the STEP file exported from KiCad, following these technical specifications:

* **Internal PCB tolerance:** `0.4 mm` on each side to ensure clearance during assembly.
* **Wall thickness:** `10.0 mm` for high structural and acoustic resistance.
* **Base thickness:** `3.0 mm`.
* **USB-C port cutout:** Aligned with the physical connector and with a `0.2 mm` clearance.
* **Mounting:** 4 reinforcement columns (*bosses*) in the corners with flat-bottom blind holes of **Ø 4.7 mm** for installing brass heat-set inserts.

---

## 📦 Bill of Materials (BOM)

The table below lists all components required for the complete assembly of the hardware and mechanical structure:

| Item | Component                   | Quantity | Description / Specification                                |
| :--- | :-------------------------- | :------: | :--------------------------------------------------------- |
| 1    | Custom PCB                  |     1    | Printed circuit board developed in KiCad                   |
| 2    | XIAO_RP2040 microcontroller |     1    | Seeed Studio XIAO RP2040 or CircuitPython-compatible board |
| 3    | Mechanical switches         |     3    | Cherry MX-style switches or compatible                     |
| 4    | Keycaps                     |     3    | Keycaps compatible with MX switches                        |
| 5    | LEDs                        |     3    | LEDs connected to pin D3                                   |
| 6    | Heat-set inserts            |     4    | M3 × 5 × 4 mm brass inserts                                |
| 7    | M3 screws                   |     4    | M3 × 16 mm screws                                          |
| 8    | Bottom case                 |     1    | 3D-printed part based on the `Bottom.STEP` file            |
| 9    | Top cover / switch plate    |     1    | 3D-printed part based on the `Top.STEP` file               |
| 10   | USB-C cable                 |     1    | Cable for connecting the macropad to the computer          |

---# ⌨️ Custom Tecladinho Macropad

This project consists of the complete development of a **custom 3-key macropad**, integrating the electronic design made in **KiCad**, the mechanical case modeling in **Autodesk Fusion 360**, and the firmware in **KMK/CircuitPython** for media control.

The macropad was designed to execute quick music commands:

* Key 1: previous track
* Key 2: next track
* Key 3: pause/play

---

## ⚡ Electronic Development

The PCB was developed in **KiCad** with a focus on simplicity and compactness. The project uses a CircuitPython-compatible microcontroller and three mechanical keys for media control.

### Used pins

| Function               | Pin |
| :--------------------- | :-: |
| Key 1 — previous track |  D0 |
| Key 2 — next track     |  D1 |
| Key 3 — play/pause     |  D2 |
| LEDs                   |  D3 |

The three keys are used as digital inputs in the firmware, while the LEDs are controlled by pin D3.

---

## 💻 Firmware

The firmware was developed using **KMK**, which runs on top of **CircuitPython**. This choice makes keyboard configuration easier, allowing the key behavior to be edited directly in Python.

### Key functions

| Key | Action         |
| :-: | :------------- |
|  1  | Previous track |
|  2  | Next track     |
|  3  | Play/Pause     |

### Main file

The main firmware must be saved on the XIAO as:

```text
main.py
```

### Base code

```python
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

# Keys connected to pins D0, D1, and D2.
# Each key connects to GND when pressed.
keyboard.matrix = KeysScanner(
    pins=(board.D0, board.D1, board.D2),
    value_when_pressed=False,
    pull=True,
)

# Keymap:
# Key 1: previous track
# Key 2: next track
# Key 3: play/pause
keyboard.keymap = [
    [
        KC.MPRV,
        KC.MNXT,
        KC.MPLY,
    ]
]

# LEDs connected to pin D3.
# This block assumes NeoPixel/WS2812 addressable LEDs.
try:
    import neopixel

    NUM_LEDS = 3

    leds = neopixel.NeoPixel(
        board.D3,
        NUM_LEDS,
        brightness=0.25,
        auto_write=True,
    )

    leds.fill((0, 0, 255))

except Exception:
    pass


if __name__ == "__main__":
    keyboard.go()
```

---

## 🛠️ Mechanical Modeling

The case was modeled in **Autodesk Fusion 360** based on the PCB dimensions exported from KiCad in STEP format.

The model is divided into two parts:

* `Top.STEP` — top cover / switch plate
* `Bottom.STEP` — bottom base of the case

### Case specifications

| Element                | Specification                                    |
| :--------------------- | :----------------------------------------------- |
| Internal PCB clearance | 0.4 mm on each side                              |
| Base thickness         | 3 mm                                             |
| Wall height            | Adjusted to protect the PCB and align the USB-C  |
| USB-C cutout           | Aligned with the physical connector on the board |
| Internal mounting      | Columns with heat-set inserts                    |
| Insert holes           | Ø 4.7 mm × 4 mm deep                             |
| Screws                 | M3 × 16 mm                                       |

---

## 🚀 Exporting Files for Production

The mechanical files must be exported in **STEP** format, not STL, to preserve the CAD geometry with greater precision.

### Required files

```text
Top.STEP
Bottom.STEP
```

### Exporting in Fusion 360

1. In Fusion 360, make only the part you want to export visible.
2. Hide the PCB and the other components.
3. Right-click the desired component.
4. Select **Export**.
5. Choose the **STEP** format.
6. Export each part separately:

```text
Top.STEP     → top cover / switch plate
Bottom.STEP  → bottom base of the case
```

---

## 📁 Suggested repository structure

```text
tecladinho-macropad/
├── README.md
├── firmware/
│   └── code.py
├── case/
│   ├── Top.STEP
│   └── Bottom.STEP
├── kicad/
│   ├── esquema/
│   └── pcb/
└── images/
    ├── box.png
    ├── electric_schema.png
    ├── opened_box.png
    └── PCB_layout.png
```

---

## ✅ Project Status

* [x] Electrical schematic in KiCad
* [x] PCB layout
* [x] Bottom case modeling
* [x] Top cover modeling
* [x] Basic firmware in KMK
* [x] STEP file export
* [ ] Physical assembly
* [ ] Final firmware test

---

## 🧠 Author

Project developed by **Arthur Lima Manenti** as a custom 3-key macropad for media control.

## 🚀 How to Export the Files for Production

According to the project guidelines, the structural files must be exported and submitted in **.STEP** format to preserve the exact curves and geometries for the 3D printing team:

1. In Fusion 360, go to **File ➔ Export**.
2. Change the file type to **.STEP**.
3. Export both parts separately:

   * `Topo.STEP` — The top switch plate.
   * `Inferior.STEP` — The bottom shell/case.

