# 函数图象

<video controls loop style="width:100%;">
    <source src=../_static/FunctionGraph.mp4 type="video/mp4"> </source>
</video>

```python
class FunctionGraph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": BLUE},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        cos_graph = axes.plot(lambda x: np.cos(x), color=RED)

        cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)")

        vert_line = axes.get_vertical_line(
            axes.i2gp(TAU, cos_graph), color=YELLOW, line_func=Line
        )
        line_label = axes.get_graph_label(
            cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
        )

        labels = VGroup(axes_labels, cos_label, line_label)
        
        self.play(Create(axes))
        self.play(Create(cos_graph, run_time=2))
        self.play(Create(vert_line))
        self.play(Write(labels))
        self.wait()
```

`i2gp`: input to graph; `TAU`: 2*PI; `UR`: Upper Right

关键词：`Function` `Graph` `draw` `plot`