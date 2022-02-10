import time
import os
import logging
from commanduino import CommandManager

logging.basicConfig(level=logging.INFO)

script_dir = os.path.dirname(__file__)
cm_config = os.path.join(script_dir, 'demo.json')
cmdMng = CommandManager.from_configfile(cm_config)

stepper = cmdMng.stepper

stepper.set_current_position(0)

stepper.enable_acceleration()
stepper.set_acceleration(1000)
stepper.set_max_speed(10000)

print('Moving to 20000 with acceleration 1000')
stepper.move_to(-2000, wait=True)

print('Moving back to 0 with acceleration 5000...')
print('Should turn in the opposite direction no?')
stepper.set_acceleration(5000)
stepper.move_to(-1000, wait=True)


print('Disabling acceleration')
stepper.disable_acceleration()
stepper.set_max_speed(10000)


print('Moving to 20000 with default speed 1000')
stepper.move_to(-3000, wait=False)
time.sleep(1)
print('Increasing speed to 10000')
stepper.set_running_speed(10000)
stepper.wait_until_idle()


print('Moving back to 0')
print('Should turn in the opposite direction no?')
print('Speed should still be 10000 no?')
stepper.set_running_speed(10000)
stepper.move_to(-5000, True)

print('moving forward 3200 steps')
stepper.move(1600, True)
time.sleep(2)
print('and again')
stepper.move(1600, True)

print('homing')
stepper.home(True)
print('program complete')

answer = ''

while input is not 'y':
    stepper.get_switch_state()
    print(stepper.switch_state)
    answer = input("again?")