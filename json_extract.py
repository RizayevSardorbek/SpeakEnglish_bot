def jsonExtract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(a, b, c):
        """Recursively search for values of key in JSON tree."""
        if isinstance(a, dict):
            for k, v in a.items():
                if isinstance(v, (dict, list)):
                    extract(v, b, c)
                elif k == c:
                    b.append(v)
        elif isinstance(a, list):
            for item in a:
                extract(item, b, c)
        return b

    values = extract(obj, arr, key)
    return values
