# 首页 <img src="../_images/meg.png" align=right />

欢迎🎉🎉🎉这里收集了一些Manim动画的示例代码，希望对你有帮助。

我们的QQ群（Manim开放互助组：166957758）建好了，欢迎加入参与讨论，无论是求助、助人还是经验分享，我们都欢迎。

如果你遇到好的Manim代码片段，请你提交到[GitHub](https://github.com/chunribu/manim-example-gallery/)，也可以发到我的[邮箱](mailto://jianjiang.bio@gmail.com)，不久后会合并到这个合集里，与所有感兴趣的小伙伴一起分享。

---

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
