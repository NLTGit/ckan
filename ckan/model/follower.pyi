"""
This type stub file was generated by pyright.
"""

import sqlalchemy
from ckan.model import domain_object, meta

class ModelFollowingModel(domain_object.DomainObject):
    def __init__(self, follower_id, object_id) -> None: ...
    @classmethod
    def get(cls, follower_id, object_id):
        """Return a ModelFollowingModel object for the given follower_id and
        object_id, or None if no such follower exists.

        """
        ...
    @classmethod
    def is_following(cls, follower_id, object_id):
        """Return True if follower_id is currently following object_id, False
        otherwise.

        """
        ...
    @classmethod
    def followee_count(cls, follower_id):
        """Return the number of objects followed by the follower."""
        ...
    @classmethod
    def followee_list(cls, follower_id):
        """Return a list of objects followed by the follower."""
        ...
    @classmethod
    def follower_count(cls, object_id):
        """Return the number of followers of the object."""
        ...
    @classmethod
    def follower_list(cls, object_id):
        """Return a list of followers of the object."""
        ...

class UserFollowingUser(ModelFollowingModel):
    """A many-many relationship between users.

    A relationship between one user (the follower) and another (the object),
    that means that the follower is currently following the object.

    """

    ...

user_following_user_table = sqlalchemy.Table(
    "user_following_user",
    meta.metadata,
    sqlalchemy.Column(
        "follower_id",
        sqlalchemy.types.UnicodeText,
        sqlalchemy.ForeignKey(
            "user.id", onupdate="CASCADE", ondelete="CASCADE"
        ),
        primary_key=True,
        nullable=False,
    ),
    sqlalchemy.Column(
        "object_id",
        sqlalchemy.types.UnicodeText,
        sqlalchemy.ForeignKey(
            "user.id", onupdate="CASCADE", ondelete="CASCADE"
        ),
        primary_key=True,
        nullable=False,
    ),
    sqlalchemy.Column("datetime", sqlalchemy.types.DateTime, nullable=False),
)

class UserFollowingDataset(ModelFollowingModel):
    """A many-many relationship between users and datasets (packages).

    A relationship between a user (the follower) and a dataset (the object),
    that means that the user is currently following the dataset.

    """

    ...

user_following_dataset_table = sqlalchemy.Table(
    "user_following_dataset",
    meta.metadata,
    sqlalchemy.Column(
        "follower_id",
        sqlalchemy.types.UnicodeText,
        sqlalchemy.ForeignKey(
            "user.id", onupdate="CASCADE", ondelete="CASCADE"
        ),
        primary_key=True,
        nullable=False,
    ),
    sqlalchemy.Column(
        "object_id",
        sqlalchemy.types.UnicodeText,
        sqlalchemy.ForeignKey(
            "package.id", onupdate="CASCADE", ondelete="CASCADE"
        ),
        primary_key=True,
        nullable=False,
    ),
    sqlalchemy.Column("datetime", sqlalchemy.types.DateTime, nullable=False),
)

class UserFollowingGroup(ModelFollowingModel):
    """A many-many relationship between users and groups.

    A relationship between a user (the follower) and a group (the object),
    that means that the user is currently following the group.

    """

    ...

user_following_group_table = sqlalchemy.Table(
    "user_following_group",
    meta.metadata,
    sqlalchemy.Column(
        "follower_id",
        sqlalchemy.types.UnicodeText,
        sqlalchemy.ForeignKey(
            "user.id", onupdate="CASCADE", ondelete="CASCADE"
        ),
        primary_key=True,
        nullable=False,
    ),
    sqlalchemy.Column(
        "object_id",
        sqlalchemy.types.UnicodeText,
        sqlalchemy.ForeignKey(
            "group.id", onupdate="CASCADE", ondelete="CASCADE"
        ),
        primary_key=True,
        nullable=False,
    ),
    sqlalchemy.Column("datetime", sqlalchemy.types.DateTime, nullable=False),
)
