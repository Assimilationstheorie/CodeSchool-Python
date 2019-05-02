class Condestructor:
    def __init__(self):
        print('Constructor')

    def __del__(self):
        print('Destructor')

cd = Condestructor()
print('Hello World')

# Output:
# Constructor
# Hello World
# Destructor

# Destructor will be called at the end of the programm
