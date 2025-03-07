class HeaderURL:
    __instance = None
    def __init__(self):
        self.url = 'https://www.google.com'
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


header1 = HeaderURL()
header2 = HeaderURL()

header1.url='https://www.appstone.com'

print(header1.url)
print(header2.url)
