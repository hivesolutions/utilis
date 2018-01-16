#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Utilis Tasks
# Copyright (c) 2008-2018 Hive Solutions Lda.
#
# This file is part of Hive Utilis Tasks.
#
# Hive Utilis Tasks is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Utilis Tasks is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Utilis Tasks. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2018 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import os
import unittest

import utilis

class ContextTest(unittest.TestCase):

    def test_simple(self):
        file_path = os.path.realpath(__file__)
        file_dir = os.path.dirname(file_path)
        path = os.path.join(file_dir, "res", "simple.tpl")
        os.environ["SIMPLE"] = "SIMPLE_VALUE"
        result = utilis.context.run(path = path, return_r = True)
        self.assertEqual(result, "SIMPLE_VALUE")

    def test_silent(self):
        file_path = os.path.realpath(__file__)
        file_dir = os.path.dirname(file_path)
        path = os.path.join(file_dir, "res", "simple.tpl")
        os.environ["SIMPLE"] = "SIMPLE_VALUE"
        result = utilis.context.run(path = path, return_r = False)
        self.assertEqual(result, None)

    def test_error(self):
        result = utilis.context.run(path = None, args = [])
        self.assertEqual(result, 1)
