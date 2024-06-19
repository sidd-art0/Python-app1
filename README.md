#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)  # instance of flyt droneigation class

time.sleep(3)

print '1. taking off till height of 5m'
drone.take_off(5.0)
print 'Current position - Point A of square ABCD'

print ' move in a square trajectory of side length 6.5m at a height of 5m'

print ' 2. moving to Point B of square ABCD'
drone.position_set(6.5, 0, 0, yaw=1.0472, relative=True)

print ' 2. moving to Point C of square ABCD'
drone.position_set(0, 6.5, 0, relative=True)

print ' 2. moving back to Point D of square ABCD'
drone.position_set(-6.5, 0, 0, relative=True)

print ' 2. moving back to Point D of square ABCD'
drone.position_set(0, -6.5, 0, relative=True)

print '     6. Landing'
drone.land(async=False)

# shutdown the instance
drone.disconnect()
