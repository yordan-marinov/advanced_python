class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length: int = min_length
        self.mails: list = mails
        self.domains: list = domains

    def __validate_name(self, name: str) -> bool:
        return len(name) >= self.min_length

    def __validate_mails(self, mail: str) -> bool:
        return mail in self.mails

    def __validate_domain(self, domain: str) -> bool:
        return domain in self.domains

    def validate(self, email):
        name, mail_domain = email.split("@")
        mail, domain = mail_domain.split(".")
        return self.__validate_name(name) and self.__validate_mails(mail) and self.__validate_domain(domain)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
