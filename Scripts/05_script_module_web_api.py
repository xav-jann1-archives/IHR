#!/usr/bin/env python
# -*- coding: utf-8 -*-

# run with python 03_...py --qi-url="tcp://ip_robot:9559"

import qi
import requests

class WeatherModule:
    """
    Wow, there should be some doc here too
    """
    def __init__(self, session):
        """
        """
        print "MyModule init"
        self.session = session
        self.memory = self.session.service("ALMemory")

        self.url = "http://api.openweathermap.org/data/2.5/weather?id=6454573&APPID=49b584e311c58fa09794e5e25a19d1af&UNITS=metric"


    def __del__(self):
        """
        """
        pass


    def print_weather(self):
        """
        """
        info = requests.get(self.url)

        info_json = info.json()
        print "info_json: %s" % info_json

    def get_temperature(self):
        """
        TODO

        **return (float) :**
           * temperature (in degrees)
        """
        info = requests.get(self.url)

        info_json = info.json()
        main_info = info_json["main"]
        print "main_info: %s" % main_info

        temperature_kelvins = main_info["temp"]
        temperature_degrees = temperature_kelvins - 273.15

        print "temperature: % s" % temperature_degrees
        return temperature_degrees




def main():
    """
    I should put some doc here
    """

    app = qi.Application(url="tcp://192.168.1.201:9559")
    app.start()

    s = app.session
    my_module = WeatherModule(s)
    s.registerService("Weather", my_module)

    app.run()



if __name__ == "__main__":
    main()
