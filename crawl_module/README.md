### 爬虫模块
> 使用语言：python，框架：scrapy

爬虫中爬取的文章有限，现包括如下程序

* 博客园中的精选博客
* 开源中国中的博客


若想使用，首先安装python环境，并推荐使用`pip`工具安装第三方依赖
> 安装依赖包

```
pip install -r requirements.txt
```

> 通过以下命令可以运行开源中国的爬虫程序

```
scrapy crawl oschina
```

> 通过以下命令可以运行博客圆的爬虫程序

```
scrapy crawl cnblogs
```

也可以参考`run.sh`文件中的命令来运行
