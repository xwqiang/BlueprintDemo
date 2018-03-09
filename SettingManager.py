import importlib
import os

from decorators.singleton import singleton


@singleton
class SettingManager(object):
    def __init__(self, env_var, setting_dir):
        """

        """
        self._content = dict()
        self.env_var = env_var
        self.env = os.getenv(self.env_var, None)
        if self.env:
            self.read('.'.join([setting_dir, self.env]))

    def __del__(self):
        self._content.clear()

    def __getitem__(self, item):
        return self._content.get(item, None)

    def __setitem__(self, key, value):
        self._content[key] = value
        return value

    def __getattr__(self, item):
        return self._content.get(item, None)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            object.__setattr__(self, key, value)
        self._content[key] = value
        return value

    def read(self, relative_path):
        """read settings from python file"""
        try:
            settings = importlib.import_module(relative_path)
        except ImportError:
            raise ImportError('Wrong relative path provided.')
        keys = [key for key in dir(settings) if not key.startswith('__')]
        for key in keys:
            # same key in different files may cause cover problem
            self._content[key] = getattr(settings, key)
        return self

    def getvalue(self, key):
        return self.__getattr__(key)

setting = SettingManager('ENV_NAME', 'config')
