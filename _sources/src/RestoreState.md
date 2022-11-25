# 恢复原样

<video controls loop style="width:100%;">
    <source src=../_static/RestoreExample.mp4 type="video/mp4"> </source>
</video>

```python
class RestoreExample(Scene):
    def construct(self):
        s = Square()
        s.save_state()
        self.play(FadeIn(s))
        self.play(s.animate.set_color(PURPLE).set_opacity(0.5).shift(2*LEFT).scale(3))
        self.play(s.animate.shift(5*DOWN).rotate(PI/4))
        self.wait()
        self.play(Restore(s), run_time=2)
```

`save_state`方法用于记录当下状态。`Restore`动画将s恢复为之前记录的状态，等同于`s.animate.restore()`。

关键词：`state` `restore` `animation`