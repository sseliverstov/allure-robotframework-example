from robot.api.deco import keyword

from robot.running.context import EXECUTION_CONTEXTS
from robot.running.runkwregister import RUN_KW_REGISTER
from robot.api import logger
from ..manual_cases import ManualTestCases


class UserName(ManualTestCases):

    def __init__(self):
        super().__init__()

    def without_decorator(self):
        pass

    @keyword("Ползовательское имя для кейворда")
    def with_simple_decorator(self):
        pass

    @keyword("Кейворд с аргументом {string}")
    def with_arg_and_placeholder(self, string):
        pass

    @keyword("Печальный кейворд")
    def failed_with_simple_decorator(self, a):
        pass#assert False
