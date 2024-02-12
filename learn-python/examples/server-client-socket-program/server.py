import configparser
import functools
import threading
import socket
import time

class ConfigDict(dict):

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("local_config.ini")
        self.host = config["LOCAL_SERVER"]["host"]
        self.port = config["LOCAL_SERVER"]["port"]


class lazy_attribute:

    def __init__(self, func):
        # Replace the values of self's special variables with the values of func's special variables
        # So, self.__name__ would have the same value of func.__name__
        # This will help to set class attribute later in the __get__ function
        functools.update_wrapper(self, func, updated=[])
        self.getter = func
    
    def __get__(self, obj, cls):
        values = self.getter()
        setattr(cls, self.__name__, values)
        return values

class Server:

    @lazy_attribute
    def _global_config():
        cfg = ConfigDict()
        return cfg

    def __init__(self):
        
        # _global_config is an attribute here.
        # Do not write `self._global_config()` because then it would be something like `ConfigDict()()` which means `{}()``
        config = self._global_config
        self.host = config.host
        self.port = config.port
        self.server_conf = (self.host, int(self.port))

        # A socket object is created using socket.socket(), specifying AF_INET for IPv4 and SOCK_STREAM for TCP communication.
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # The server binds itself to the specified address using bind() 
        self.server.bind(self.server_conf)

        # starts listening for connections with listen()
        self.server.listen(5)

        # Uses accept() to wait for a client connection and stores the client's socket and address in self.clientsocket and self.addr, respectively.
        self.client_socket, self.client_addr = self.server.accept()
        print("Got connection from {}".format(self.client_addr))
        
    
if __name__ == '__main__':
    server1 = Server()

