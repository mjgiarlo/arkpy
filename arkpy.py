import random


digits = [str(i) for i in range(0, 10)]
xdigits = digits + ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'm', 'n',
                    'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

def mint(authority, template, prefix=''):
    """ mint an ARK within an authority according to a template
    """
    # Penn State's ARK authority number is 42409

    # random template: eeddeeddk
    #   e is an xdigit: 0123456789bcdfghjkmnpqrstvwxz
    #   d is a digit:   0123456789
    #   k is checkchar: special xdigit

    # initialize an array to hold the various parts of an ARK
    # to be joined later
    ark_parts = []

    if authority:
        ark_parts.append(authority)
        ark_parts.append('/')

    if prefix:
        ark_parts.append(prefix)
    
    # generate a name based on given template
    ark_parts.append(_generate_name(template))

    # join the ARK from its parts
    ark = ''.join(ark_parts)

    # generate a check character, if specified in template
    if template[-1] == 'k':
        ark += _generate_check(ark)

    # return identifier
    return ark

def _generate_name(template):
    name = ''
    for char in list(template):
        if char == 'e':
            digit_array = xdigits 
        elif char == 'd': 
            digit_array = digits
        else:
            continue
        name += random.choice(digit_array)
    return name

def _generate_check(ark):
    sum = 0
    position = 0
    for char in list(ark):
        try:
            ordinal = xdigits.index(char)
        except ValueError:
            ordinal = 0
        position += 1
        sum += (ordinal * position)
    return xdigits[sum % len(xdigits)]

def validate(ark):
    return _generate_check(ark[:-1]) == ark[-1]
