# PAL web crawler

抓取[外塞之雾](http://www.whistlerwmz.my-place.us/)网站上的仙剑相关的数据（目前只做了怪物信息的抓取）

## 使用方法

首先搭建环境，安装 `requirements.txt` 中列出的包。其中，`playwright` 需要额外的安装，以添加 web driver。

```shell
pip install -r requirements.txt
python -m playwright install
```

然后运行 `retrieve.py` 将数据抓取到本地（我已经提交了抓取好的 `.json` 文件，直接使用即可，网站上应该也不会有什么更新了）。
之后再运行 `display.py` 即可查看结果。

```shell
# optional
python retrieve.py
# see the results
python display.py
```
