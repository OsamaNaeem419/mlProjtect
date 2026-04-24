import sys
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion


if __name__ == "__main__":
    logging.info("Pipeline started")

    try:
        ingestion = DataIngestion()
        train_path, test_path = ingestion.initiate_data_ingestion()

        print("Train file:", train_path)
        print("Test file:", test_path)

        logging.info("Pipeline completed successfully")

    except Exception as e:
        logging.error("Pipeline failed")
        raise CustomException(e, sys)