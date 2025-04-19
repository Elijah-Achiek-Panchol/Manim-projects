from manim import *
import numpy as np

class BloodySouthSudanFlag(Scene):
    def construct(self):
        # White background
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
        )

        # Blue triangle
        triangle = Polygon(
            [-flag_width/2, total_height/2, 0],
            [-flag_width/2, -total_height/2, 0],
            [-flag_width/2 + total_height*0.8, 0, 0]
        ).set_fill(BLUE, 1)

        # Yellow star
        star = Star(5, outer_radius=0.35*scale_factor, inner_radius=0.15*scale_factor
                  ).set_fill(YELLOW, 1).move_to([-flag_width/2 + total_height*0.35, 0, 0])

        # Group all flag elements
        flag = VGroup(stripes, triangle, star).scale(scale_factor)
        self.add(flag)

        # Blood drip animation class
        class BloodDrip(VMobject):
            def __init__(self, start_point):
                super().__init__()
                self.start_point = start_point
                self.set_points_as_corners([start_point, start_point])
                self.set_stroke(RED_D, width=5)
                
            def update_drip(self, dt):
                new_point = self.get_end() + DOWN * dt * 2
                self.add_points_as_corners([new_point])
                
                # Reset if below screen
                if self.get_end()[1] < -config.frame_height/2:
                    self.set_points_as_corners([self.start_point])

        # Create drip sources along black and red stripes
        drip_sources = [
            flag.get_top() + RIGHT * x * 0.2 
            for x in np.linspace(-2.5, 2.5, 15)
        ]
        drips = VGroup(*[BloodDrip(point) for point in drip_sources])
        self.add(drips)

        # Add updaters for animation
        for drip in drips:
            drip.add_updater(lambda m, dt: m.update_drip(dt))

        # Blood pool formation
        blood_pool = Circle(radius=0.3, fill_opacity=0.7
                          ).set_fill(RED_E).next_to(flag, DOWN, buff=0)
        blood_pool.save_state()
        blood_pool.scale(0.1).set_opacity(0)

        # Title text
        title = Text("South Sudan! We love and cherish you", font_size=36, color=BLACK
                   ).next_to(flag, DOWN, buff=1.5)
        self.add(title)

        # Animation sequence
        self.wait(1)
        self.play(
            Restore(blood_pool),
            rate_func=there_and_back,
            run_time=4
        )
        self.wait(3)
