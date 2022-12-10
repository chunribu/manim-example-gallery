import os
import re
import glob
import shutil
import argparse


def match_code_blocks(from_):
    pattern = r'::video::\n```.*?\n(.*?)```\n'
    return re.findall(pattern, from_, flags=re.DOTALL)

def match_scene_name(from_):
    return re.search(r'class (\w+)\(\w*Scene\)', from_).group(1)

def video_tag(cls_name):
    template = '''<video controls loop style="width:100%;">
    <source src={src} type="video/mp4"> </source>
</video>
'''
    video_path = '../_static/' + cls_name + '.mp4'
    return template.format(src=video_path)

def search_md_files():
    return [i for i in os.listdir('src/') if i.endswith('.md')]

def exec_code(code):
    header = '''from manim import *

'''
    cls_name = match_scene_name(code)
    fname = '.' + cls_name + '.py'
    with open(fname, 'w', encoding='UTF-8') as f:
        f.write(header + code)
    os.system(f'manim {fname} {cls_name}')
    shutil.move(f'media/videos/.{cls_name}/1080p60/{cls_name}.mp4',
                f'_static/{cls_name}.mp4')

def clean_all():
    shutil.rmtree('media/', ignore_errors=True)
    for f in glob.glob('.*.py'):
        os.remove(f)

def render(args):
    if args.file:
        markdown_files = args.file
    else:
        markdown_files = search_md_files()
    src_dir = 'src/'
    for fname in markdown_files:
        fpath = src_dir + fname
        with open(fpath, 'r+', encoding='UTF-8') as f:
            content = f.read()
            f.seek(0)
            code_blocks_to_execute = match_code_blocks(content)
            for code_block in code_blocks_to_execute:
                scene_name = match_scene_name(code_block)
                content = content.replace('::video::', video_tag(scene_name), 1)
                exec_code(code_block)
            f.write(content)
            f.truncate()

def inst_dev_reqs():
    os.system('pip install -r requirements.txt')

def build():
    os.system('jb build . --all')

def deploy():
    os.system('ghp-import -n -p -f _build/html')

def parse_args():
    parser = argparse.ArgumentParser('Manim-Example-Gallery Manager')
    parser.add_argument('-f', '--file', nargs='*',
                        help='需要插入视频的Markdown文件（名），可为多个。默认检索src/下的所有.md文件')
    parser.add_argument('-i', '--install', action=argparse.BooleanOptionalAction,
                        help='为开发环境安装依赖')
    parser.add_argument('-b', '--build', action=argparse.BooleanOptionalAction,
                        help='根据markdown生成静态网页')
    parser.add_argument('-d', '--deploy', action=argparse.BooleanOptionalAction,
                        help='部署。将html复制到“gh-pages”分支')
    parser.add_argument('-c', '--clean', action=argparse.BooleanOptionalAction,
                        help='清理全部临时文件')
    return parser.parse_args()

def main():
    args = parse_args()
    if args.install:
        inst_dev_reqs()
    if args.file:
        render(args)
    if args.build:
        build()
    if args.deploy:
        deploy()
    if (not args.file) and (not args.install) and (not args.build) and (not args.deploy) and (not args.clean):
        render(args)
    if args.clean:
        clean_all()

if __name__ == '__main__':
    main()