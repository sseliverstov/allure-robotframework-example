from robot.api.deco import keyword
from ..manual_cases import ManualTestCases


class UserTestLibrary(ManualTestCases):

    def without_decorator(self):
        pass

    @keyword("Простой кейворд")
    def with_simple_decorator(self):
        pass

    @keyword("Кейворд с аргументом {string}")
    def with_arg_and_placeholder(self, string):
        pass

    @keyword("Кейворд с ошибкой")
    def failed_with_simple_decorator(self):
        assert False
