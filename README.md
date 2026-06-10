# ⌨️ Custom Manenti Macropad

This project consists of the complete development of a custom macropad keyboard, integrating the electronic circuit in **KiCad** and the case modeling in **Autodesk Fusion**.


## 📸 Project Demo

### Render / Screenshot of the Macropad Design

![Closed case](./images/box.png)

### Technical Drawing and 3D Modeling of the Case

![Opened case](./images/opened_box.png)

---

## ⚡ Electronic Development (KiCad)

The circuit was designed to be compact and functional, using a microcontroller on one side of the board and the three switches on the other. The design has mounting holes strategically positioned in the four corners of the board.

### Electrical Schematic

![Electrical Schematic in KiCad](./images/electric_schema.png)

### PCB Layout (Edge Cuts and Traces)

![PCB Layout](./images/PCB_layout.png)

---

## 🛠️ Case Specifications (Fusion 360)

I modeled the panel case from scratch in Fusion using the .STEP file exported from KiCad as a base to get the correct measurements; I made something simple, but functional.

- **Internal PCB tolerance:** `0.4 mm` on each side to ensure clearance during assembly.
- **Wall thickness:** `13.0 mm` for high structural and acoustic resistance.
- **Base thickness:** `3.0 mm`.
- **cut to USB:** Aligned with the physical connector.
- **Mounting:** 4 reinforcing columns at the corners of the plate (taking care not to touch any "wires") with **Ø 4.7 mm** holes for screw installation.

---

## 📦 Bill of Materials

The table below lists all components required for the complete assembly of the structure:

| Item | Component                   | Quantity | Description / Specification                                |
| :--- | :-------------------------- | :------: | :--------------------------------------------------------- |
| 1    | Custom PCB                  |    1     | Printed circuit board developed in KiCad                   |
| 2    | XIAO_RP2040 microcontroller |    1     | Seeed Studio XIAO RP2040 or CircuitPython-compatible board |
| 3    | Mechanical switches         |    3     | Cherry MX-style switches or compatible                     |
| 4    | Keycaps                     |    3     | Keycaps compatible with MX switches                        |
| 5    | LEDs                        |    3     | LEDs connected to pin D3                                   |
| 6    | Heat-set inserts            |    4     | M3 × 5 × 4 mm brass inserts                                |
| 7    | M3 screws                   |    4     | M3 × 16 mm screws                                          |
| 8    | Bottom case                 |    1     | 3D-printed part based on the `Bottom.STEP` file            |
| 9    | Top cover / switch plate    |    1     | 3D-printed part based on the `Top.STEP` file               |
| 10   | USB-C cable                 |    1     | Cable for connecting the macropad to the computer          |

---# ⌨️ Custom Tecladinho Macropad

The macropad was designed to execute quick music commands:

- Key 1: previous track
- Key 2: next track
- Key 3: pause/play

---

## ⚡ Electronic Development

The project uses a CircuitPython-compatible microcontroller and three mechanical keys for media control.

### Used pins

| Function               | Pin |
| Key 1 — previous track | D0  |
| Key 2 — next track     | D1  |
| Key 3 — play/pause     | D2  |
| LEDs                   | D3  |

The three keys are used as digital inputs in the firmware, while the LEDs are controlled by pin D3.

---

## 💻 Firmware

The firmware was developed using **KMK**, which runs on top of **CircuitPython**. This choice makes keyboard configuration easier, allowing the key behavior to be edited directly in Python.

### Main file

The main firmware must be saved on the XIAO as:

```text
main.py
```

---


## 🚀 Exporting Files for Production

The mechanical files must be exported in **.STEP** format, not STL, to preserve the CAD geometry.

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

---


## 🧠 Author

Project developed by **Arthur Lima Manenti** as a custom 3-key macropad for media control.

---

I declared the use of AI in this Readme.md to form the basis of the document, but I checked and edited everything that was inconsistent and repetitive.
