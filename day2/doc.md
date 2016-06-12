#docx模块是可以直接操作生成docx文档的python模块

##基本使用方法：
  doc = Document();在内存中建立一个doc文档
  doc.add_paragraph(data); 在doc 文档中添加一个段落
  doc.add_picture("xxx.png")添加一个图片 
  doc.save('demo.docx') 存储docx文档
