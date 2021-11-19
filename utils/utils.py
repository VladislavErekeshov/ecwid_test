import configparser


class Utils:
    __config = configparser.ConfigParser()

    def config_data(self, head, attribute):
        self.__config.read('resources/config.ini')
        return self.__config[head][attribute]

    def test_data(self, head, attribute):
        self.__config.read('resources/test_data.ini')
        return self.__config[head][attribute]


