from file_a import func_a

def func_b():
    print("Function B")
    func_a()

# # changed code after importing from common place
from common import shared_logic

def func_b():
    print("Function B")
    shared_logic()