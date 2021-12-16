from robot.running.context import EXECUTION_CONTEXTS
from robot.api import logger


class ManualHelper(object):
    ROBOT_LISTENER_API_VERSION = 3

    def start_test(self, data, result):
        tags = data.tags
        if "allure.label=manual" in tags:
            EXECUTION_CONTEXTS.current.dry_run = True

    def stop_test(self, data, result):
        EXECUTION_CONTEXTS.current.dry_run = False
