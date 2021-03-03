def to_camel_case(text: str):
    txt = text.replace('_', '-')
    lst = txt.split('-')
    for i in range(1, len(lst)):
        lst[i] = lst[i].capitalize()
    return ''.join(lst)
