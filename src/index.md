# 首页 <img src="../_images/meg.png" align=right />

<video controls autoplay loop style="width:100%;">
    <source src=../_static/DarkThemeBanner.mp4 type="video/mp4"> </source>
</video>

```python
class DarkThemeBanner(Scene):
    def construct(self):
        banner = ManimBanner()
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))
```
