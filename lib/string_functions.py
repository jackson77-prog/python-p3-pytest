def return_string():
    return ''

def interpolate_string(s):
    return f'Hello, {s}!'
def test_interpolate_string():
    '''Test for interpolate_string function.'''
    result = interpolate_string('World')
    assert result == 'Hello, World!'
