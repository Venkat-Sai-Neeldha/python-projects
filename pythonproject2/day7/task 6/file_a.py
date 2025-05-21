from file_b import func_b

def func_a():
    print("Function A")
    func_b()


# changed code after importing from common place
from common import shared_logic

def func_a():
    print("Function A")
    shared_logic()