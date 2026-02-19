import sys
import logging

def error_message_detail(error, error_detail: sys):
    # exc_info() humein batata hai ki error kahan aur kaise hua
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Sabhi details ko format ke andar hona chahiye
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # super() ke baad brackets () zaroori hain
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

            