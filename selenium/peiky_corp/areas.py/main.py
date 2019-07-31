import unittest
from login import *
from new_areas import *
from delete_areas import *


def tearDown(self):
    self.peiky.close()


if __name__ == "__main__":
    unittest.main(DeleteArea())
