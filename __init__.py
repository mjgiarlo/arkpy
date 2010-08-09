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
    
    # first generate a name based on given template
    name = _generate_name(template)

    # then prepend the optional prefix (for additional namespacing)
    name = prefix + name

    # then prepend authority.number and the '/' character e.g., "11111/id"
    ark = "%s/%s" % (authority, name)

    # then generate a check character, if specified in template
    if template[-1] == 'k':
        ark += _generate_check(ark)

    # return identifier w/ check char to caller
    return ark

def _generate_name(template):
      name = ''
      for char in list(template):
          if char not in ['d', 'e']:
              continue
          digit_array = xdigits if char == 'e' else digits
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
