![highway by hack club banner](https://camo.githubusercontent.com/326e94989ced0720460894e97d36883bb0eebae2757b1bbadd0797fa86edd747/68747470733a2f2f68632d63646e2e68656c312e796f75722d6f626a65637473746f726167652e636f6d2f732f76332f306262636361363866666133383435333030626237363934306638616439316664353364326436385f30362d33302d323032352d313631382e706e67)

# numhackpad

numhackpad is a 16 key macropad with nothing else except for cool oneshot art

## Features:
- 16 keys
- cool oneshot reference on the pcb

## CAD Model:
the case and pcb should fit nicely with 8 m3 screws and heatset inserts. 4 for the case, 4 for the PCB (standoffs).

it has 2 printed pieces: the bottom and the top of the case

![top](https://hc-cdn.hel1.your-objectstorage.com/s/v3/aa0dce6b94d13610377e439fdee1426dac5653a7_screenshot_2025-07-06_at_4.48.40___pm.png)
![bottom](https://hc-cdn.hel1.your-objectstorage.com/s/v3/11bd733bad6728e32ada1485eecb76ba7b07c981_image.png)
![put together](https://hc-cdn.hel1.your-objectstorage.com/s/v3/9efde0e97415c62855aad832330b958e58d98b36_screenshot_2025-07-06_at_4.48.27___pm.png)
![put together again](https://hc-cdn.hel1.your-objectstorage.com/s/v3/8952adb2fd979d32f4bdc9ba582b261e89a0188b_screenshot_2025-07-06_at_4.48.32___pm.png)
made using Fusion360

## PCB
heres the pcb, it was made using KiCAD and the silkscreen was taken from a google image of the oneshot lightbulb (no spoilers!)
schematic
![schematic](https://hc-cdn.hel1.your-objectstorage.com/s/v3/3be1e634152d126c7a05665ef1133a6337b589cd_screenshot_2025-07-06_at_3.07.36___pm.png)

pcb
![3d pcb view](https://hc-cdn.hel1.your-objectstorage.com/s/v3/c30d65369d4980343ac0f1afb61ffbed3f5bc94a_image.png)
![2d pcb view](https://hc-cdn.hel1.your-objectstorage.com/s/v3/4202c5608baf8b70ccc33942978632d598f2eb9c_image.png)

used cherry MX for the footprints

## Firmware Overview
numhackpad uses [KMK](https://github.com/KMKfw) firmware.

- the 16 keys act as a numpad, it is missing the delete key

## BOM:
here should be everything you need to make this hackpad

- 16x Cherry MX Switches
- 16x DSA Keycaps
- 8x M3x5x4 Heatset inserts
- 8x M3x16mm screws
- 16x 1N4148 DO-35 Diodes.
- 1x XIAO RP2040
- 1x Case (2 printed parts)
- 1x PCB


## Extra stuff
lwk it started off as a normal hackpad and then got a lot worse