import configparser
import socket

class ConfigDict(dict):

    def __init__(self):
        config_parser = configparser.ConfigParser()
        config_parser.read("local_config.ini")
        self.server_ip = config_parser["LOCAL_SERVER"]["host"]
        self.server_port = config_parser["LOCAL_SERVER"]["port"]

class Client:

    def _global_config(self):
        cfg = ConfigDict()
        return cfg

    def __init__(self):
        self.config = self._global_config()
        self.server_conf = (self.config.server_ip, int(self.config.server_port))

        # A socket object is created using socket.socket(), specifying AF_INET for IPv4 and SOCK_STREAM for TCP communication.
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.client.connect(self.server_conf)
        print('Connection succesful made to the server')


if __name__ == '__main__':
    client1 = Client()
