def tags(tag):
    def decoder(func):
        def wrapper(*variables):
            result = f'<{tag}>{func(*variables)}</{tag}>'
            return result

        return wrapper

    return decoder

