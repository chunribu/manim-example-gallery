# 全屏

<video controls loop style="width:100%;">
    <source src=../_static/FullScreenRectangleExample.mp4 type="video/mp4"> </source>
</video>

```python
class FullScreenRectangleExample(Scene):
    def construct(self):
        bg = FullScreenRectangle(fill_opacity=1)
        self.play(FadeIn(bg))
```

关键词：`FullScreen` `background`