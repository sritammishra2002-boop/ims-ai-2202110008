
import math
from pathlib import Path
from cadquery import func as cf


def clutch_brick(length, width, height, stud_d, stud_h, spacing):

    # Create main brick body
    body = cf.box(length, width, height)

    # Create one stud
    stud = cf.cylinder(d=stud_d, h=stud_h)

    # Generate 2 rows × 4 columns = 8 studs
    for row in range(2):
        for col in range(4):

            x = (col - 1.5) * spacing
            y = (row - 0.5) * spacing

            new_stud = stud.moved(
                x=x,
                y=y,
                z=height
            )

            body = body + new_stud

    return body


# Create 2 × 4 Clutch Brick
brick = clutch_brick(
    31.2,
    15.6,
    9.6,
    4.8,
    1.7,
    8.0
)


# Calculate expected volume
expected = (
    31.2 * 15.6 * 9.6
    + 8 * math.pi * (4.8 / 2) ** 2 * 1.7
)


# Verify volume
actual = brick.Volume()

assert abs(actual - expected) < 0.5, "Volume check failed!"


# Save STL directly to Windows Desktop
desktop = Path.home() / "Desktop"
output_file = desktop / "brick.stl"

brick.exportStl(str(output_file))


# Display results
print("2 x 4 Clutch Brick created successfully!")
print("Number of studs: 8")
print("Expected Volume:", expected)
print("Actual Volume:", actual)
print("STL saved at:", output_file)
