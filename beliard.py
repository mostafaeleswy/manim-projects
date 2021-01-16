from big_ol_pile_of_manim_imports import *
from math import cos, sin, pi



class biliard(Scene):
    def construct(self):
        table = Polygon(
            [-39, 24.5, 0],
            [-39, -24.5, 0],
            [39, -24.5, 0],
            [39, 24.5, 0],            

            color=YELLOW
        )        

        table.scale(.1)
        self.play( ShowCreation(table))
        self.wait(3)

        text1= TextMobject("49 m ")
        text2= TextMobject("78 m ")

        text1.scale(2)
        text2.scale(2)

        text1.next_to(table,RIGHT,buff=0.5)
        text2.next_to(table,DOWN,buff=0.5)
        self.play( Write(text1),Write(text2))

        self.wait(3)

        dot1=Dot()
        dot2=Dot()
        dot3=Dot()
        dot4=Dot()        


        dot1.move_to([-3.9, 2.45, 0])
        dot2.move_to([-3.9, -2.45, 0])
        dot3.move_to([3.9, 2.45, 0])
        dot4.move_to([3.9, -2.45, 0])

        

        dot1.set_fill(RED, 1)
        dot2.set_fill(RED, 1)
        dot3.set_fill(RED, 1)
        dot4.set_fill(RED, 1)




        self.play( ShowCreation(dot1),ShowCreation(dot2),ShowCreation(dot3),ShowCreation(dot4))

        self.wait(3)

        ball=Dot()
	    
        ball.move_to([-3.9, -2.45, 0])
        ball.set_fill(GREEN, 1)
        ball.scale(3)
        self.play( ShowCreation(ball))
        self.wait(3)

        line = Line([-39/10, -24.5/10, 0],[10/10,24.5/10,0])
        self.play(ShowCreation(line))	
        self.wait(3)

        text3= TexMobject("45^{o}")
        text3.next_to(dot2,RIGHT,buff=0.5)
        text3.shift(0.5*UP)
        self.play( Write (text3))
        self.wait(20)

class biliard2(Scene):
    def construct(self):

        text4= TextMobject("Answer ")
        text4.scale(3)
        self.play(Write (text4))
        self.wait(0.5)
        self.play(FadeOut (text4))
        text5= TextMobject("3 ")
        text5.scale(3)
        self.play(Write (text5))
        self.wait(0.5)
        self.play(FadeOut (text5))        
        text6= TextMobject("2 ")
        text6.scale(3)
        self.play(Write (text6))
        self.wait(0.5)
        self.play(FadeOut (text6))   
        text7= TextMobject("1 ")
        text7.scale(3)
        self.play(Write (text7))
        self.wait(0.5)
        self.play(FadeOut (text7))   
        text8= TextMobject("0 ")
        text8.scale(3)
        self.play(Write (text8))
        self.wait(0.5)
        self.play(FadeOut (text8))  


class biliard3(Scene):
    def construct(self):



        table = Polygon(
        [-39, 24.5, 0],
        [-39, -24.5, 0],
        [39, -24.5, 0],
        [39, 24.5, 0],            

            color=YELLOW
        )        

        table.scale(.1)
        self.play( ShowCreation(table))
        self.wait(1)

        text1= TextMobject("49 m ")
        text2= TextMobject("78 m ")

        text1.scale(2)
        text2.scale(2)

        text1.next_to(table,RIGHT,buff=0.5)
        text2.next_to(table,DOWN,buff=0.5)
        self.add( text1,text2)

        self.wait(1)

        dot1=Dot()
        dot2=Dot()
        dot3=Dot()
        dot4=Dot()        


        dot1.move_to([-3.9, 2.45, 0])
        dot2.move_to([-3.9, -2.45, 0])
        dot3.move_to([3.9, 2.45, 0])
        dot4.move_to([3.9, -2.45, 0])

        

        dot1.set_fill(RED, 1)
        dot2.set_fill(RED, 1)
        dot3.set_fill(RED, 1)
        dot4.set_fill(RED, 1)




        self.play( ShowCreation(dot1),ShowCreation(dot2),ShowCreation(dot3),ShowCreation(dot4))

        self.wait(3)

        ball=Dot()
	    
        ball.move_to([-3.9, -2.45, 0])
        ball.set_fill(GREEN, 1)
        ball.scale(3)
        self.play( ShowCreation(ball))
        self.wait(3)

        y=-24.5
        x=-39
        for z in range(1,1000 , 1):

            if x ==-39:
               shiftx=1
            if x ==39:
               shiftx=-1
            if y ==-24.5:
               shifty=1
            if y ==24.5:
               shifty=-1
        	

            line = Line([x/10, y/10, 0],[(x+shiftx)/10, (y+shifty)/10, 0])
            self.add(line)	
        
            x=x+shiftx
            y=y+shifty
            self.wait(0.1)



