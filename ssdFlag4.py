from manim import *
import numpy as np

class HeartSouthSudanFlag(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Flag components
        flag_width = 6
        flag_height = 3
        main_stripe_height = flag_height / 3.5
        white_stripe_height = main_stripe_height / 2
        total_height = 3 * main_stripe_height + 2 * white_stripe_height
        scale_factor = flag_height / total_height

        # Create flag stripes
        black_stripe = Rectangle(width=flag_width, height=main_stripe_height).set_fill(BLACK, 1)
        white_stripe1 = Rectangle(width=flag_width, height=white_stripe_height).set_fill(WHITE, 1)
        red_stripe = Rectangle(width=flag_width, height=main_stripe_height).set_fill(RED, 1)
        white_stripe2 = Rectangle(width=flag_width, height=white_stripe_height).set_fill(WHITE, 1)
        green_stripe = Rectangle(width=flag_width, height=main_stripe_height).set_fill(GREEN, 1)

        # Position stripes
        stripes = VGroup(
            black_stripe.shift(UP*(main_stripe_height + white_stripe_height)),
            white_stripe1.shift(UP*(main_stripe_height/2 + white_stripe_height/2)),
            red_stripe,
            white_stripe2.shift(DOWN*(main_stripe_height/2 + white_stripe_height/2)),
            green_stripe.shift(DOWN*(main_stripe_height + white_stripe_height))
        ).scale(scale_factor)

        # Blue triangle and star
        triangle = Polygon(
            [-flag_width/2, total_height/2, 0],
            [-flag_width/2, -total_height/2, 0],
            [-flag_width/2 + total_height*0.8, 0, 0]
        ).set_fill(BLUE, 1).scale(scale_factor)

        star = Star(5, outer_radius=0.35*scale_factor, inner_radius=0.15*scale_factor
                  ).set_fill(YELLOW, 1).move_to([-flag_width/2 + total_height*0.35, 0, 0]).scale(scale_factor)

        # Final flag group
        flag = VGroup(stripes, triangle, star)
        self.add(flag)

        # Title text
        title = Text("South Sudan! We love and cherish you", font_size=36, color=BLACK)
        
        # Mathematical heart
        heart = ParametricFunction(
            lambda t: np.array([
                16 * np.sin(t)**3,
                13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t),
                0
            ]),
            t_range=[0, 2*PI]
        ).scale(0.03).set_color(RED).next_to(flag, DOWN, buff=0.8)
        
        title.next_to(heart, DOWN, buff=0.3)
        self.add(title, heart)

        # Beating animation
        def beat(mob, alpha):
            scale = 1 + 0.2 * np.sin(2 * PI * alpha)
            mob.become(ParametricFunction(
                lambda t: np.array([
                    16 * np.sin(t)**3,
                    13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t),
                    0
                ]),
                t_range=[0, 2*PI]
            ).scale(0.03 * scale).set_color(RED).next_to(flag, DOWN, buff=0.8))
            
        self.play(
            UpdateFromAlphaFunc(
                heart,
                beat,
                rate_func=there_and_back,
                run_time=1.5
            )
        )
        self.wait(0.5)
        
        # Continuous beating
        self.play(
            UpdateFromAlphaFunc(
                heart,
                beat,
                rate_func=there_and_back,
                run_time=1.5
            )
        )
        self.play(
            UpdateFromAlphaFunc(
                heart,
                beat,
                rate_func=there_and_back,
                run_time=1.2
            )
        )
        self.wait(2)
