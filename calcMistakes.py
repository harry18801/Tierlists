from manim import *


class AnimateMathExpression(Scene):
    def construct(self):
        # Define each piece of the equation incrementally
        part1 = MathTex(r"\frac{d}{dx}")  # First part: derivative operator
        part2 = MathTex(r"\bigg(")  # Opening parenthesis

        # Full fraction combining numerator and denominator
        fraction = MathTex(
            r"\frac{\ln(e^\pi) + \sqrt{\arctan\left(6.02 \cdot 10^{23}\right)}}"
            r"{e^{e^{e^e}}! + \sqrt[\pi]{\pi}\hbar\zeta(2) - \cos\left(\frac{\pi}{\ln(2)}\right)}"
        )

        part4 = MathTex(r"\bigg)")  # Closing parenthesis
        equals_zero = MathTex(r"= 0")  # Equality

        # Combine all parts into a single expression
        full_expression = VGroup(part1, part2, fraction, part4).arrange(RIGHT)

        # Step-by-step animation
        self.play(Write(part1))  # Animate d/dx
        self.wait(1)

        self.play(Write(part2))  # Animate opening parenthesis
        self.wait(1)

        self.play(Write(fraction))  # Animate the fraction
        self.wait(1)

        self.play(Write(part4))  # Animate closing parenthesis
        self.wait(5)

        # Add = 0 at the end
        full_expression_with_zero = VGroup(full_expression, equals_zero).arrange(DOWN)
        self.play(Write(equals_zero))
        self.wait(2)


########################################


