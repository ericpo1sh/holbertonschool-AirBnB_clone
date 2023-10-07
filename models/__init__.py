#!/usr/bin/python3
""" initialization of models as package """
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
