# 图象阴影

<video controls loop style="width:100%;">
    <source src=../_static/GraphArea.mp4 type="video/mp4"> </source>
</video>

```python
class GraphArea(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5],
            y_range=[0, 6],
            x_axis_config={"numbers_to_include": [2, 3]},
            tips=False,
        )

        labels = ax.get_axis_labels()

        curve_1 = ax.plot(lambda x: 4 * x - x ** 2, x_range=[0, 4], color=BLUE_C)
        curve_2 = ax.plot(
            lambda x: 0.8 * x ** 2 - 3 * x + 4,
            x_range=[0, 4],
            color=GREEN_B,
        )

        line_1 = ax.get_vertical_line(ax.i2gp(2, curve_1), color=YELLOW)
        line_2 = ax.get_vertical_line(ax.i2gp(3, curve_1), color=YELLOW)

        area = ax.get_area(curve_2, [2, 3], bounded_graph=curve_1, color=GREY, opacity=0.5)

        self.play(Create(ax), Write(labels))
        self.play(Create(curve_1), Create(curve_2))
        self.play(Create(line_1), Create(line_2))
        self.play(Create(area))
        self.wait()
```

关键词：`area` `plot` `function`