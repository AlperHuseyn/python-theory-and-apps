""" Instructor solution for practice question #3.1 """


def puts(text, **kwargs):
    valid = True
    for key in kwargs:
        if key not in ('reverse', 'repeat', 'center', 'fillchar'):
            print('Invalid argument: {}'.format(key))
            valid = False

    if not valid:
        return

    if 'fillchar' in kwargs and 'center' not in kwargs:
        print('"filchar" must be use with "center" parameter')
        return

    reverse = kwargs.get('reverse', False)
    repeat = kwargs.get('repeat', 1)
    center = kwargs.get('center', 0)
    fillchar = kwargs.get('fillchar', ' ')

    rs_text = text[::-1] if reverse else text
    rs_text = rs_text * repeat
    rs_text = rs_text.center(center, fillchar)

    print(rs_text)


puts('ankara', reverse=False, repeat=3, center=50, fillchar='x')