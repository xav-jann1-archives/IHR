#!/usr/bin/env python
# -*- coding: utf-8 -*-

import qi

robot_ip = "192.168.1.201"

def main():
    """
    I should put some doc here
    """
    robot_session = qi.Session()
    robot_session.connect(robot_ip)

    tts = robot_session.service("ALTextToSpeech")
    motion = robot_session.service("ALMotion")
    animated_speech = robot_session.service("ALAnimatedSpeech")


    motion.wakeUp()

    tts.say("Coucou mais je ne bouge pas. blablablablabla")

    animated_speech.say("Coucou, et ici je bouge en plus!. Blablablablabla")

    motion.rest()




if __name__ == "__main__":
    main()
