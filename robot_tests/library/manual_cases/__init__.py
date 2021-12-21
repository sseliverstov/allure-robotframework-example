from robot.running.context import EXECUTION_CONTEXTS


class ManualTestCases(object):
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self

    def start_test(self, data, result):
        tags = data.tags

        if "allure.label=manual" in tags:
            EXECUTION_CONTEXTS.current.dry_run = True

            EXECUTION_CONTEXTS.current.actual_get_runner = EXECUTION_CONTEXTS.current.get_runner
            fake_runner = EXECUTION_CONTEXTS.current.get_runner("Fake keyword")

            def fake_get_runner(name):
                lib, kw = name.split(".", 1)
                fake_runner.name = kw or name
                return fake_runner

            EXECUTION_CONTEXTS.current.get_runner = fake_get_runner

    def stop_test(self, data, result):
        EXECUTION_CONTEXTS.current.dry_run = False
        EXECUTION_CONTEXTS.current.get_runner = EXECUTION_CONTEXTS.current.actual_get_runner

    def fake_keyword(self, *args, **kwargs):
        raise NotImplementedError()