class biliard4(Scene):

        
    def construct(self):
        table = Polygon(
            [-39, 24.5, 0],
            [-39, -24.5, 0],
            [39, -24.5, 0],
            [39, 24.5, 0],            

            color=YELLOW
        )        

        table.scale(.1)
        self.play( ShowCreation(table))

        text1= TextMobject("49 m ")
        text2= TextMobject("78 m ")

        text1.scale(2)
        text2.scale(2)

        text1.next_to(table,RIGHT,buff=0.5)
        text2.next_to(table,DOWN,buff=0.5)
        self.play( Write(text1),Write(text2))


        dot1=Dot()
        dot2=Dot()
        dot3=Dot()
        dot4=Dot()        


        dot1.move_to([-3.9, 2.45, 0])
        dot2.move_to([-3.9, -2.45, 0])
        dot3.move_to([3.9, 2.45, 0])
        dot4.move_to([3.9, -2.45, 0])

        

        dot1.set_fill(RED, 1)
        dot2.set_fill(RED, 1)
        dot3.set_fill(RED, 1)
        dot4.set_fill(RED, 1)




        self.play( ShowCreation(dot1),ShowCreation(dot2),ShowCreation(dot3),ShowCreation(dot4))




        line = Line([-39/10, -24.5/10, 0],[10/10,24.5/10,0])
        self.play(ShowCreation(line))	
        self.wait(3)

        text3= TexMobject("45^{o}")
        text3.next_to(dot2,RIGHT,buff=0.5)
        text3.shift(0.5*UP)
        self.play( Write (text3))
        self.wait(4)
        self.play( FadeOut (text3))



        text1= TextMobject("(0,0) ")
        text2= TextMobject("(1,1)")
        text3=TextMobject("(49,49)")
        text4=TextMobject("(50,48)")

        dot1=Dot()
        dot2=Dot()
        dot3=Dot()
        dot4=Dot()  


        dot1.move_to([-3.9, -2.45, 0])
        dot2.move_to([-3.8, -2.35, 0])
        dot3.move_to([1, 2.45, 0])
        dot4.move_to([1.1, 2.35, 0])

        

        dot1.set_fill(WHITE, 1)
        dot2.set_fill(WHITE, 1)
        dot3.set_fill(WHITE, 1)
        dot4.set_fill(WHITE, 1)


        text1.next_to(dot1,RIGHT,buff=0.5)
        text2.next_to(dot2,RIGHT,buff=0.5)       
        text3.next_to(dot3,RIGHT,buff=0.5)
        text4.next_to(dot4,RIGHT,buff=0.5)

        self.play(ShowCreation (dot1))
        self.play(Write(text1))
        self.play(FadeOut(text1))
        self.play(ShowCreation (dot2))
        self.play(Write(text2))    
        self.play(FadeOut(text2))

        self.play(ShowCreation (dot3))
        self.play(Write(text3)) 
        self.play(FadeOut(text3))
        self.play(ShowCreation (dot4))
        self.play(Write(text4))
        self.play(FadeOut(text4))

class biliard5(Scene):

    def construct(self):
        text4= TextMobject("(Even,Even) ")
        text4.scale(3)
        self.play(Write (text4))
        self.wait(0.5)
        self.play(FadeOut (text4))
        text8= TextMobject("OR ")
        text8.scale(3)
        self.play(Write (text8))
        self.wait(0.5)
        self.play(FadeOut (text8))  

        text5= TextMobject("(Odd,Odd) ")
        text5.scale(3)
        self.play(Write (text5))
        self.wait(0.5)
        self.play(FadeOut (text5))       

class Grid(VMobject):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        VMobject.__init__(self, **kwargs)

    def generate_points(self):
        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))


class ScreenGrid(VGroup):
    CONFIG = {
        "rows":8,
        "columns":14,
        "height": FRAME_Y_RADIUS*2,
        "width": 14,
        "grid_stroke":0.5,
        "grid_color":WHITE,
        "axis_color":RED,
        "axis_stroke":2,
        "show_points":False,
        "point_radius":0,
        "labels_scale":0.5,
        "labels_buff":0,
        "number_decimals":2
    }

    def __init__(self,**kwargs):
        VGroup.__init__(self,**kwargs)
        rows=self.rows
        columns=self.columns
        grilla=Grid(width=self.width,height=self.height,rows=rows,columns=columns).set_stroke(self.grid_color,self.grid_stroke)

        vector_ii=ORIGIN+np.array((-self.width/2,-self.height/2,0))
        vector_id=ORIGIN+np.array((self.width/2,-self.height/2,0))
        vector_si=ORIGIN+np.array((-self.width/2,self.height/2,0))
        vector_sd=ORIGIN+np.array((self.width/2,self.height/2,0))

        ejes_x=Line(LEFT*self.width/2,RIGHT*self.width/2)
        ejes_y=Line(DOWN*self.height/2,UP*self.height/2)

        ejes=VGroup(ejes_x,ejes_y).set_stroke(self.axis_color,self.axis_stroke)

        divisiones_x=self.width/columns
        divisiones_y=self.height/rows

        direcciones_buff_x=[UP,DOWN]
        direcciones_buff_y=[RIGHT,LEFT]
        dd_buff=[direcciones_buff_x,direcciones_buff_y]
        vectores_inicio_x=[vector_ii,vector_si]
        vectores_inicio_y=[vector_si,vector_sd]
        vectores_inicio=[vectores_inicio_x,vectores_inicio_y]
        tam_buff=[0,0]
        divisiones=[divisiones_x,divisiones_y]
        orientaciones=[RIGHT,DOWN]
        puntos=VGroup()
        leyendas=VGroup()


        for tipo,division,orientacion,coordenada,vi_c,d_buff in zip([columns,rows],divisiones,orientaciones,[0,1],vectores_inicio,dd_buff):
            for i in range(1,tipo):
                for v_i,direcciones_buff in zip(vi_c,d_buff):
                    ubicacion=v_i+orientacion*division*i
                    punto=Dot(ubicacion,radius=self.point_radius)
                    coord=round(punto.get_center()[coordenada],self.number_decimals)
                    leyenda=TextMobject("%s"%coord).scale(self.labels_scale)
                    leyenda.next_to(punto,direcciones_buff,buff=self.labels_buff)
                    puntos.add(punto)
                    leyendas.add(leyenda)

        self.add(grilla,ejes,leyendas)
        if self.show_points==True:
            self.add(puntos)


