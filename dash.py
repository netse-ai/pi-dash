from io import BytesIO
from time import sleep
from picamera import PiCamera

my_stream = BytesIO()
caerma = PiCamera()
camera.start_preview()
sleep(2)
# camera.capture(my_stream, 'jpeg')
