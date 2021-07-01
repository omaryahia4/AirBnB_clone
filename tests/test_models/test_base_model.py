#!/usr/bin/python3
"""Unittest class BaseModel
"""
import unittest
import models
from models.base_model import BaseModel
from datetime import datetime


class BaseModelTest(unittest.TestCase):
    """ basemodels test """

    def test_attrb(self):
        """test atttr"""

        bm = BaseModel()
        bm1 = BaseModel()
        self.assertRaises(AttributeError)
        self.assertTrue(isinstance(bm, BaseModel))
        bm.name = "bz"
        self.assertEqual(bm.name, "bz")
        bm.id = "1"
        self.assertEqual(bm.id, "1")
        self.assertTrue(hasattr(bm1, "created_at"))
        self.assertTrue(hasattr(bm1, "updated_at"))
        self.assertTrue(hasattr(bm1, "created_at"))
        self.assertNotEqual(bm.id, bm1.id)
        self.assertNotEqual(bm.id, bm1.id)
        self.assertNotEqual(bm.created_at, bm1.created_at)
        self.assertNotEqual(bm.updated_at, bm1.updated_at)
        self.assertTrue(isinstance(bm.created_at, datetime))
        self.assertTrue(isinstance(bm.updated_at, datetime))
        self.assertTrue(type(bm1.to_dict()), dict)

    def test_str(self):
        """test str"""
        bm = BaseModel()
        x = "[BaseModel] ({}) {}".format(bm.id, bm.__dict__)
        self.assertEqual(x, str(bm))

    def to_dict(self):
        """test to_dict
        """
        bm = BaseModel()
        dic = bm.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        self.assertEqual(print(dic), print(bm.to_dict()))
        self.assertIsInstance(bm.to_dict(), dic)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()
