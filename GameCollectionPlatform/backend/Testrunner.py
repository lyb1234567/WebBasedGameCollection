from django.test.runner import DiscoverRunner
from importlib import import_module
import os
Models=['Collection','customUser','Community','Review','GamePublisher','Game']
class CustomTestRunner(DiscoverRunner):
    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        results = super().run_tests(test_labels, extra_tests, **kwargs)
        for label in test_labels:
            self.check_test_content(label)
            Models.remove(label)
        if not Models:
            return results
        print('\n\n')
        for notFinished in Models:
            print(f"Tests for {notFinished} has not been created")
        return results

    def check_test_content(self,filename):
            module_path = f"{filename}.tests"
            try:
                module = import_module(module_path)
                if hasattr(module, 'TestCase') and len(module.TestCase.__dict__) > 0:
                    print(f"Tests for {filename} finished")
                else:
                    print(f"Tests for {filename} not finished")
            except ModuleNotFoundError:
                print(f"No tests found for {filename}. Module not found: {module_path}")