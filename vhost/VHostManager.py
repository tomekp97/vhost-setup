import sys
from vhost.VHostCreate import VHostCreate
from vhost.system_support import os_is_supported, server_is_supported

class VHostManager:
    def __init__(self, arguments, working_directory):
        self.arguments = arguments
        self.creator = VHostCreate(arguments, working_directory)
    
    def init(self):

        if os_is_supported() and server_is_supported():
            if self.arguments.disable:
                print("Will disable the VHOST.")
            else:
                print("Setting up...")
                self.creator.init()
        else:
            sys.exit()

    def enable():
        pass