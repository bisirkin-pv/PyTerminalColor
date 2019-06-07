import json


class PyTerminalColor:
    """
    Coloring text in the terminal
    v1.0
    """
    def __init__(self, config):
        with open(config) as json_file:
            self.data = json.load(json_file)

    def colorize(self, text, foreground='', background='', style=''):
        """
        Color the text by the passed parameters.
        :param text: input text
        :param foreground:
        :param background:
        :param style:
        :return: colored text
        """
        return "{}{}{}{}{}".format(
            self.__get('foregroundColors', foreground),
            self.__get('backgroundColors', background),
            self.__get('textStyles', style),
            text,
            self.__get('reset', 'default'),
        )

    def __get(self, block, key):
        return self.data[block].get(key, '')


if __name__ == '__main__':
    pyTerminalColor = PyTerminalColor('config.json')
    print(pyTerminalColor.colorize('Text', "yellow", "lightGray", "underline"))
