from pytest import mark

SCENARIOS=[
    (10, 'Valid'),
    (50, 'Valid'),
    (9, 'Not in range'),
    (60, 'Not in range'),
    (-1, 'Negative integer'),
    ('String', 'Not a number'),
    (10.1 ,'Not an integer')

]


@mark.parametrize(
    'value, message',
    SCENARIOS,
    ids=[
        'boundary_min_valid_value',
        'boundary_max_valid_value',
        'below_min_value',
        'above_max_value',
        'negative_value',
        'string_value',
        'float_value'
    ]
)
def test_validator(
        check_and_validate_page,
        value,
        message
):
    check_and_validate_page.enter_number(value)
    check_and_validate_page.is_message_correct(message)
