import unittest
from vehicle import Vehicle, ElectricVehicle

class TestVehicle(unittest.TestCase):
    def test_fuel_up_vehicle(self):
        veh1 = Vehicle("Porsche", "Macan", 2019)
        self.assertEqual(veh1.fuel_up, "Gas tank is now full or can move.")

    def test_drive_vehicle(self):
        veh1 = Vehicle("Porsche", "Macan", 2019)
        self.assertEqual(veh1.drive, "The Macan is now driving.")

    def test_fuel_up_electric_vehicle(self):
        veh2 = ElectricVehicle("BMW", "i4", 2022)
        self.assertEqual(veh2.fuel_up, "This vehicle has no fuel tank!")

    def test_charge_electric_vehicle(self):
        veh2 = ElectricVehicle("BMW", "i4", 2022)
        self.assertEqual(veh2.charge, "The vehicle is now charged.")

if __name__ == '__main__':
    unittest.main()