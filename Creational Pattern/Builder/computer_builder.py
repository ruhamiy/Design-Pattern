from abc import ABC, abstractmethod


# PRODUCT

class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None
        self.power_supply = None
        self.cooling_system = None

    def __str__(self):
        return (
            "===== COMPUTER CONFIGURATION =====\n"
            f"CPU: {self.cpu}\n"
            f"RAM: {self.ram}\n"
            f"Storage: {self.storage}\n"
            f"GPU: {self.gpu}\n"
            f"Power Supply: {self.power_supply}\n"
            f"Cooling System: {self.cooling_system}\n"
        )


# BUILDER INTERFACE

class ComputerBuilder(ABC):

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_cpu(self, cpu):
        pass

    @abstractmethod
    def set_ram(self, ram):
        pass

    @abstractmethod
    def set_storage(self, storage):
        pass

    @abstractmethod
    def set_gpu(self, gpu):
        pass

    @abstractmethod
    def set_power_supply(self, power):
        pass

    @abstractmethod
    def set_cooling_system(self, cooling):
        pass


# CONCRETE BUILDER

class GamingComputerBuilder(ComputerBuilder):

    def __init__(self):
        self.reset()

    def reset(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu

    def set_ram(self, ram):
        self.computer.ram = ram

    def set_storage(self, storage):
        self.computer.storage = storage

    def set_gpu(self, gpu):
        self.computer.gpu = gpu

    def set_power_supply(self, power):
        self.computer.power_supply = power

    def set_cooling_system(self, cooling):
        self.computer.cooling_system = cooling

    def get_product(self):
        product = self.computer
        self.reset()
        return product


# DIRECTOR

class Director:

    def build_gaming_pc(self, builder: ComputerBuilder):
        builder.reset()
        builder.set_cpu("Intel i9")
        builder.set_ram("32GB DDR5")
        builder.set_storage("2TB NVMe SSD")
        builder.set_gpu("NVIDIA RTX 4090")
        builder.set_power_supply("850W Gold")
        builder.set_cooling_system("Liquid Cooling")

    def build_office_pc(self, builder: ComputerBuilder):
        builder.reset()
        builder.set_cpu("Intel i5")
        builder.set_ram("16GB DDR4")
        builder.set_storage("512GB SSD")
        builder.set_gpu("Integrated Graphics")
        builder.set_power_supply("500W Bronze")
        builder.set_cooling_system("Air Cooling")

    def build_server_pc(self, builder: ComputerBuilder):
        builder.reset()
        builder.set_cpu("AMD EPYC")
        builder.set_ram("64GB ECC RAM")
        builder.set_storage("4TB SSD RAID")
        builder.set_gpu("None")
        builder.set_power_supply("1000W Platinum")
        builder.set_cooling_system("Advanced Airflow System")


# CLIENT CODE

if __name__ == "__main__":

    director = Director()
    builder = GamingComputerBuilder()

    # Build Gaming PC
    director.build_gaming_pc(builder)
    gaming_pc = builder.get_product()
    print(gaming_pc)

    # Build Office PC
    director.build_office_pc(builder)
    office_pc = builder.get_product()
    print(office_pc)

    # Build Server PC
    director.build_server_pc(builder)
    server_pc = builder.get_product()
    print(server_pc)