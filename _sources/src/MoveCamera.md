# 镜头移动

<video controls loop style="width:100%;">
    <source src=../_static/MoveCamera.mp4 type="video/mp4"> </source>
</video>

```python
class MoveCamera(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=(-0.1, 4.25), y_range=(-1.5, 1.5), z_range=(-1.5, 1.5), y_length=5, z_length=5)
        func = lambda p: axes.coords_to_point(p, np.exp(complex(0, PI*p)).real, np.exp(complex(0, PI*p)).imag)
        
        curve = ParametricFunction(
            func,
            t_range=(0, 2, 0.1)
        )
        curve_extension = ParametricFunction(
            func,
            t_range=(2, 4, 0.1)
        )

        self.set_camera_orientation(phi=90*DEGREES, theta=0*DEGREES, focal_distance=10000)
        self.add(axes)
        self.play(Create(curve, run_time=2))
        self.wait()
        self.move_camera(phi=130*DEGREES, theta=-60*DEGREES, focal_distance=10000)
        self.wait()
        self.play(Create(curve_extension, run_time=2))
        self.wait()
        self.move_camera(phi=90*DEGREES, theta=-90*DEGREES, focal_distance=10000)
        self.wait()
```

关键词：`Camera` `ChangeAngle`