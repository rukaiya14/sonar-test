def greet_user(name):
    print("Hello " + name)

def insecure_function(password):
    print("Password is: " + password)  # Vulnerable: exposing secret

greet_user("Rukaiya")
insecure_function("12345")
