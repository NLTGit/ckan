"""
This type stub file was generated by pyright.
"""

from contextlib import contextmanager
from typing import Generator, Iterable, List, Union
from pyutilib.component.core import (
    ExtensionPoint,
    Plugin as _pca_Plugin,
    SingletonPlugin as _pca_SingletonPlugin,
    implements as _implements,
)

implements = _implements

PLUGINS_ENTRY_POINT_GROUP = "ckan.plugins"
SYSTEM_PLUGINS_ENTRY_POINT_GROUP = "ckan.system_plugins"
TEST_PLUGINS_ENTRY_POINT_GROUP = "ckan.test_plugins"
GROUPS = [
    PLUGINS_ENTRY_POINT_GROUP,
    SYSTEM_PLUGINS_ENTRY_POINT_GROUP,
    TEST_PLUGINS_ENTRY_POINT_GROUP,
]
@contextmanager
def use_plugin(
    *plugins: str,
) -> Generator[Union[SingletonPlugin, List[SingletonPlugin]], None, None]: ...

class PluginImplementations(ExtensionPoint):
    def __iter__(self) -> Iterable[SingletonPlugin]: ...

class PluginNotFoundException(Exception): ...
class Plugin(_pca_Plugin): ...
class SingletonPlugin(_pca_SingletonPlugin): ...

def get_plugin(plugin) -> SingletonPlugin: ...
def plugins_update() -> None: ...
def load_all() -> None: ...
def load(*plugins) -> Union[SingletonPlugin, List[SingletonPlugin]]: ...
def unload_all() -> None: ...
def unload(*plugins) -> None: ...
def plugin_loaded(name) -> bool: ...
def find_system_plugins() -> List[SingletonPlugin]: ...
