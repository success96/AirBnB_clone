#!/usr/bin/python3
"""This is a magic method for models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
