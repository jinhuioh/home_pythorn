# import argparse
# import sys
# from tkinter import messagebox
# import requests
#
# #kakao연결 + 신청해놨던 키.
# API_URL = 'https://dapi.kakao.com/v2/vision/multitag/generate'
# MAPPER_KEY = 'a4ea34842d567247008295eb355add44'

class Car:
    def __init__(self,w):
        self.wheels = w

    def getWheels(self):
        return self.wheels

if __name__ == '__main__':
    c = Car(4)
    n = c.getWheels()
    print(c)