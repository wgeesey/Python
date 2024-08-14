from name_function import get_formatted_name


def test_first_last_name():
    """Do names like 'Johnny Appleseed' work?"""
    formatted_name = get_formatted_name('johnny', 'appleseed')
    assert formatted_name == 'Johnny Appleseed'


def test_first_last_middle_name():
    """Do names like 'Alpha Bravo Charlie' work?"""
    formatted_name = get_formatted_name(
        'alpha', 'charlie', 'bravo')
    assert formatted_name == 'Alpha Bravo Charlie'
