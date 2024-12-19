知网学术大讲堂刷课脚本

https://k.cnki.net/ 


大致使用方法：
1. 获取 course_id 和 lecture_id，填入 list，每行第一个是 course_id，后面空格依次填充 lecture_id
2. 重命名 config.py.tmpl 填充必要cookie配置然后运行脚本即可。


没实现，如果你也有研究原理，欢迎共享
1. 批量自动获取 course_id 和 lecture_id


## note 

这个接口可以获取 course_ids
```
curl 'https://k.cnki.net/kedu/course/list' 
```

这个接口可以获取 lecture_ids
```
curl 'https://k.cnki.net/kedu/courseInfo/catalog?courseId=53388&progressRequired=true' 
```