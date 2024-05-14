# -*- encoding: utf-8 -*-
'''
@File    :   gitpush.py
@Time    :   2024/05/14 16:35:46
@Author  :   zhangsiheng 
@Version :   1.0
@Contact :   zhangsiheng@cvte.com
@Desc    :   None
'''

import os

os.system('git init')
os.system('git add .')
os.system('git commit -m "first commit"')
os.system('git branch -M main')
os.system('git remote add origin git@github.com:NewZsh/repo_for_render_mermaid.git')
os.system('git push -u origin main')

