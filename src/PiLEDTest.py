import hal.hal_input_switch as swch
import hal.hal_led as Led
from time import sleep

swch.init()
Led.init()

def bqn():
  position = swch.read_slide_switch()
  if position == 1:
    Led.set_output(24,True)
    sleep(0.2)
    Led.set_output(24,False)
    sleep(0,2)
  elif position == 0:
    i=0
    while i<25:
      Led.set_output(24,True)
      sleep(0.1)
      Led.set_output(24, False) 
      sleep(0.1)
      i=i+1
    quit()

while True:
  bqn()

  