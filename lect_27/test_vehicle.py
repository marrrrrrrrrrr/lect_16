import pytest
from vehicle import Vehicle, ElectricVehicle

class TestVehicle:
    def test_fuel_up_vehicle(self):
        veh1 = Vehicle("Porsche", "Macan", 2019)
        assert veh1.fuel_up == "Gas tank is now full or can move."
        
        veh1.model = "Cayenne"
        assert veh1.fuel_up == "Gas tank is now full or can move."

    def test_drive_vehicle(self):
        veh1 = Vehicle("Porsche", "Macan", 2019)
        assert veh1.drive() == "The Macan is now driving."

    def test_fuel_up_electric_vehicle(self):
        veh2 = ElectricVehicle("BMW", "i4", 2022)
        assert veh2.fuel_up == "This vehicle has no fuel tank!"

    def test_charge_electric_vehicle(self):
        veh2 = ElectricVehicle("BMW", "i4", 2022)
        assert veh2.charge == "The vehicle is now charged."

if __name__ == "__main__":
    pytest.main()