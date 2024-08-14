import os
import sys
import logging



logging_str = '[%(asctime)s: %(levelname)s: %(module)s: %(message)s]'

log_filename = "logs"
log_filedir ="Log_record"
log_filename_path = os.path.join(log_filedir,log_filename)

os.makedirs(os.path.dirname(log_filename_path), exist_ok =True)


logging.basicConfig(

    level = logging.INFO,
    format = logging_str,
    force=True,

    handlers = [
        logging.FileHandler(log_filename_path),
        logging.StreamHandler(sys.stdout)
    ]

)

logger = logging.getLogger("cnnClassifierLogger")

