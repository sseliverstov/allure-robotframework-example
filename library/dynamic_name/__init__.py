
class DynamicName(object):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def get_keyword_names(self):
        return ['my_keyword']

    def my_keyword(self):
        pass

