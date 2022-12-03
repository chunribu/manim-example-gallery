# 函数图象变换

<video controls loop style="width:100%;">
    <source src=../_static/GraphTransform.mp4 type="video/mp4"> </source>
</video>

```python
class GraphTransform(Scene):
    def construct(self):
        ax = Axes()
        curve1 = ax.plot(lambda x: .1 * x**2, color=TEAL)
        
        curve2 = ax.plot(lambda x: 0, color=TEAL)

        part1 = ax.plot(lambda x: -2, x_range=[-7,0])
        part2 = ax.plot(lambda x: 2, x_range=[0,7])
        curve3 = VGroup().set_points(np.vstack((
            part1.get_all_points(), 
            part2.get_all_points()
        ))).set_color(TEAL)

        self.add(ax)
        self.play(Create(curve1, run_time=2))
        self.play(ReplacementTransform(curve1, curve2))
        self.play(ReplacementTransform(curve2, curve3))
```

关键词：`FunctionGraph` `Transform`