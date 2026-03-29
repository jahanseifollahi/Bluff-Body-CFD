from ansys.geometry.core.sketch import Sketch
from ansys.geometry.core.math import Point2D
from ansys.geometry.core import launch_modeler
from ansys.geometry.core.misc import UNITS
#print("Yes, it works!")

#cyl_sketch=pygeo.Sketch()

units=UNITS.m
D = 0.1 # Diameter of Cylinder
L_upstream = D*20
L_downstream = D*40
H = 35*D

correction=(0.00121*(1.15))

L=L_upstream+L_downstream

move=L_upstream-(L/2)

modeler=launch_modeler(mode="spaceclaim")

design=modeler.create_design("bluff_body_cylinder")

sketch=Sketch()

sketch_wake=Sketch()

#sketch_semicircele=Sketch()

wake_height=10*D
wake_length=25*D

#semi_circle_start=Point2D([move,(-(D/2)-correction)],unit=units)
#semi_circle_end=Point2D([move,((D/2)+correction)],unit=units)
#semi_circle_peak=Point2D([move+(D/2)+correction,0],unit=units)

wake_center_x=move+((wake_length/2)-(5*D))

sketch_wake.box(Point2D([wake_center_x,0],unit=units),wake_length*units,wake_height*units)

sketch_wake.circle(center=Point2D([move,0],unit=units), radius=(D/2)*units)

#sketch_semicircele.arc_from_three_points(semi_circle_end, semi_circle_peak, semi_circle_start)

#sketch_semicircele.segment(semi_circle_start,semi_circle_end)

sketch.box(Point2D([0,0],unit=units),L*units,(H)*units)

sketch.circle(center=Point2D([move,0],unit=units), radius=(D/2)*units)

#circle=design.create_surface(name="Circle",sketch=sketch)

wake_zone=design.create_surface(name="WakeZone",sketch=sketch_wake)

#wake_zone.subtract(circle)

#semi_circle=design.create_surface(name="SemiCircle",sketch=sketch_semicircele)

#wake_zone.subtract(semi_circle)

fluid_domain=design.create_surface(name="FluidDomain",sketch=sketch)

fluid_domain.imprint_curves(sketch=sketch_wake, faces=fluid_domain.faces)

wake_zone_copy = design.create_surface(name="WakeZoneCopy", sketch=sketch_wake)

fluid_domain.subtract(wake_zone_copy)

print("Design created")

input("Press Enter to continue...")


