class Machine:
    def __init__(self, name, processing_time):
        self.name = name
        self.processing_time = processing_time

    def process_product(self, product):
        print(f"{product} is being processed at {self.name}")
        # Simulate processing time
        # You can add additional logic specific to each workstation
        print(f"{product} finished processing at {self.name}")
