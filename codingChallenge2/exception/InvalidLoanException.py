class InvalidLoanException(Exception):
    def __init__(self,str):
        super().__init__(str)
        