
from cadquery import func as cf

# Day 7: Parametric CAD - Plate with a hole

plate = cf.box(80, 50, 10)

hole = cf.cylinder(d=20, h=10).moved(x=20)

part = plate - hole

print("Valid:", part.isValid())
print("Volume:", round(part.Volume(), 1))

assert part.isValid()
assert abs(part.Volume() - 36858.4) < 1.0

part.exportStl("plate.stl")

print("Plate exported successfully!")
