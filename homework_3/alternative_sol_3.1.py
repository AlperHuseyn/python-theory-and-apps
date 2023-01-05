""" Alternative solution using assert to check if the inputs are valid """


def puts(text, **kwargs):
    valid_kwargs = {'reverse': False, 'repeat': 1, 'center': 0, 'fill_char': ' '}

    # Check if the given kwargs are valid
    for key, value in kwargs.items():
        if key not in valid_kwargs:
            print(f'Invalid argument: {key}={kwargs[key]}')
            return

    # Use assert to check for valid input
    assert isinstance(valid_kwargs['repeat'], int), f'Error, repeat takes only integers. ' \
                                                    f'It is given: {valid_kwargs["repeat"]}'

    assert isinstance(valid_kwargs['center'], int), f'Error, center takes only integers. ' \
                                                    f'It is given: {valid_kwargs["center"]}'

    assert (isinstance(valid_kwargs['fill_char'], str) and len(valid_kwargs['fill_char']) == 1), \
        f'Error, fill_char takes only str. It is given: {valid_kwargs["fill_char"]}'

    # Update valid_kwargs with the given kwargs
    valid_kwargs.update(kwargs)

    # Reverse the text if specified
    if valid_kwargs['reverse']:
        text = text[::-1]

    # Repeat the text if specified
    text *= valid_kwargs['repeat']

    # Check if fill_char used without center
    if 'fill_char' in valid_kwargs and valid_kwargs['center'] == 0:
        print('Error, fill_char can only be used with center')
        return

    # Center the text if specified
    if len(text) < valid_kwargs['center']:
        spaces = valid_kwargs['center'] - len(text)
        split_spaces = spaces // 2 + (spaces % 2)
        text = valid_kwargs['fill_char'] * split_spaces + text + valid_kwargs['fill_char'] * (spaces - split_spaces)

    print(text)


puts('Alper', reverse=False, repeat=2, fill_char=' ')
