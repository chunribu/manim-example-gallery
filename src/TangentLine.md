# 切线

<video controls loop style="width:100%;">
    <source src=../_static/TangentLineExample.mp4 type="video/mp4"> </source>
</video>

```python
class TangentLineExample(Scene):
    def construct(self):
        circle = Circle(radius=2)
        line_1 = TangentLine(circle, alpha=0.0, length=4, color=BLUE_D) # right
        line_2 = TangentLine(circle, alpha=0.4, length=4, color=GREEN) # top left
        self.add(circle)
        self.play(Create(line_1))
        self.play(Create(line_2))
```

关键词：`TangentLine` `line`