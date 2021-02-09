import exceptions

MINIMUM_NAME_LENGTH = 4
VALID_DOMAINS = ("com", "bg", "net", "org")
AT_SYMBOL = "@"


def validate_email(
        email,
        length=MINIMUM_NAME_LENGTH,
        domains=VALID_DOMAINS,
        at_symbol=AT_SYMBOL
):
    def validate_length():
        name, mail = email.split("@")
        if len(name) <= length:
            raise exceptions.NameTooShortError

    def validate_domain():
        domain = email.split(".").pop()
        if domain not in domains:
            raise exceptions.InvalidDomainError

    def validate_at_symbol():
        if at_symbol not in email:
            raise exceptions.MustContainAtSymbolError

    if not any([validate_at_symbol(), validate_length(), validate_domain()]):
        return "Email is valid"


def get_emails():
    while True:
        email = input()
        if email == "End":
            break

        print(validate_email(email))


get_emails()
