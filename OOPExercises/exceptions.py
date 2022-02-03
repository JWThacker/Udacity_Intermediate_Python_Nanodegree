INVALID_PASSWORDS = (
    'password',
    'abc123',
    '123abc',
)

class InvalidPasswordError(KeyError):
    pass

def validate_password(username, password):
    if password == username:
        raise InvalidPasswordError("Password cannot be the same as username.")
    if password in INVALID_PASSWORDS:
        raise InvalidPasswordError("Password cannot one of the common passwords.")


def create_account(username, password):
    return (username, password)


def main(username, password):
    try:
        valid = validate_password(username, password)
    except InvalidPasswordError as err:
        print(err)
    else:
        account = create_account(username, password)
    finally:
        print("Validated password against username and collection.")



if __name__ == '__main__':
    main('jim', 'jam')
    main('admin', 'password')  # Oh no!
    main('guest', 'guest')  # Oh no!