class biliard6(Scene):
    def construct(self):
        grid=ScreenGrid()
        dot1=Dot()
        self.add(grid)
        self.play(ShowCreation (dot1))
        self.wait(5)

        dot2=Dot()
        dot2.move_to([1, 1, 0])
        dot3=Dot()
        dot3.move_to([1, -1, 0])
        dot4=Dot()
        dot4.move_to([-1, 1, 0])
        dot5=Dot()
        dot5.move_to([-1, -1, 0])        

        self.play(ShowCreation(dot2),ShowCreation(dot3),ShowCreation(dot4),ShowCreation(dot5))
        self.wait(3)

        line1=Line([0, 0, 0],[1, 1, 0])
        line2=Line([0, 0, 0],[-1, 1, 0])
        line3=Line([0, 0, 0],[1, -1, 0])
        line4=Line([0, 0, 0],[-1, -1, 0])
        
        self.play(ShowCreation(line1))
        self.play(ShowCreation(line2))
        self.play(ShowCreation(line3))
        self.play(ShowCreation(line4)) 
        self.wait(3)
        text1=TextMobject("(1,1)")
        text2=TextMobject("(-1,1)")
        text3=TextMobject("(1,-1)")
        text4=TextMobject("(-1,-1)")

        text1.next_to(dot2,UP+RIGHT)
        text2.next_to(dot3,DOWN+RIGHT)
        text3.next_to(dot4,UP+LEFT)
        text4.next_to(dot5,DOWN+LEFT)
        self.play(Write(text1),Write(text2),Write(text3),Write(text4))
        self.wait(10)


class biliard7(Scene):
    def  construct(self):

        table = Polygon(
            [-39, 24.5, 0],
            [-39, -24.5, 0],
            [39, -24.5, 0],
            [39, 24.5, 0],            

            color=YELLOW)
              
        table.scale(.1)
        self.play( ShowCreation(table))

        text1= TextMobject("49 m ")
        text2= TextMobject("78 m ")

        text1.scale(2)
        text2.scale(2)

        text1.next_to(table,RIGHT,buff=0.5)
        text2.next_to(table,DOWN,buff=0.5)
        self.play( Write(text1),Write(text2))


        dot1=Dot()
        dot2=Dot()
        dot3=Dot()
        dot4=Dot()        


        dot2.move_to([-3.9, 2.45, 0])
        dot1.move_to([-3.9, -2.45, 0])
        dot3.move_to([3.9, 2.45, 0])
        dot4.move_to([3.9, -2.45, 0])

        

        dot1.set_fill(RED, 1)
        dot2.set_fill(RED, 1)
        dot3.set_fill(RED, 1)
        dot4.set_fill(RED, 1)




        self.play( ShowCreation(dot1),ShowCreation(dot2),ShowCreation(dot3),ShowCreation(dot4))

        self.wait(5)
        text1=TextMobject("(0,0)")
        text2=TextMobject("(0,49)")
        text3=TextMobject("(78,49)")
        text4=TextMobject("(78,0)")


        text1.next_to(dot1,LEFT+DOWN)
        text2.next_to(dot2,LEFT+UP)
        text3.next_to(dot3,RIGHT+UP)
        text4.next_to(dot4,RIGHT+DOWN)

        self.play(Write(text1))          
        self.wait(2)
        self.play(Write(text2))          
        self.wait(2)
        self.play(Write(text3))          
        self.wait(2)
        self.play(Write(text4))          
        self.wait(2)

        text5=TextMobject("x")
        text5.scale(3)
        text5.set_color(RED)
        text5.move_to(text2)

        self.play(Write(text5))
        self.wait(3)
        text6=TextMobject("x")
        text6.scale(3)
        text6.set_color(RED)
        text6.move_to(text3)

        self.play(Write(text6))
        self.wait(3)
        circle1=Circle()
        circle1.scale(1)
        circle1.set_color(GREEN)
        circle1.move_to(text4)

        self.play(ShowCreation(circle1))
        self.wait(5)