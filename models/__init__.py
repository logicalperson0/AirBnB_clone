#!/usr/bin/python3
"""Import the storage in engine"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
