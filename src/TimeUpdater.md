# 随时间更新

<video controls loop style="width:100%;">
    <source src=../_static/TimeUpdater.mp4 type="video/mp4"> </source>
</video>

```python
class TimeUpdater(Scene):
    def construct(self):
        def updater_forth(mobj, dt):
            mobj.rotate_about_origin(dt)
        def updater_back(mobj, dt):
            mobj.rotate_about_origin(-dt)
        line_reference = Line(ORIGIN, LEFT).set_color(WHITE)
        line_moving = Line(ORIGIN, LEFT).set_color(YELLOW)
        line_moving.add_updater(updater_forth)
        self.add(line_reference, line_moving)
        self.wait(2)
        line_moving.remove_updater(updater_forth)
        line_moving.add_updater(updater_back)
        self.wait(2)
        line_moving.remove_updater(updater_back)
        self.wait(0.5)
```

当被添加的更新函数包含名为`dt`的参数时，这个更新函数会接收到`dt`（两帧之间的实际间隔时间）。

关键词：`TimeBased` `Updater` `rotate`