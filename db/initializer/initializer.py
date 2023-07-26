from sql_queries import SqlQueries
from db.pipeline import DatabasePipeline


if __name__ == "__main__":
    pipeline = DatabasePipeline()
    pipeline.addOperation(SqlQueries.createTestTable())
    pipeline.addOperation(SqlQueries.createOrdersTable())
    pipeline.addOperation(SqlQueries.createExtensionsTable())
    pipeline.run()
