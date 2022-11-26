# 数轴

<video controls loop style="width:100%;">
    <source src=../_static/NumberLineExample.mp4 type="video/mp4"> </source>
</video>

```python
class NumberLineExample(Scene):
    def construct(self):
        nl = NumberLine(
            x_range=[-10, 10, 2],
            length=10,
            color=BLUE,
            include_numbers=True,
        )
        self.play(Create(nl))
        self.wait()
```

关键词：`NumberLine` `axis`