class SqlQueries:
    @staticmethod
    def createOrdersTable():
        return """
            CREATE TABLE IF NOT EXISTS `orders` (
                `User Id` INT,
                `Event Dt` DATE,
                `Revenue` FLOAT
            )
            """

    @staticmethod
    def createExtensionsTable():
        return """
            CREATE TABLE IF NOT EXISTS `extensions` (
                `User Id` INT,
                `Event Start` DATETIME,
                `Event End` DATETIME
            )
            """

    @staticmethod
    def createTestTable():
        return """
            CREATE TABLE IF NOT EXISTS `test` (
                `User Id` INT,
                `Event Dt` DATETIME,
                `num1` INT,
                `num2` INT
            )
            """
