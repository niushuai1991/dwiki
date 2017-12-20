
# 知识库平台

## 技术选型
language: python2.7
search engine: Elasticserach
database: MySQL
framework: django
开发语言使用python，是因为我希望把这个项目做成一个比较轻量的项目，另外python在开发速度和自带的功能上比较强，所以选择它。
检索功能，我设想的是能够进行实时检索，目前有不少互联网项目在使用ES，如github,京东等。
数据库，按目前的情况，搜索功能完全使用ES，那数据库只需要保证能存储下目前的数据量及可。
以公司现有的文档和预计的发展情况来说，MySQL应该能够支撑得住。如果使用mariadb之类的估计也可以。

后台框架，目前决定使用django，我之前尝试过使用django，在开发过程中还是比较快的。

