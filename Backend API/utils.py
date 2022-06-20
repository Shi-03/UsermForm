def email_pattern():
    email_pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    return email_pattern

def mobile_pattern():
    #mobile_pattern = '(?:\+?\(?\d{2,3}?\)?\D?)?\d{4}\D?\d{4}'
    mobile_pattern = '[7-9][0-9]{9}'
    return mobile_pattern

def name_pattern():
    name_pattern = '^[A-Z][-a-zA-Z]+$'
    return name_pattern