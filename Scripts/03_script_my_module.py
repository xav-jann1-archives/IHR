#!/usr/bin/env python
# -*- coding: utf-8 -*-

# run with python 03_...py --qi-url="tcp://ip_robot:9559"

import qi

class MyModule:
    """
    Wow, there should be some doc here too
    """
    def __init__(self, session):
        """
        """
        print "MyModule init"
        self.session = session
        self.tts = self.session.service("ALTextToSpeech")

    def say_something(self, something):
        """
        """
        print "MyModule.say_something"
        self.tts.say(something)




def main():
    """
    I should put some doc here
    """

    app = qi.Application(url="tcp://192.168.1.201:9559")
    app.start()

    s = app.session
    my_module = MyModule(s)
    s.registerService("MyModule", my_module)

    app.run()



if __name__ == "__main__":
    main()
