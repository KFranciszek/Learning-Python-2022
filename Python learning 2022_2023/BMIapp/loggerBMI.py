# Usługa do zapisywania logów działania oraz błędów do pliku. 

#logowanie wywołania usługi dicBMI
import logging
import dicBMI
from dicBMI  import BMI_data

def loggingDEBUG():

    formatLogging = '[%(asctime).20s] [%(levelname)s] %(message)s'

    logging.basicConfig(filename='D:\Python\Projekt\python1.log',
                        level=logging.DEBUG,
                        format=formatLogging)
    logger = logging.getLogger()
    logger.info(dicBMI)
    logger.info(BMI_data)

def loggingERROR ():
    formatLogging = '[%(asctime).20s] [%(levelname)s] %(message)s'
    logging.basicConfig(filename='D:\Python\Projekt\pythonERROR.log',
                        level=logging.ERROR,
                        format=formatLogging)
    logger = logging.getLogger()
    logger.error(dicBMI)
    logger.error(BMI_data)

loggingERROR()
loggingDEBUG()
