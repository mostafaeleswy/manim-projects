from big_ol_pile_of_manim_imports import *
from math import cos, sin, pi

class Pythagoras(Scene):
    def construct(self):
        title = TextMobject("pythagoras theorem")
        title.to_edge(UP)

        self.play(Write(title))

        self.wait(2)
   
        main_triangle = Polygon(
            [-1, -2, 0],
            [1, -2, 0],
            [1, 2 , 0],
            color=YELLOW
        )

        main_triangle.set_fill(YELLOW, 0.6)
        
        self.play( ShowCreation(main_triangle) )

        self.wait(2)

        text1= TextMobject("a")
        text2= TextMobject("b")
        text3= TextMobject("c")

        text1.next_to(main_triangle,RIGHT,buff=0.2)
        text2.next_to(main_triangle,DOWN,buff=0.2)
        text3.next_to(main_triangle,LEFT,buff=-.7)



        self.play(Write(text1),Write(text2),Write(text3))
        self.wait(3)

        formula_1=TexMobject("c^{2}=a^{2}+b^{2}")
        formula_1.scale(1)
        formula_1.to_edge(DOWN)
        self.play(Write(formula_1))

        self.wait(4)


        self.play(FadeOut(main_triangle),FadeOut(text1),FadeOut(text2),FadeOut(text3),FadeOut(formula_1))

        self.wait(2)

        triangle1 = Polygon(
            [6, -3, 0],
            [6, -1, 0],
            [4.5, -3 , 0],
            color=WHITE
        )

        triangle2 = Polygon(
            [4, -3, 0],
            [4, -1, 0],
            [2.5, -3 , 0],
            color=WHITE
        )       
        triangle3 = Polygon(
            [2, -3, 0],
            [2, -1, 0],
            [.5, -3 , 0],
            color=WHITE
        )    

        triangle4 = Polygon(
            [0, -3, 0],
            [0, -1, 0],
            [-1.5, -3 , 0],
            color=WHITE
        )    

        square = Polygon(
            [-2, -3, 0],
            [-2, -2.5, 0],
            [-2.5, -2.5 , 0],
            [-2.5, -3 , 0],

            color=WHITE
        )    

        triangle1.set_fill(BLUE, 1)
        triangle2.set_fill(BLUE, 1)
        triangle3.set_fill(BLUE, 1)
        triangle4.set_fill(BLUE, 1)
        square.set_fill(RED, 1)
        self.play( ShowCreation(triangle1), ShowCreation(triangle2),ShowCreation(triangle3),ShowCreation(triangle4),ShowCreation(square))
        self.wait(1)

        

        text4= TextMobject("a")
        text5= TextMobject("b")
        text6= TextMobject("c")
        text4.scale(.7)
        text5.scale(.7)
        text6.scale(.7)


        text4.next_to(triangle1,RIGHT,buff=0.1)
        text5.next_to(triangle1,DOWN,buff=0.1)
        text6.next_to(triangle1,LEFT,buff=-.4)



        self.play(Write(text4),Write(text5),Write(text6))
        self.wait(1)


        text7= TextMobject("b-a")

        text7.scale(.7)



        text7.next_to(square,UP,buff=0.1)




        self.play(Write(text7))
        self.wait(2)

        #self.play(ApplyMethod(square.shift, LEFT * 3))


        
        c=2.5
        triangle5 = Polygon(
            [c/2, c/2, 0],
            [-c/2, c/2, 0],
            [c/2-1.6, c/2-1.2, 0],
            color=WHITE
        )
        triangle6 = Polygon(
            [c/2, c/2, 0],
            [c/2, -c/2, 0],
            [c/2-1.2, c/2-.9 , 0],
            color=WHITE
        )       
        triangle7 = Polygon(
            [c/2, -c/2, 0],
            [-c/2, -c/2, 0],
            [-c/2+1.6, -c/2+1.2, 0],
            color=WHITE
        )

        triangle8 = Polygon(
            [-c/2, -c/2, 0],
            [-c/2, c/2, 0],
            [-c/2+1.2, -c/2+.9 , 0],
            color=WHITE
        )       

        square2 = Polygon(
            [-c/2+1.6, -c/2+1.2, 0],
            [-c/2+1.2, -c/2+.9 , 0],
            [c/2-1.6, c/2-1.2, 0],            
            [c/2-1.2, c/2-.9 , 0],

            color=WHITE
        )    
        

        group1 = VGroup(square2, triangle5, triangle6, triangle7, triangle8)
        group1.move_to(4*LEFT)

        self.play( ShowCreation(group1))

        self.wait(3)

        self.play(FadeOut(text4),FadeOut(text5),FadeOut(text6),FadeOut(text7))



        self.play(ApplyMethod(triangle1.move_to, [-4,c/2, 0]))
        self.play(ApplyMethod(triangle1.rotate, -0.2952*PI))
        self.play(ApplyMethod(triangle2.move_to, [-4,-c/2, 0]))
        self.play(ApplyMethod(triangle2.rotate, PI*+0.704532))
        self.play(ApplyMethod(triangle3.move_to, [-4+c/2,0, 0]))
        self.play(ApplyMethod(triangle3.rotate,-0.79517*PI))
        self.play(ApplyMethod(triangle4.move_to, [-4-c/2,0, 0]))
        self.play(ApplyMethod(triangle4.rotate, .204832*PI))
        self.play(ApplyMethod(square.move_to, [-4,0, 0]))
        self.play(ApplyMethod(square.rotate, .204832*PI))        
        self.wait(2)
        
        text8= TextMobject("c")
        text8.next_to(triangle1,UP,buff=0.1)
        text9= TextMobject("c")
        text9.next_to(triangle3,RIGHT,buff=0.1)
        self.play(Write(text8),Write(text9))

        formula_2=TexMobject("Area = c^{2}")

    
        formula_2.scale(1)
        formula_2.next_to(triangle2,DOWN,buff=0.5)
        self.play(Write(formula_2))
        self.wait(2)



        triangle1.generate_target()
        triangle1.target.shift([0,0, 0]).rotate(0)

        triangle2.generate_target()
        triangle2.target.shift([0,c, 0]).rotate(0)

        gruou2=VGroup(triangle1.target,triangle2.target)
        gruou2.rotate(0.2952*PI).shift(c/2*DOWN+8*RIGHT)


        self.play(MoveToTarget(triangle1.copy()), MoveToTarget(triangle2.copy()))

        self.wait(1)


        triangle3.generate_target()
        triangle3.target.shift([0,0, 0]).rotate(0)

        triangle4.generate_target()
        triangle4.target.shift([c,0, 0]).rotate(0)

        gruou3=VGroup(triangle3.target,triangle4.target)
        gruou3.rotate(0.2952*PI).shift(-0.25+5.25*RIGHT)



        self.play(MoveToTarget(triangle3.copy()), MoveToTarget(triangle4.copy()))

        self.wait(2)        

        square2.generate_target()
        square2.target.shift([7,0.75, 0]).rotate(0.2952*PI)
        square2.target.set_fill(RED, 1)
        self.play(MoveToTarget(square2.copy()))
        self.wait(2)        

        text9= TextMobject("b")
        text10= TextMobject("a")
        text11= TextMobject("b-a")
        text12= TextMobject("b")
        text13= TextMobject("a")
        text14= TextMobject("a")
        
        

        text9.next_to(triangle1.target,RIGHT,buff=0.2)
        self.play(Write(text9))
        self.wait(1)

        text10.next_to(triangle2.target,UP,buff=0.1)
        text10.scale(.5)
        self.play(Write(text10))
        self.wait(1)

        text11.next_to(square2.target,UP,buff=0.1)
        text11.scale(.5)
        self.play(Write(text11))
        self.wait(1)

        text12.next_to(square2.target,UP,buff=.5)
        text12.shift(RIGHT*.75)
        text12.scale(1)
        self.play(Write(text12))
        self.wait(1)

        text13.next_to(triangle3.target,LEFT,buff=.3)
        text13.scale(1)
        self.play(Write(text13))
        self.wait(1)

        text14.next_to(triangle4.target,UP,buff=.1)
        text14.shift(LEFT*.3)

        text14.scale(1)
        self.play(Write(text14))
        self.wait(1)

        formula_3=TexMobject("Area = a^{2}+b^{2}")

    
        formula_3.scale(1)
        formula_3.next_to(triangle2.target,DOWN,buff=0.5)
        formula_3.shift(1*LEFT)
        self.play(Write(formula_3))
        self.wait(2)

        formula_4=TexMobject("c^{2} = a^{2}+b^{2}")

    
        formula_4.scale(1)
        formula_4.to_edge(DOWN)
        self.play(Write(formula_4))
        self.wait(4)