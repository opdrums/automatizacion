import unittest
from login import *
from new_areas import *
from delete_areas import *
from delete_areas_firts_opcion import *
from edit_area import *
from multiple_areas_delete import *
from multiple_areas import *


def tearDown(self):
    self.peiky.close()


if __name__ == "__main__":
    unittest.main(LoginUnittests())
