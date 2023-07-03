import sys 
import logging

def error_message_detail(error, error_detail:sys):
    _,_,exe_tb=error_detail.exc_info()
    file_name=exe_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number[{1}] error message[{2}]".format(file_name,exe_tb.tb_lineno,str(error))
    
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

'''
we are overriding the init method.. learn more abt it. 
error_detail which is being passed to function comes from sys library.
First parent exception is inherited, the error message which comes from fucntion comes to error_message var- the class variable.
This code is common we do this in except block every else. 

'''

    