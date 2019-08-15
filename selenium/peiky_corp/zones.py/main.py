import unittest
from login_zones import *
from create_zone import *
from carga_masiva_zonas import *
from edit_zonas import *
from delete_zona import *


def tearDown(self):
    self.peiky.close()


if __name__ == "__main__":
    unittest.main(CreateZone())
