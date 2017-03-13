#!/usr/bin/env python
# coding=utf-8

import unittest

class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      # для проверки ожидаемого результата
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      # для проверки условия
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      # для проверки, что метод порождает исключение
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # Проверим, что s.split не работает, если разделитель - не строка
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()