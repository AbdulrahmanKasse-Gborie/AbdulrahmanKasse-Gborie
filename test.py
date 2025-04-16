import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
INPUT_PIN = 17  # GPIO17

GPIO.setup(INPUT_PIN, GPIO.IN)

try:
    print("Monitoring power supply signal...")
    while True:
        if GPIO.input(INPUT_PIN):
            print("Power is ON (HIGH)")
        else:
            print("Power is OFF (LOW)")
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Stopped.")
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
INPUT_PIN = 17  # GPIO17

GPIO.setup(INPUT_PIN, GPIO.IN)

try:
    print("Monitoring power supply signal...")
    while True:
        if GPIO.input(INPUT_PIN):
            print("Power is ON (HIGH)")
        else:
            print("Power is OFF (LOW)")
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Stopped.")
