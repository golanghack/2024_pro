#! /usr/bin/env python3 

LANGS = {'Russian': 'Привет, ', 'French': 'Bonjour, ', 'Germany': 'Hallo, ', 'Spanish':'Hola, '}
DEFAULT = 'Hello, '

def get_prefix(prefix):
    try:
        lang = LANGS[prefix]
        return lang 
    except KeyError:
        return DEFAULT
    
    
def hello(name: str, prefix: str) -> str:
    if name == '':
        return get_prefix(prefix) + 'World'
    return get_prefix(prefix) + name

def main():
    prefix = get_prefix('')
    message = hello('', prefix)
    print(message)
    

if __name__ == '__main__':
    main()
    
        
