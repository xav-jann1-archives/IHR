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
        self.memory = self.session.service("ALMemory")

        self.watch_head_subscriber = None
        self.watch_head_id = None


    def __del__(self):
        """
        """
        self.stop_watch_head_touch()


    def say_something(self, something):
        """
        """
        print "MyModule.say_something"
        self.tts.say(something)


    def start_watch_head_touch(self):
        """
        """
        if self.watch_head_subscriber is None:
            self.watch_head_subscriber = self.memory.subscriber("FrontTactilTouched")
            self.watch_head_id = self.watch_head_subscriber.signal.connect(self._watch_head_callback)

    def stop_watch_head_touch(self):
        """
        """
        try:
            if self.watch_head_subscriber is not None:
                self.watch_head_subscriber.signal.disconnect(self.watch_head_id)
        except Exception as e:
            print "Exception in stop_watch_subscriber: %s" % e


    def _watch_head_callback(self, value):
        """
        """
        if value == 1:
            self.say_something("On a touché ma tête")


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
