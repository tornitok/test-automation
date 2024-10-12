from support.error_messages import AssertionErrors

class Assertions:
    @staticmethod
    def assert_equal(expected, actual):
        assert expected == actual, AssertionErrors.URL_NOT_FOUND.format(expected, actual)
