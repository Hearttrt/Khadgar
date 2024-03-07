## Something about Python scripts
### XML/xml_to_csv.py 
旨在使用iterparse 处理大型复杂的XML结构文件，提取想要的信息

#### 使用iterparse 处理大型XML
+ 解析XML： 使用iterparse 遍历XML文档，根据事件类型（'Start', 'End'）来处理遇到的元素。iterparse()创建出的迭代器产生出形式为（event，elem）的元组，这里的event是列出的事件，而elem是对应的XML元素。
+ 提取信息：识别元素的属性及相关信息
+ 保存文件：有效信息保存到CSV中。

#### 目的
+ 每次重装Windows都要点击DISM++各个选项来优化操作系统，步骤过于繁琐。因此旨在减少重复性操作，虽然重装次数不够频繁。因此我想可以直接使用Python对xml进行分析和处理提取有效的信息，生成对应适合自己系统优化的reg文件

#### 数据源
https://github.com/Chuyu-Team/Dism-Multi-language/blob/master/Data.xml

#### 分析
+ 通过对大佬Chuyu-Team的Data.xml文件分析，其xml结构包括了修改系统设置的注册表路径，数据类型和值。
+ 由于xml结构过于复杂，部分数据在6+层里面，通过常规的步骤比较繁琐，因此借鉴《Python CookBook》书中`6.4　以增量方式解析大型XML文件` 处理data数据。
