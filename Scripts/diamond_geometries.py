from ansys.geometry.core.sketch import Sketch
from ansys.geometry.core.math import Point2D
from ansys.geometry.core import launch_modeler
from ansys.geometry.core.misc import UNITS
import math
#print("Yes, it works!")

#cyl_sketch=pygeo.Sketch()

units=UNITS.m

W=0.1
L=W*1.5
Half_Width = W/2 #perpendicular to flow
Half_length = L/2 #parallel to flow

L_upstream = (L)*20
L_downstream = (L)*40

Total_H = 35*W

Total_L=L_upstream+L_downstream

move=L_upstream-(Total_L/2)

modeler=launch_modeler(mode="spaceclaim")

design=modeler.create_design("bluff_body_diamond")

sketch=Sketch()

sketch_wake=Sketch()

#sketch_diamond=Sketch()

#sketch_diamond=Sketch()

#sketch_semicircele=Sketch()

wake_height=10*W
wake_length=25*L

wake_center_x=move+((wake_length/2)-(5*(L)))

sketch_wake.box(Point2D([wake_center_x,0],unit=units),wake_length*units,wake_height*units)

sketch.box(Point2D([0,0],unit=units),Total_L*units,Total_H*units)

# #Diamond Verticies
# leading  = Point2D([move - Half_length, 0], unit=units)
# trailing = Point2D([move + Half_length, 0], unit=units)
# top     = Point2D([move, Half_Width], unit=units)
# bottom   = Point2D([move, -Half_Width], unit=units)

# # Diamond edges
# sketch_wake.segment(leading, top)
# sketch_wake.segment(top, trailing)
# sketch_wake.segment(trailing, bottom)
# sketch_wake.segment(bottom, leading)

# sketch_diamond.segment(leading, top)
# sketch_diamond.segment(top, trailing)
# sketch_diamond.segment(trailing, bottom)
# sketch_diamond.segment(bottom, leading)


# import math

# r_lead = 0.002  # leading/trailing edge radius
# r_side = 0.005  # top/bottom radius

# # Diamond half-angle at leading/trailing = atan(Half_Width/Half_length)
# angle = math.atan2(Half_Width, Half_length)

# # Arc tangent offsets
# # Leading edge
# lead_top    = Point2D([leading[0] + r_lead*math.sin(angle), 
#                         leading[1] + r_lead*math.cos(angle)], unit=units)
# lead_bottom = Point2D([leading[0] + r_lead*math.sin(angle), 
#                         leading[1] - r_lead*math.cos(angle)], unit=units)

# # Top
# top_lead    = Point2D([top[0] - r_side*math.cos(angle), 
#                         top[1] - r_side*math.sin(angle)], unit=units)
# top_trail   = Point2D([top[0] + r_side*math.cos(angle), 
#                         top[1] - r_side*math.sin(angle)], unit=units)

# # Trailing edge
# trail_top   = Point2D([trailing[0] - r_lead*math.sin(angle), 
#                         trailing[1] + r_lead*math.cos(angle)], unit=units)
# trail_bot   = Point2D([trailing[0] - r_lead*math.sin(angle), 
#                         trailing[1] - r_lead*math.cos(angle)], unit=units)

# # Bottom
# bot_trail   = Point2D([bottom[0] + r_side*math.cos(angle), 
#                         bottom[1] + r_side*math.sin(angle)], unit=units)
# bot_lead    = Point2D([bottom[0] - r_side*math.cos(angle), 
#                         bottom[1] + r_side*math.sin(angle)], unit=units)

# # Straight segments
# sketch_wake.segment(lead_top,   top_lead)
# sketch_wake.segment(top_trail,  trail_top)
# sketch_wake.segment(trail_bot,  bot_trail)
# sketch_wake.segment(bot_lead,   lead_bottom)

# # Arcs at corners
# sketch_wake.arc_from_three_points(lead_bottom, leading,  lead_top)
# sketch_wake.arc_from_three_points(top_lead,    top,      top_trail)
# sketch_wake.arc_from_three_points(trail_top,   trailing, trail_bot)
# sketch_wake.arc_from_three_points(bot_trail,   bottom,   bot_lead)



wake_zone=design.create_surface(name="WakeZone",sketch=sketch_wake)

fluid_domain=design.create_surface(name="FluidDomain",sketch=sketch)

#fluid_domain.imprint_curves(sketch=sketch, faces=fluid_domain.faces)

#fluid_domain.imprint_curves(sketch=sketch_wake, faces=fluid_domain.faces)

#wake_zone_copy = design.create_surface(name="WakeZoneCopy", sketch=sketch_wake)

#fluid_domain.subtract(wake_zone_copy)

#diamond_center = Point2D([move, 0, 0], unit=units)
#face_to_remove = fluid_domain.faces.find_closest(diamond_center)
#design.delete(face_to_remove)

print("Design created")

input("Press Enter to continue...")



