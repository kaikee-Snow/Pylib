import traceback
import sys
try:
    raise ValueError('this is a exp')
except Exception as ex:
    # print(sys.exc_info())
    ex_type, ex_val, ex_stack = sys.exc_info()
    print(ex_type, ex_val)
    for stack in traceback.extract_tb(ex_stack):
        print(stack)
