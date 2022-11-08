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

`TracedPath`用于追踪点的轨迹。接收一个函数，用于获取坐标。可以传入消散时间，轨迹会在一段时间后消散。例子中设置`stroke_opacity`为非单一数值，得到渐变效果。

关键词：`trace` `path` `animation`
