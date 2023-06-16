from machine import Machine
from product import Product
from simulation import ProductionLineSimulation

# Define the production line layout
workstation1 = Machine("Machine 1", 2)
workstation2 = Machine("Machine 2", 3)
workstation3 = Machine("Machine 3", 2)
layout = [workstation1, workstation2, workstation3]

# Create a digital twin simulation instance
simulation = ProductionLineSimulation(layout)

# Run the simulation
simulation.run_simulation(10)
