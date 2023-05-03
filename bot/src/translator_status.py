#sealed classないのくそ
class TranslatorStatus:
    def __init__(self,message) -> None:
        self.message = message
    def status(self):
        pass

class Error(TranslatorStatus):
    def __init__(self,message) -> None:
        super().__init__(message)
    def status(self):
        return self.message

class Success(TranslatorStatus):
    def __init__(self,message) -> None:
        super().__init__(message)
    def status(self):
        return self.message