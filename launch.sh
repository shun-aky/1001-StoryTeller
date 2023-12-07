#! /bin/sh

sudo pigpiod
. myenv/bin/activate
python3 driver.py
deactivate
