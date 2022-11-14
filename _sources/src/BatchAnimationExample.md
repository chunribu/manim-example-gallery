# 批量动画

<video controls loop style="width:100%;">
    <source src=../_static/TestScene.mp4 type="video/mp4"> </source>
</video>

```python
def shuffle(string):
    '''随机打乱字符串并返回新的字符串'''
    import random
    char_list = list(string)
    random.shuffle(char_list)
    return ''.join(char_list)

class TestScene(Scene):
    def construct(self):
        # 生成20个字符
        chars = VGroup(*(
            Text(char, color = utils.color.random_color())
            for _ in range(4) for char in shuffle('MANIM')
        ))
        # 网格排列（4行5列）
        chars.arrange_in_grid(rows=4)

        # 用AnimationGroup管理多个FadeIn动画
        self.play(AnimationGroup(
            *(FadeIn(m, shift=DOWN) for m in chars),
            lag_ratio = .3,
        ))
        self.wait()
```

使用`AnimationGroup`管理多个动画，`lag_ratio`为相邻两个动画之间的延迟程度，数值可以大于1。

关键词：`batch` `multi` `animation` `AnimationGroup`