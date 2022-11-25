# 直角

<video controls loop style="width:100%;">
    <source src=../_static/RightAngleExample.mp4 type="video/mp4"> </source>
</video>

```python
class RightAngleExample(Scene):
    def construct(self):
        elbow = Elbow(width=2.0)

        line1 = Line( LEFT, RIGHT )
        line2 = Line( DOWN, UP )
        rightangle = RightAngle(line1, line2)
        plot = VGroup(line1, line2, rightangle)

        _ = Group(elbow, plot).arrange(buff=1)
        self.play(Create(elbow))
        self.play(Create(plot))
        self.wait()
```

关键词：`Elbow` `RightAngle` `geometry`