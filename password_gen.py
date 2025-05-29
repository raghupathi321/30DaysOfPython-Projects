import random
def generate_password(length):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    symbols = '!@#$%^&*()-_=+[]{}|;:,.<>?/'
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    password += [random.choice(lowercase + uppercase + digits + symbols) for _ in range(length - 4)]
    return ''.join(password)
print("Generated Password:", generate_password(12))
