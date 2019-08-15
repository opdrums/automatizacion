import unittest
from login import *
from create_areas import *
from delete_areas import *
from edit_areas import *
from carga_masiva_areas import *


def tearDown(self):
    self.peiky.close()


if __name__ == "__main__":
    unittest.main(EditArea())
