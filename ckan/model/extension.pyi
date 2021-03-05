"""
This type stub file was generated by pyright.
"""

import logging
from sqlalchemy.orm.interfaces import MapperExtension
from sqlalchemy.orm.session import SessionExtension

"""
Provides bridges between the model and plugin PluginImplementationss
"""
log = logging.getLogger(__name__)

class ObserverNotifier(object):
    """
    Mixin for hooking into SQLAlchemy
    MapperExtension/SessionExtension
    """

    observers = ...

class PluginMapperExtension(MapperExtension):
    """
    Extension that calls plugins implementing IMapper on SQLAlchemy
    MapperExtension events
    """

    def notify_observers(self, func):
        """
        Call func(observer) for all registered observers.

        :param func: Any callable, which will be called for each observer
        :returns: EXT_CONTINUE if no errors encountered, otherwise EXT_STOP
        """
        ...
    def before_insert(self, mapper, connection, instance): ...
    def before_update(self, mapper, connection, instance): ...
    def before_delete(self, mapper, connection, instance): ...
    def after_insert(self, mapper, connection, instance): ...
    def after_update(self, mapper, connection, instance): ...
    def after_delete(self, mapper, connection, instance): ...

class PluginSessionExtension(SessionExtension):
    """
    Class that calls plugins implementing ISession on SQLAlchemy
    SessionExtension events
    """

    def notify_observers(self, func):
        """
        Call func(observer) for all registered observers.

        :param func: Any callable, which will be called for each observer
        :returns: EXT_CONTINUE if no errors encountered, otherwise EXT_STOP
        """
        ...
    def after_begin(self, session, transaction, connection): ...
    def before_flush(self, session, flush_context, instances): ...
    def after_flush(self, session, flush_context): ...
    def before_commit(self, session): ...
    def after_commit(self, session): ...
    def after_rollback(self, session): ...