class ProductRuleProof(Scene):
    def construct(self):
        # Title
        title = Text("Proof of the Product Rule", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # step 0: limit definition
        definition = MathTex(r"f'(x) = \lim_{h \to 0} \frac{f(x+h) -f(x)}{h}").move_to(
            ORIGIN
        )
        self.play(Write(definition))
        self.wait(3)
        self.play(FadeOut(definition))

        product_rule = MathTex(
            r"\frac{d}{dx}[f(x) g(x)] = \lim_{h \to 0} \frac{f(x+h) g(x+h) - f(x) g(x)}{h}",
            font_size=36,
        ).next_to(title, DOWN, buff=0.5)

        # Display the equation
        self.play(Write(product_rule))
        self.wait(2)

        product_rule2 = MathTex(
            r"= \lim_{h \to 0} \frac{f(x+h)g(x+h) - f(x+h)g(x) + f(x+h)g(x) - f(x)g(x)}{h}",
            font_size=36,
        ).next_to(product_rule, DOWN, buff=0.5)

        # Display the equation
        self.play(Write(product_rule2))
        self.wait(5)

        product_rule3 = MathTex(
            r"= \lim_{h \to 0} \frac{f(x+h)[g(x+h) -g(x)] + g(x) [f(x+h) -f(x)]}{h}",
            font_size=36,
        ).next_to(product_rule2, DOWN, buff=0.5)

        # Display the equation
        self.play(Write(product_rule3))
        self.wait(5)

        product_rule4 = MathTex(
            r"= \lim_{h \to 0} f(x+h) \frac{g(x+h) -g(x)}{h} + \lim_{h \to 0} g(x) \frac{f(x+h)-f(x)}{h}",
            font_size=36,
        )

        # Display product_rule3
        self.play(ReplacementTransform(product_rule3, product_rule4))
        self.wait(4)

        product_rule5 = MathTex(
            r"= \lim_{h \to 0} f(x+h) \lim_{h \to 0} \left(\frac{g(x+h) -g(x)}{h}\right) + \lim_{h \to 0} g(x) \lim_{h \to 0} \left(\frac{f(x+h)-f(x)}{h}\right)",
            font_size=36,
        ).next_to(product_rule4, DOWN, buff=0.5)

        self.play(Write(product_rule5))
        self.wait(5)

        product_rule6 = MathTex(r"f(x)g'(x) + g(x)f'(x)", font_size=36).next_to(
            product_rule5, DOWN, buff=0.5
        )
        self.play(Write(product_rule6))
        self.wait(5)


class AntiderivativeGraph(Scene):
    def construct(self):
        # Set up axes
        axes = Axes(
            x_range=[-4, 4],
            y_range=[-5, 10],
            axis_config={"color": WHITE},
        )

        # Label axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")

        # Define the function f(x) = x and its antiderivative F(x) = x^2/2 + C
        F_graph = axes.plot(lambda x: x**2 / 2, color=YELLOW)

        # Display the axes, labels, and the function graph
        self.play(Create(axes), Write(x_label), Write(y_label))

        # Label the function graph
        integral_text = MathTex(r"\int x \, dx = \frac{x^2}{2} + C").to_edge(
            UP + LEFT * 2
        )
        self.play(Write(integral_text))
        self.wait(1)

        # Animate the family of solutions by moving the graph up and down
        self.play(FadeIn(F_graph))  # First display the initial graph

        # Animate the graph shifting vertically (simulating different C values)
        for C_value in [0, -4, -1, 3, 5]:
            shifted_graph = axes.plot(lambda x: x**2 / 2 + C_value, color=GREEN)
            self.play(
                Transform(F_graph, shifted_graph)
            )  # Smooth transition to the new graph
            self.wait(1)

        # Final pause to end the scene
        self.wait(2)
        self.play(FadeOut(axes, integral_text, F_graph, x_label, y_label))


class USubstitution(Scene):
    def construct(self):
        # Create the integral equation before substitution
        integral_left = MathTex(r"\int_a^b f(g(x)) g'(x) \, dx", font_size=48)
        integral_left.move_to(ORIGIN + UP)  # Center it at the origin

        # Create the integral equation after substitution
        integral_right = MathTex(r"\int_{u(a)}^{u(b)} f(u) \, du", font_size=48)
        integral_right.next_to(
            integral_left, DOWN, buff=1
        )  # Position it below the first integral

        # Create an arrow between the two integrals
        arrow = Arrow(
            start=integral_left.get_bottom(), end=integral_right.get_top(), buff=0.1
        )

        # Create labels for the substitution (u(x) and the boundaries)
        u_substitution_text = MathTex(r"u = g(x)", font_size=36)
        u_substitution_text.next_to(
            integral_left, LEFT, buff=1
        )  # Position it to the left of the first integral

        # Display the initial equation (before substitution)
        self.play(Write(integral_left))
        self.wait(1)

        # Display the substitution label
        self.play(Write(u_substitution_text))
        self.wait(1)

        # Animate the arrow pointing from the left integral to the right integral
        self.play(GrowArrow(arrow))
        self.wait(1)

        # Display the final equation (after substitution)
        self.play(Write(integral_right))
        self.wait(2)

        # Fade everything out
        self.play(FadeOut(integral_left, integral_right, u_substitution_text, arrow))


class LHospitalsRuleConditions(Scene):
    def construct(self):
        # Create the bulleted list for the conditions of L'Hopital's Rule
        blist = BulletedList(
            r"$\lim_{x \to c} \frac{f(x)}{g(x)} \text{ yields an indeterminate form such as } \frac{0}{0} \text{ or } \frac{\infty}{\infty}$",
            r"$f(x) \text{ and } g(x) \text{ are differentiable at } x = c$",
            r"$\text{The denominator, } g'(x) \neq 0, \text{ cannot divide by } 0$",
            r"$\lim_{x \to c} \frac{f'(x)}{g'(x)} \text{ exists}$",
            height=3,
            width=8,
        )
        # Position the bullet list in the center of the screen
        blist.move_to(ORIGIN)

        # Display each item in the list one at a time
        self.play(Write(blist[0]))
        self.wait(2)
        self.play(Write(blist[1]))
        self.wait(2)
        self.play(Write(blist[2]))
        self.wait(2)
        self.play(Write(blist[3]))
        self.wait(4)

        # Fade out everything at the end
        self.play(FadeOut(blist))


class IntegralComparisons(Scene):
    def construct(self):
        # Create the integrals as MathTex objects
        integral_1 = MathTex(r"\int \frac{1}{x^2 + 1} \, dx", font_size=72)
        integral_2 = MathTex(r"\int \frac{1}{x^3 + 1} \, dx", font_size=72)
        integral_3 = MathTex(r"\int e^{-x} \, dx", font_size=72)
        integral_4 = MathTex(r"\int x e^{-x^2} \, dx", font_size=72)
        integral_5 = MathTex(r"\int e^{-x^2} \, dx", font_size=72)
        integral_6 = MathTex(r"\int \frac{\sin(x)}{x} \, dx", font_size=64)
        integral_7 = MathTex(r"\int \sin(x^2) \, dx", font_size=64)
        integral_8 = MathTex(r"\int \ln(\sin(x)) \, dx", font_size=64)

        # Initially position the integrals at the origin (center of the screen)
        integral_1.move_to(ORIGIN)
        integral_2.move_to(ORIGIN)
        integral_3.move_to(ORIGIN)
        integral_4.move_to(ORIGIN)
        integral_5.move_to(ORIGIN)
        integral_6.move_to(ORIGIN)
        integral_7.move_to(ORIGIN)
        integral_8.move_to(ORIGIN)

        # Fade in and animate the integrals
        self.play(FadeIn(integral_1))
        self.play(integral_1.animate.shift(LEFT * 4))  # Move left
        self.wait(1)

        self.play(FadeIn(integral_2))
        self.play(integral_2.animate.shift(RIGHT * 4))  # Move right
        self.wait(2)

        # Fade out the first pair and transition to the next group
        self.play(FadeOut(integral_1), FadeOut(integral_2))

        self.play(FadeIn(integral_3))
        self.play(integral_3.animate.shift(LEFT * 4))  # Move left
        self.wait(1)

        self.play(FadeIn(integral_4))
        self.play(integral_4.animate.shift(RIGHT * 4))  # Move right
        self.wait(2)

        self.play(FadeIn(integral_5))
        self.wait(2)

        # Fade out the third integral and transition to the next group
        # Fade out the second pair and transition to the next group
        self.play(FadeOut(integral_3), FadeOut(integral_4), FadeOut(integral_5))

        # Display the last set of integrals and animate them moving left and right
        self.play(FadeIn(integral_6))
        self.play(integral_6.animate.shift(LEFT * 4.5))  # Move left
        self.wait(1)

        self.play(FadeIn(integral_7))
        self.play(integral_7.animate.shift(RIGHT * 4.5))  # Move right
        self.wait(1)

        self.play(FadeIn(integral_8))
        self.wait(3)

        # Fade out everything at the end
        self.play(FadeOut(integral_6), FadeOut(integral_7), FadeOut(integral_8))


class AbsoluteValueGraph(Scene):
    def construct(self):
        # Axes for |x| in the top half
        top_axes = Axes(
            x_range=[-3, 3, 1], y_range=[-1, 3, 1], x_length=6, y_length=3, tips=False
        ).to_edge(UP)

        # Graph of |x|
        abs_graph = top_axes.plot(lambda x: abs(x), color=BLUE)

        abs_function = MathTex(r"f(x) = |x|", font_size=36).next_to(
            top_axes, LEFT, buff=1
        )

        # Add a circle at x=0
        circle = Circle(radius=0.1, color=RED).move_to(top_axes.c2p(0, 0))

        # Arrow and text for "NOT DIFFERENTIABLE!!"
        arrow = Arrow(
            start=top_axes.c2p(2, 2), end=top_axes.c2p(0, 0), buff=0.1, color=WHITE
        )
        text = Text("NOT DIFFERENTIABLE!!", color=RED, font_size=24).next_to(
            arrow, RIGHT
        )

        # Axes for f'(x) in the bottom half
        bottom_axes = Axes(
            x_range=[-3, 3, 1], y_range=[-2, 2, 1], x_length=6, y_length=3, tips=False
        ).to_edge(DOWN)

        abs_function_prime = MathTex(r"f'(x)", font_size=36).next_to(
            bottom_axes, LEFT, buff=1
        )
        # Show f'(x) as a discontinuous function (-1 for x < 0, 1 for x > 0)
        left_graph = bottom_axes.plot(
            lambda x: -1 if x < 0 else 0, x_range=[-3, -0.01], color=GREEN
        )
        right_graph = bottom_axes.plot(
            lambda x: 1 if x >= 0 else 0, x_range=[0.01, 3], color=GREEN
        )

        # Yellow dots approaching x=0 from both sides
        left_dot = Dot(point=bottom_axes.c2p(-2, -1), color=YELLOW)
        right_dot = Dot(point=bottom_axes.c2p(2, 1), color=YELLOW)

        # Animations
        self.play(Create(top_axes), Create(bottom_axes))
        self.play(Create(abs_graph))
        self.play(Write(abs_function))
        self.play(Create(circle), Create(arrow), Write(text))

        self.wait(3)

        self.play(Create(left_graph), Create(right_graph))
        self.play(Write(abs_function_prime))
        self.wait(2)
        self.play(FadeIn(left_dot), FadeIn(right_dot))

        # Animate the yellow dots moving toward x=0
        self.play(
            left_dot.animate.move_to(bottom_axes.c2p(-0.01, -1)),
            right_dot.animate.move_to(bottom_axes.c2p(0.01, 1)),
            run_time=3,
        )

        # Add text that the limit does not exist
        limit_text = Text("Limit does NOT exist!!", color=YELLOW, font_size=24).next_to(
            bottom_axes, RIGHT, buff=0.5
        )
        self.play(Write(limit_text))

        self.wait(3)


class IntegralTransform(Scene):
    def construct(self):
        # Create the initial integral expressions
        ln_integral = MathTex(r"\int \ln(x) \, dx", font_size=48).to_edge(LEFT * 3)
        arctan_integral = MathTex(r"\int \arctan(x) \, dx", font_size=48).to_edge(
            RIGHT * 3
        )

        # Display the initial integrals
        self.play(Write(ln_integral), Write(arctan_integral))
        self.wait(4)

        # Create the transformed integral expressions with 1* included
        ln_integral_transformed = MathTex(
            r"\int 1 \cdot \ln(x) \, dx", font_size=48, substrings_to_isolate="1"
        ).to_edge(LEFT * 3)
        arctan_integral_transformed = MathTex(
            r"\int 1 \cdot \arctan(x) \, dx",
            font_size=48,
            substrings_to_isolate="1",
        ).to_edge(RIGHT * 3)

        # Color the "1" in orange
        ln_integral_transformed.set_color_by_tex("1", ORANGE)
        arctan_integral_transformed.set_color_by_tex("1", ORANGE)

        # Transform the initial integrals into the transformed integrals
        self.play(Transform(ln_integral, ln_integral_transformed))
        self.play(Transform(arctan_integral, arctan_integral_transformed))
        self.wait(2)
