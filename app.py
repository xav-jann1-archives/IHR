# -*- encoding: UTF-8 -*-

import sys
import time
import qi

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser

# Adresse IP du Pepper utilisé:
PEPPER_IP = "pepper2.local"

# Global variable to store the HumanGreeter module instance
HumanGreeter = None


class HumanGreeterModule(ALModule):

    def __init__(self, name):
        ALModule.__init__(self, name)
        # No need for IP and port here because
        # we have our Python broker connected to NAOqi broker

        self.t1, self.t2 = time.time()-10, time.time()
        
        # Create a proxy to ALTextToSpeech for later use
        self.tts = ALProxy("ALTextToSpeech")
        
        """ 
            Connection        
        """
        session = qi.Session()
        try:
            session.connect("tcp://{}:{}".format(PEPPER_IP, 9559))
        except RuntimeError:
            print ("\nCan't connect to Naoqi at IP {} (port {}).\nPlease check your script's arguments."
               " Run with -h option for help.\n".format(PEPPER_IP, 9559))
            sys.exit(1)
        
        """
            Face Detection
        """
        faceDetection = session.service("ALFaceDetection")
        faceDetection.enableTracking(True)
        
        # Subscribe to the FaceDetected event:
        self.memory = ALProxy("ALMemory")
        self.memory.subscribeToEvent("FaceDetected", "HumanGreeter", "onFaceDetected")
        self.memory.subscribeToEvent("ALBasicAwareness/HumanLost", "HumanGreeter", "HumanLost")
        
        """
            QiChat
        """        
        """
        self.ALDialog = session.service("ALDialog")
        self.ALDialog.setLanguage("French")
        
        # Désactive les topics en cours d'utilisation:
        self.unloadAllTopics();

        # Chargement du topic:
        self.topic = self.ALDialog.loadTopic("/home/nao/Projet/dial.top")
        self.ALDialog.subscribe("dial")
        
        # activate dialog
        self.ALDialog.activateTopic(self.topic)
        """
    
    # Fonction déclenchée lorsqu'il n'y a plus personne autour de Pepper:
    def HumanLost(self, *_args):
        # Désactive l'évènement:
        self.memory.unsubscribeToEvent("ALBasicAwareness/HumanLost","HumanGreeter")
        
        # Enregistre l'heure lorsque la personne est parti:
        self.t1 = time.time()
        
        # Déclenche un évènement pour le qiChat:
        self.memory.raiseEvent("ManagementEvent", "pause")
        
        # Ré-active les événements:        
        self.memory.subscribeToEvent("FaceDetected", "HumanGreeter", "onFaceDetected")
        self.memory.subscribeToEvent("ALBasicAwareness/HumanLost", "HumanGreeter", "HumanLost")
    
    # Lorsqu'une personne se présente devant Pepper:
    def onFaceDetected(self, *_args):
        # Désactive l'évènement:
        self.memory.unsubscribeToEvent("FaceDetected","HumanGreeter")
        
        # Réaction de Pepper:
        self.tts.say("Oh")
        
        # Calcul le temps depuis qu'une personne était perdue:
        self.t2 = time.time()
        
        # Si c'est une nouvelle personne:
        if self.t2 - self.t1 > 10:
            # self.tts.say("restart")
            self.memory.raiseEvent("ManagementEvent", "restart")
        
        # Si c'est la même personne:
        else:
            # self.tts.say("resume")
            self.memory.raiseEvent("ManagementEvent", "resume")
            #self.tts.say("Rebonjour ! J'attends toujours votre réponse.")        
    
    """
    # Enlève tous les Topics utilisés par Pepper:
    def unloadAllTopics(self):
        for dT in self.ALDialog.getLoadedTopics('French'):
            try:
                self.ALDialog.unloadTopic(dT)
            except Exception as e:
                print "Could not unload", dT
                print e
    """ 



def main():
    """ Main entry point

    """

    global HumanGreeter
    HumanGreeter = HumanGreeterModule("HumanGreeter")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        sys.exit(0)



if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--pip",
        help="Parent broker port. The IP address or your robot",
        dest="pip")
    parser.add_option("--pport",
        help="Parent broker port. The port NAOqi is listening to",
        dest="pport",
        type="int")
    parser.set_defaults(
        pip=PEPPER_IP,
        pport=9559)

    (opts, args_) = parser.parse_args()
    pip   = opts.pip
    pport = opts.pport

    # We need this broker to be able to construct
    # NAOqi modules and subscribe to other modules
    # The broker must stay alive until the program exists
    myBroker = ALBroker("myBroker",
       "0.0.0.0",   # listen to anyone
       0,           # find a free port and use it
       pip,         # parent broker IP
       pport)       # parent broker port
       
    main()
