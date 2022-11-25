# 椭圆

<video controls loop style="width:100%;">
    <source src=../_static/EllipseExample.mp4 type="video/mp4"> </source>
</video>

```python
class EllipseExample(Scene):
    def construct(self):
        ellipse_1 = Ellipse(width=2.0, height=4.0, color=BLUE_B)
        ellipse_2 = Ellipse(width=4.0, height=1.0, color=BLUE_D)
        ellipse_group = Group(ellipse_1,ellipse_2).arrange(buff=1)
        self.play(Create(ellipse_1))
        self.play(Create(ellipse_2))
```

关键词： `Ellipse` `geometry`