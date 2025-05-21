from logger import logger

def do_something():
    print(f"[Module A] Current log level: {logger.get_level()}")
    logger.set_level("DEBUG")