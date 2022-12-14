import serial

s_inst = serial.Serial()
s_inst.baudrate = 115200
s_inst.port ='COM3'
s_inst.open()


def bitman(roll, pitch):
    a, b = False, False
    packet = None

    if s_inst.in_waiting:
        try:
            packet = s_inst.readline().decode('utf')
        except:
            packet = s_inst.readline().decode('utf')

    if packet:
        packet = packet.strip().split()

        if len(packet) == 1:
            if packet[0] == 'A':
                a = True
            elif packet[0] == 'B':
                b = True
            elif packet[0] == 'AB':
                a, b = True, True

        elif len(packet) == 2:
            magnitude, direction = packet
            if direction == "ROLL":
                roll = int(magnitude)
            if direction == "PITCH":
                pitch = int(magnitude)

    return roll, pitch, a, b
