def cls():
    import platform
    import os
    if platform.system == 'Darwin':
        os.system('clear')
    elif platform.system == 'Windows':
        os.system('cls')
    elif platform.system == 'Linux':
        os.system('clear')