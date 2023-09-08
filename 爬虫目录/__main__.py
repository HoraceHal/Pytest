# This is a basic workflow to help you get started with Actions

name: Github
Pages

# Controls when the workflow will run
on:
schedule:
# 下一行是说在每天的国际标准时间23点（北京时间早上7点）触发该任务
# 你可以随意修改
- cron: '0 23 * * *'
# Allows you to run this workflow manually from the Actions tab
workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
# This workflow contains a single job called "build"
build:
# The type of runner that the job will run on
runs - on: ubuntu - latest

# Steps represent a sequence of tasks that will be executed as part of the job
steps:
# 拉取代码
- name: Checkout
uses: actions / checkout @ v2
# 1、生成静态文件
- name: Build
run: npm
i - g
notablog & & notablog
generate.
# 2、部署到 GitHub Pages
- name: Deploy
uses: JamesIves / github - pages - deploy - action @ v4
.2
.5
with:
    token: ${{secrets.ACCESS_TOKEN}}
    repository - name: FizzerYu / FizzerYu.github.io  # 修改这里
    BRANCH: main  # 如果你的仓库默认分支是 master 记得修改这里
    FOLDER: public