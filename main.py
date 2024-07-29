from src.cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = 'STAGE 01: DATA INGESTION'

if __name__ == "__main__":
    try:
        logger.info(f'>>>>>>stage {STAGE_NAME} started <<<<<<<<<<')
        obj = DataIngestionPipeline()
        obj.main()

        logger.info(f'>>>>>>stage {STAGE_NAME} coomleted <<<<<<<<<<')

    except Exception as e:
        raise e

