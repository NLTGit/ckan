"""
This type stub file was generated by pyright.
"""

import cgi
import logging
from werkzeug.datastructures import FileStorage as FlaskFileStorage

ALLOWED_UPLOAD_TYPES = (cgi.FieldStorage, FlaskFileStorage)
MB = 1 << 20
log = logging.getLogger(__name__)
_storage_path = None
_max_resource_size = None
_max_image_size = None

def get_uploader(upload_to, old_filename=...):
    """Query IUploader plugins and return an uploader instance for general
    files."""
    ...

def get_resource_uploader(data_dict):
    """Query IUploader plugins and return a resource uploader instance."""
    ...

def get_storage_path():
    """Function to cache storage path"""
    ...

def get_max_image_size(): ...
def get_max_resource_size(): ...

class Upload(object):
    def __init__(self, object_type, old_filename=...) -> None:
        """Setup upload by creating a subdirectory of the storage directory
        of name object_type. old_filename is the name of the file in the url
        field last time"""
        ...
    def update_data_dict(self, data_dict, url_field, file_field, clear_field):
        """Manipulate data from the data_dict.  url_field is the name of the
        field where the upload is going to be. file_field is name of the key
        where the FieldStorage is kept (i.e the field where the file data
        actually is). clear_field is the name of a boolean field which
        requests the upload to be deleted.  This needs to be called before
        it reaches any validators"""
        ...
    def upload(self, max_size=...):
        """Actually upload the file.
        This should happen just before a commit but after the data has
        been validated and flushed to the db. This is so we do not store
        anything unless the request is actually good.
        max_size is size in MB maximum of the file"""
        ...

class ResourceUpload(object):
    def __init__(self, resource) -> None: ...
    def get_directory(self, id): ...
    def get_path(self, id): ...
    def upload(self, id, max_size=...):
        """Actually upload the file.

        :returns: ``'file uploaded'`` if a new file was successfully uploaded
            (whether it overwrote a previously uploaded file or not),
            ``'file deleted'`` if an existing uploaded file was deleted,
            or ``None`` if nothing changed
        :rtype: ``string`` or ``None``

        """
        ...
