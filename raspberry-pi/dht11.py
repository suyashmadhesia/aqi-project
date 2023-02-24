def read_dht():
    data = bytearray(5)
    # Send start signal to the sensor
    dht_pin.init(machine.Pin.OUT)
    dht_pin.low()
    time.sleep(0.018)
    dht_pin.high()
    dht_pin.init(machine.Pin.IN, machine.Pin.PULL_UP)
    # Wait for the sensor to respond
    for i in range(10000):
        if dht_pin.value() == 0:
            break
    else:
        raise OSError("Sensor did not respond")
    # Read the data from the sensor
    for i in range(5):
        data[i] = 0
        for j in range(8):
            while dht_pin.value() == 0:
                pass
            time.sleep_us(30)
            if dht_pin.value() == 1:
                data[i] |= 1 << (7 - j)
        dht_pin.init(machine.Pin.OUT)
        dht_pin.low()
        time.sleep_us(40)
        dht_pin.high()
    # Checksum validation
    if (data[0] + data[1] + data[2] + data[3]) & 0xff != data[4]:
        raise OSError("Checksum error")
    # Calculate temperature and humidity values
    humidity = data[0]
    temperature_c = data[2]
    return temperature_c, humidity
