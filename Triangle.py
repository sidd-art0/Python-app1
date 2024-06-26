#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)  

time.sleep(3)

print ('0. taking off till 10m')
drone.take_off(10.0)
print ('taking down 10 m')

print (' move in a triangular trajectory of side length 10m at a height of 10m')

print (' 1. moving from Point A to B of triangle ABC')
drone.position_set(8.0, 6.0, 10, relative=True)

print (' 2. moving from Point B to C of triangle ABC')
drone.position_set(-8.0, 6.0, 0, relative=True)

print (' 3. moving back to home position  from Point C to A of triangle ABC')
drone.position_set(0, -10, 0, relative=True)

print (' 4. Landing')
drone.land(async=False)

drone.disconnect()
