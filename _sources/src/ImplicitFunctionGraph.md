# 隐函数图象

<video controls loop style="width:100%;">
    <source src=../_static/ImplicitFunctionGraph.mp4 type="video/mp4"> </source>
</video>

```python
class ImplicitFunctionGraph(Scene):
    def construct(self):
        ax = Axes()
        graph = ax.plot_implicit_curve(
            lambda x, y: y**2 + 2 * x,
            color=RED
        )
        self.add(ax)
        self.play(Create(graph))
        self.wait()
```

这里的`lambda x, y: y**2 + 2 * x`表示`F(x, y) = y^2 + 2x = 0`。

关键词：`ImplicitFunction` `plot`