#BeautifulSoup学习
  bs 是将复杂的Html文档转换成一个复杂的树形结构，每个节点都是一个python对象，所有的对象可以归为四种。Tag、NavigableString、BeautifulSoup、Comment
##内置对象
###Tag：与原生Html中的标签类似，如a 标签，img标签。tag 两个重要的属性 name（标签的名字，例如a标签。tag.name ='a'。） 和 attributes(标签的属性值，标签的属性有多个，例如class 属性，name 属性，tag标签的属性操作与字典类似，如获取一个class属性，tag['class'],也可以直接利用“点”获取所有的属性，比如tag.attrs：这个方法会获取该标签中所有的属性值，)多值属性（一个属性中含有多个值），例如class 可能会为了控制样式会显示多个值，对于在html中比较常见的BeautifulSoup返回的是一个list，在Html定义中都没有被定义为多值属性的，那bs将该属性作为字符串返回。Tag中的字符串不能编辑，但是可以被替换成其它的字符串，使用replace_with()方法。
###BeautifulSoup：该对象表示的是一个文档的全部内容，大部分时候，可以把它当作Tag对象，它支持遍历文档树和搜索文档树中描述的大部分的方法。它没有name和attribute属性，其包含一个值为[document]的.name属性
###NavigableString：可以遍历的字符串，对象支持遍历文档树和搜索文档树中定义的大部分属性，Bs用NavigableString类来包装tag中的字符串，NavigableString字符串与Python中的Unicode字符串相同，通过unicode（）方法可以直接将NavigableString对象转换成Unicode字符串。
###Comment:注释，comment时一个特殊类型的NavigableString对象，
##字节点
###tag.name:直接使用tag.name的形式，也可以在文档树的tag中多次调用这个方法，例如获取body中的b标签。soup.body.b。PS:通过点属性只能获得当前名字的第一个tag。
###tag.contents：将tag的字节点一列表的方式输出，
###tag.children
