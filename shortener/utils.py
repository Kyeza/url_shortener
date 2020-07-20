def shortener_base62_encoder(id):
    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    short_url = ""

    # for each digit find the base 62
    while id > 0:
        short_url += string[id % 62]
        id //= 62

    return short_url
