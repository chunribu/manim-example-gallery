# 显示运动轨迹

<video controls loop style="width:100%;">
    <source src=../_static/DissipatingPathExample.mp4 type="video/mp4"> </source>
</video>

```python
class DissipatingPathExample(Scene):
    def construct(self):
        a = Dot(RIGHT * 2)
        b = TracedPath(a.get_center, dissipating_time=0.5, stroke_opacity=[0, 1])
        self.add(a, b)
        self.play(a.animate(path_arc=PI / 4).shift(LEFT * 2))
        self.play(a.animate(path_arc=-PI / 4).shift(LEFT * 2))
        self.wait()
```

这是一段描述。

关键词：`kw1` `kw2`
