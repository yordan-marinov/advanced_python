class EmailValidatorError(BaseException):
    pass


class NameTooShortError(EmailValidatorError):
    def __init__(self, massage="Name must be more than 4 characters"):
        self.massage = massage
        super().__init__(massage)


class MustContainAtSymbolError(EmailValidatorError):
    def __init__(self, massage="Email must contain @"):
        self.massage = massage
        super().__init__(massage)


class InvalidDomainError(EmailValidatorError):
    def __init__(self, massage="Domain must be one of the following: .com, .bg, .org, .net"):
        self.massage = massage
        super().__init__(massage)
