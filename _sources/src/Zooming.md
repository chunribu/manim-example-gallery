# 镜头缩放

<video controls loop style="width:100%;">
    <source src=../_static/Zooming.mp4 type="video/mp4"> </source>
</video>

```python
class Zooming(MovingCameraScene):
    def construct(self):
        text=MathTex(r"\nabla\textbf{u}").scale(3)
        square=Square()
        VGroup(text,square).arrange(RIGHT, buff=3)

        self.add(text,square)
        self.camera.frame.save_state()

        self.play(
            self.camera.auto_zoom(text, margin=1)
        )
        self.wait()
        self.play(Restore(self.camera.frame))

        self.play(
            self.camera.auto_zoom(square, margin=1)
        )
        self.wait()
        self.play(Restore(self.camera.frame))

```

关键词：`Camera` `Zoom` `zoom in`