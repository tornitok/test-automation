from pytest import mark
import allure

@allure.title('Сценарий успешной проверки логина')
@allure.severity(allure.severity_level.CRITICAL)
def test_success_log_in(index_page):
    index_page.enter_user_name()
    index_page.enter_password()
    index_page.click_button()
    index_page.is_url_valid()

INVALID_LOG_IN_SCENARIOUS=[
    ('test@ts.ts', '123456', 'Password or username is incorrect'),
    ('', '123456', 'Username field cannot be empty'),
    ('test@ts.ts', '', 'Password field cannot be empty'),
    ('', '', 'Username and password fields cannot be empty'),
]
@mark.parametrize(
    'user_name, password, error_message',
    INVALID_LOG_IN_SCENARIOUS,
    ids=[
        'invalid_credentials',
        'empty_user_name',
        'empty_password',
        'empty_fields'
    ]
)
def test_invalid_log_in(
        index_page,
        user_name,
        password,
        error_message
):
    index_page.enter_user_name('test@ts.ts')
    index_page.enter_password('123456')
    index_page.click_button()
    index_page.is_error_message_correct('Password or username is incorrect')