# 条形图

<video controls loop style="width:100%;">
    <source src=../_static/BarChartExample.mp4 type="video/mp4"> </source>
</video>

```python
class BarChartExample(Scene):
    def construct(self):
        chart = BarChart(
            values=[-5, 40, -10, 20, -3],
            bar_names=["one", "two", "three", "four", "five"],
            y_range=[-20, 50, 10],
            y_length=6,
            x_length=10,
            x_axis_config={"font_size": 36},
        )

        c_bar_lbls = chart.get_bar_labels(font_size=48)

        self.play(FadeIn(chart, scale=2))
        self.play(Create(c_bar_lbls))
```

关键词：`Bar` `plot` `graph`