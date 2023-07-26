import pandas as pd

from reader import BaseFileReader
from db.database import databaseSession


class CSVFileReader(BaseFileReader):
    def __init__(self, file):
        super().__init__(file)

    def __readFile(self):
        return pd.read_csv(self._file)

    def clearData(self):
        self._data = self._data.dropna()
        self._data = self._data.drop_duplicates()  # drop_duplicates(subset=["column"])

    def writeToDatabase(self, table):
        with databaseSession as db:
            self._data.to_sql(name=table, con=db.connection, if_exists="replace")

    @property
    def data(self):
        return self._data
