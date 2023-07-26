class BaseFileReader:
    def __init__(self, file):
        self._file = file
        self._data = self.__readFile()

    def __readFile(self):
        ...

    def clearData(self):
        ...

    def writeToDatabase(self, table):
        ...

    @property
    def data(self):
        return self._data