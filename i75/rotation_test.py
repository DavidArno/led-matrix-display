from graphics import Matrix
from time import sleep

matrix = Matrix()
pen = matrix.display.create_pen(255, 0,0)
matrix.display.clear()
matrix.display.set_pen(pen)
matrix.display.rectangle(7, 7, 48, 10)
matrix.update()


# print(2)
# display = PicoGraphics(DISPLAY_INTERSTATE75_64X64)
# print(3)
# pen = display.create_pen(255, 0,0)
# print(4)
# display.clear()
# display.set_pen(pen)
# display.rectangle(7, 7, 48, 10)
# print(5)
# hub75 = hub75.Hub75(64, 64, panel_type=DISPLAY_INTERSTATE75_64X64)
# hub75.start()
# hub75.update(display)
# print(6)
sleep(2)
matrix.rotate(90)
sleep(2)
matrix.rotate(180)
sleep(2)
matrix.rotate(270)
sleep(2)
matrix.rotate(0)
sleep(2)

