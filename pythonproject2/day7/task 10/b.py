from logger import logger

def do_another_thing():
    print(f"[Module B] Current log level: {logger.get_level()}")