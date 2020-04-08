from browser import website
from constants import *
import os

if __name__ == '__main__':
    procap = website()
    procap.login()
    procap.get_call()
