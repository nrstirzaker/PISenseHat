from sense_hat import SenseHat
import time

sense = SenseHat()


b = (0, 128, 255) # Blue

m = (153, 0, 76) # Magenta

y = (255, 255, 0) # Yellow

w = (200, 200, 200) # White

e = (0, 0, 0,) # Empty


pet1 = [
    e, e, e, e, e, e, e, e,
    m, e, e, e, e, e, e, e,
    e, m, e, e, m, e, m, e,
    e, m, b, b, m , y, y, e,
    e, b, b, b, y, w, y, b,
    e, b, b, b, y, y, y, e,
    e, b, e, b, e, b, e, e,
    e, e, e, e, e, e, e, e,
    ]

pet2 = [
    e, e, e, e, e, e, e, e,
    e, e, m, e, e, e, e, e,
    e, m, e, e, m, e, m, e,
    e, m, b, b, m , y, y, e,
    e, b, b, b, y, w, y, b,
    e, b, b, b, y, y, y, e,
    e, e, b, e, b, e, e, e,
    e, e, e, e, e, e, e, e,
    ]
def walking():
    for i in range(10):
        sense.set_pixels(pet1)
        time.sleep(0.5)
        sense.set_pixels(pet2)
        time.sleep(0.5)

sense.clear()

x, y, z = sense.get_accelerometer_raw().values()

while x<2 and y<2 and z<2:
    x, y, z = sense.get_accelerometer_raw().values()
    walking()    
 
