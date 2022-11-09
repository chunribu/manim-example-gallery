# 批量动画

<video controls loop style="width:100%;">
    <source src=../_static/BatchAnimationExample.mp4 type="video/mp4"> </source>
</video>

```python
def shuffle(string):
    '''随机打乱字符串并返回新的字符串'''
    import random
    char_list = list(string)
    random.shuffle(char_list)
    return ''.join(char_list)

class BatchAnimationExample(Scene):
    def construct(self):
        # 批量生成元素
        chars = [
            Text(char, color = utils.color.random_color())
            for _ in range(4) for char in shuffle('MANIM')
        ]
        # 利用VGroup的arrange方法排列对齐
        char_group = VGroup()
        for i in range(4):
            row = VGroup(*chars[i*5:(i+1)*5])
            row.arrange(RIGHT)
            char_group.add(row)
        char_group.arrange(DOWN)
        # 用AnimationGroup管理多个FadeIn动画
        self.play(AnimationGroup(*(
                FadeIn(m, shift=DOWN)
                for m in chars
            ),
            lag_ratio = .5,
            run_time = 5,
        ))
        # 停留1秒
        self.wait()
```

使用`AnimationGroup`管理多个动画，设置`run_time`为总动画时长，`lag_ratio`为相邻两个动画之间的延迟程度，数值可以大于1。

关键词：`batch` `multi` `animation` `AnimationGroup`