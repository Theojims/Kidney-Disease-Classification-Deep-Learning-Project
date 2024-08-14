from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation_mflow import Evaluation
from cnnClassifier import logger

STAGE_NAME = "04: ModelEvaluation"

class ModelEvaluationPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_eval_config = config.get_model_evaluation_config()
        evaluation = Evaluation(model_eval_config)
        evaluation.evaluation()
        #evaluation.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
