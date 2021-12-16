from robot.api.deco import keyword


class UserName(object):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def without_decorator(self):
        pass

    @keyword("Ползовательское имя для кейворда")
    def with_simple_decorator(self):
        pass

    @keyword("Кейворд с аргументом {string}")
    def with_arg_and_placeholder(self, string):
        pass

    @keyword("Печальный кейворд")
    def failed_with_simple_decorator(self):
        assert False
