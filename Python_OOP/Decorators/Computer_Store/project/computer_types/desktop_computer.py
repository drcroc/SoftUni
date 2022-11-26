from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    AVAILABLE_PROCESSORS = \
        {
            'AMD Ryzen 7 5700G': 500,
            'Intel Core i5-12600K': 600,
            'Apple M1 Max': 1800
        }

    MAX_RAM = 128

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        if processor not in DesktopComputer.AVAILABLE_PROCESSORS.keys():
            raise ValueError(f'{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!')

        if ram > DesktopComputer.MAX_RAM or not self.validating_ram(ram):
            raise ValueError(f'{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!')

        self.set_computer_parts(processor, ram)
        return f'Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$.'
