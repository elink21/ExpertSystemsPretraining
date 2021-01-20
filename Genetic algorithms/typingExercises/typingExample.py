

def ceasar(text: str, key: int) -> str:
    return "".join([chr(ord(c)+key) for c in text])


print(ceasar("CDE",1))
