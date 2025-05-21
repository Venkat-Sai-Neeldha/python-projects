import importlib

def load_and_run(module_name):
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, 'run'):
            module.run()
        else:
            print(f"Module '{module_name}' does not have a 'run' function.")
    except ImportError as e:
        print(f"Error importing module '{module_name}': {e}")