from basic import logger


def is_alive():
    logger.info("Calling Keep Alive")
    return "is alive", 200
