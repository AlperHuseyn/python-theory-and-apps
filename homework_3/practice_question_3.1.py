""" My approach to practice question #3.1 """


def puts(text, **kwargs):
    """
    Prints text with various formatting options.

    Keyword arguments:
        reverse -- bool, whether to reverse the text or not (default False)
        repeat -- int, number of times to repeat the text (default 1)
        center -- int, number of characters to center the text in (default 0)
        fill_char -- char, character to use for filling (default ' ')
    """
    valid_kwargs = {'reverse': False, 'repeat': 1, 'center': 0, 'fill_char': ' '}

    # Check if the given kwargs are valid
    for key, value in kwargs.items():
        if key not in valid_kwargs:
            print(f'Invalid argument: {key}={kwargs[key]}')
            return
        else:
            valid_kwargs[key] = value

    # Reverse the text is specified
    if valid_kwargs['reverse']:
        text = text[::-1]

    # Checks whether the value for repeat valid or not
    if not isinstance(valid_kwargs['repeat'], int):
        print(f'Error, repeat takes only integers. It is given: {valid_kwargs["repeat"]}')
        return
    else:
        text *= valid_kwargs['repeat']

    # Check if fill_char is specified without center
    if 'fill_char' in valid_kwargs and valid_kwargs['center'] == 0:
        print('Error, fill_char can only be used with center')
        return

    # Center the text in the specified area
    if not isinstance(valid_kwargs["center"], int):
        print(f'Error, center takes only integers. It is given: {valid_kwargs["center"]}')
        return
    else:
        spaces = valid_kwargs['center'] - len(text)
        split_spaces = spaces // 2 + (spaces % 2)

        if valid_kwargs['center']:
            # Checks if fill_char valid
            if (not isinstance(valid_kwargs['fill_char'], str)) or len(valid_kwargs['fill_char']) != 1:
                print(f'Error, fill_char must be one-char str. It is given: {valid_kwargs["fill_char"]}')
                return
            else:
                text = valid_kwargs['fill_char'] * split_spaces + text + valid_kwargs['fill_char'] * \
                       (spaces - split_spaces)
        else:
            if len(text) < valid_kwargs['center']:
                text = ' ' * split_spaces + text + ' ' * (spaces - split_spaces)

    print(text)


puts('Alper', reverse=False, repeat=2, fill_char=' ')
