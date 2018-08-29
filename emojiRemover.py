def removeEmojis(arg):
    return (str((arg).encode('utf-8', 'ignore')))[1:]



print(removeEmojis('DANK'))