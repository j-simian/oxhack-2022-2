import microbit

while True:
    reading = microbit.accelerometer.get_x()
    if reading > 20:
        microbit.display.show("R")
    elif reading < -20:
        microbit.display.show("L")
    else:
        microbit.display.show("-")
