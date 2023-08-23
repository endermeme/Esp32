import machine
import ili9341

# config socket 
spi = machine.SPI(
    1,
    baudrate=40000000,
    sck=machine.Pin(18),
    mosi=machine.Pin(23)
)

# control config socket 
lcd = ili9341.ILI9341(
    spi,
    cs=machine.Pin(5),
    dc=machine.Pin(4),
    rst=machine.Pin(2),
    width=320,
    height=240
)

# làm mới màn hình 
lcd.fill(ili9341.color565(0, 0, 0))

# hiển thị chữ 
lcd.text('Hello, ESP32!', 10, 10, ili9341.color565(255, 255, 255))
lcd.show()
