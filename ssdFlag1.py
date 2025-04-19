from manim import *

class SouthSudanFlag(Scene):
    def construct(self):
        # Set background color to white
        self.camera.background_color = WHITE

        # Flag dimensions
        flag_width = 6
        flag_height = 3

        # Define stripe heights
        main_stripe_height = flag_height / 3.5
        white_stripe_height = main_stripe_height / 2

        # Total height calculation
        total_height = (
            3 * main_stripe_height + 2 * white_stripe_height
        )
        scale_factor = flag_height / total_height

        # Draw stripes
        black_stripe = Rectangle(
            width=flag_width,
            height=main_stripe_height
        ).set_fill(BLACK, 1).set_stroke(width=0)
        black_stripe.shift(UP * (main_stripe_height + white_stripe_height))

        white_stripe1 = Rectangle(
            width=flag_width,
            height=white_stripe_height
        ).set_fill(WHITE, 1).set_stroke(width=0)
        white_stripe1.shift(UP * (main_stripe_height/2 + white_stripe_height/2))

        red_stripe = Rectangle(
            width=flag_width,
            height=main_stripe_height
        ).set_fill(RED, 1).set_stroke(width=0)
        
        white_stripe2 = Rectangle(
            width=flag_width,
            height=white_stripe_height
        ).set_fill(WHITE, 1).set_stroke(width=0)
        white_stripe2.shift(DOWN * (main_stripe_height/2 + white_stripe_height/2))

        green_stripe = Rectangle(
            width=flag_width,
            height=main_stripe_height
        ).set_fill(GREEN, 1).set_stroke(width=0)
        green_stripe.shift(DOWN * (main_stripe_height + white_stripe_height))

        # Blue triangle
        triangle = Polygon(
            [-flag_width/2, total_height/2, 0],
            [-flag_width/2, -total_height/2, 0],
            [-flag_width/2 + total_height * 0.8, 0, 0]
        ).set_fill(BLUE, 1).set_stroke(width=0)

        # Yellow star
        star = Star(
            n=5,
            outer_radius=0.35 * scale_factor,
            inner_radius=0.15 * scale_factor
        ).set_fill(YELLOW, 1).set_stroke(width=0)
        star.move_to([-flag_width/2 + total_height * 0.35, 0, 0])

        # Scale all elements
        group = Group(
            black_stripe,
            white_stripe1,
            red_stripe,
            white_stripe2,
            green_stripe,
            triangle,
            star
        ).scale(scale_factor)

        self.add(group)
