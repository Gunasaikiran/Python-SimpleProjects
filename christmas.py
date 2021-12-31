#Python Christmas Tree
from turtle import *

def move_to( x, y ):
    penup()
    setx( x )
    sety( y )
    pendown()

def draw_triangle( size ):
    color( 'black', 'green')
    begin_fill()
    setheading( 240 )
    for i in range( 0,3 ):
        forward( size )
        left( 120 )
    end_fill()

def draw_circle( size, c_color ):
    color( 'black', c_color )
    begin_fill()
    circle( size )
    end_fill()
 
def draw_star( size ):
    color( 'black', 'yellow' )
    setheading( 72 )
    begin_fill()
    
    for i in range( 0, 5 ):
        forward( size )
        right( 144 )
    end_fill()

# Draw the tree
move_to( 50, -80 )
draw_triangle( 200 )

move_to( 50, 0 )
draw_triangle( 150 )
 
move_to( 50, 50 )
draw_triangle( 100 )
 
# Draw the star
 
move_to( 39, 40 )
draw_star( 40 )
 
# Draw the ornaments
 
move_to( 80, -40 )
#Adding colour red
draw_circle( 15, 'red' )
 
move_to( 20, -100 )
#Adding colour blue
draw_circle( 15, 'blue' )
 
move_to( 100, -200 )
#Adding colour purple
draw_circle( 15, 'purple' )
 
 
# Draw the message
move_to( -30, 100 )
write( "Merry Christmas!", font=( "Arial", 16, "bold" ) )
done()