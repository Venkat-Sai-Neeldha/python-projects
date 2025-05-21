from a import do_something
from b import do_another_thing
from logger import logger

print(f"[Main] Initial log level: {logger.get_level()}")

do_something()
do_another_thing()

print(f"[Main] Final log level: {logger.get_level()}")