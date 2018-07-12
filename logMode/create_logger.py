import logging,os


class user_logger():
    def __init__(self):
        self.path = os.path.abspath('.')

    def __repr__(self):
        return 'Modelog'

    def __call__(self, *args, **kwargs):
        log = logging.getLogger('msgForlog')
        log.setLevel(logging.INFO)

        loggerhand = logging.FileHandler(self.path+'/logMode/msgForlog.log')
        loggerhand.setLevel(logging.INFO)

        loggerFormater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        loggerhand.setFormatter(loggerFormater)

        loggerstr = logging.StreamHandler()

        log.addHandler(loggerhand)
        log.addHandler(loggerstr)



