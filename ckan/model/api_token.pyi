"""
This type stub file was generated by pyright.
"""

import datetime
from sqlalchemy import Column, ForeignKey, Table, types
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict
from ckan.model import DomainObject, meta

api_token_table = Table(
    u"api_token",
    meta.metadata,
    Column(u"id", types.UnicodeText, primary_key=True, default=_make_token),
    Column(u"name", types.UnicodeText),
    Column(u"user_id", types.UnicodeText, ForeignKey(u"user.id")),
    Column(u"created_at", types.DateTime, default=datetime.datetime.utcnow),
    Column(u"last_access", types.DateTime, nullable=True),
    Column(u"plugin_extras", MutableDict.as_mutable(JSONB)),
)

class ApiToken(DomainObject):
    def __init__(self, user_id=..., name=...) -> None: ...
    @classmethod
    def get(cls, id): ...
    @classmethod
    def revoke(cls, id): ...
    def touch(self, commit=...): ...
    def set_extra(self, key, value, commit=...): ...
