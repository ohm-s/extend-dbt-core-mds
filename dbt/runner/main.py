import os
import re
import sys
from dbt.context import base

original_modules = base.get_context_modules
class Loader:
    __all__ = ['load_module']

    dynamic_modules = {}

    def load_module(custom_module_name, file_location):
      import importlib.util
      import sys
      spec= importlib.util.spec_from_file_location(custom_module_name, file_location)
      module_spec_loaded = importlib.util.module_from_spec(spec)
      spec.loader.exec_module(module_spec_loaded)
      sys.modules[custom_module_name] = module_spec_loaded
      Loader.dynamic_modules[custom_module_name] = module_spec_loaded


def get_dynamic_module_context():
    context_exports = Loader.__all__
    obj = {name: getattr(Loader, name) for name in context_exports}
    obj['inc'] = Loader.dynamic_modules
    return obj

def get_context_modules_with_dynamic():
    global original_modules
    modules = original_modules()
    get_dynamic_modules_wrapper = get_dynamic_module_context()
    modules['dynamic'] = get_dynamic_modules_wrapper
    return modules

Loader.load_module('sample', os.environ['DBT_PROJECT_DIR']  + '/macros/__dynamic_modules__/sample/__init__.py')

base.get_context_modules = get_context_modules_with_dynamic

# Copied from the below command
# cat `which dbt`
# This might change depending on your dbt version
from dbt.cli.main import cli
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(cli())
