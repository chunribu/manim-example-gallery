# 电路图

<video controls loop style="width:100%;">
    <source src=../_static/Circuit.mp4 type="video/mp4"> </source>
</video>

```python
class Circuit(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{circuitikz}")

        c = MathTex(
            r'''\draw 
                (0,2)   to[battery1]      (0,0)
                (0,2)   --                (2,2)
                (2,2)   to[R=\(R_1\)]     (2,0)
                (2,2)   --                (4,2)
                (4,2)   to[rmeter, t=V]   (4,0)
                (4,0)   --                (2,0)
                (2,0)   to[rmeter, t=A]   (0,0);
            ''',
            stroke_width=4,
            fill_opacity=0,
            stroke_opacity=1,
            tex_environment="circuitikz",
            tex_template=template,
        )

        self.play(Write(c, run_time=3))
        self.wait()
```

关键词：`TexTemplate` `Latex` `Physics`