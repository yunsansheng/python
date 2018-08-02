#markdown语法

[TOC]


1. **bold**
 
2. *italic* 

3. <del>del代替删除线</del>

3. unorder list  无序列表用 - + * 任何一种都可以，先实心，再空心，再方块
    - a
    - b
    - c
    + 1
    * 1
        + 1
            + 2

4. orderlist ，先1，2，3，再罗马数字,在a.b.c
    1. l 
        1. 21
    
    2. k
  
5. quote

    >quote

    > > This is nested blockquote.
    >
    > Back to the first level.
    > > thisis the two
    
6. pic
    
    ![name](http://www.baidu.com)
    `可以用img代替`
7. url

    [urlname](http://www.baidu.com)
    `可以用a代替`
    
8. code

`i am sigle code`

```123
    code here
```

9. table

>可以指定对齐方式, 如Item列左对齐, Value列右对齐, Qty列居中对齐
 
| Item     | Value | Qty   |
| :------- | ----: | :---: |
| Computer | \$1600 |  5    |
| Phone    | \$12   |  12   |
| Pipe     | \$1    |  234  |

10. 直接用html

    <table>
        <tr>
            <th rowspan="2">值班人员</th>
            <th>星期一</th>
            <th>星期二</th>
            <th>星期三</th>
        </tr>
        <tr>
            <td>李强</td>
            <td>张明</td>
            <td>王平</td>
        </tr>
    </table>


#注意
- 请注意，在 HTML 区块标签间的 Markdown 格式语法将不会被处理，你在 HTML 区块内使用 Markdown 样式的*强调*会没有效
- 一个 Markdown 段落是由一个或多个连续的文本行组成，它的前后要有一个以上的空行（空行的定义是显示上看起来像是空的，便会被视为空行。比方说，若某一行只包含空格和制表符，则该行也会被视为空行）。
- 列表项目标记通常是放在最左边，但是其实也可以缩进，最多 3 个空格，项目标记后面则一定要接着至少一个空格或制表符。
- 分割线 你可以在一行中用三个以上的星号、减号、底线来建立一个分隔线，行内不能有其他东西。你也可以在星号或是减号中间插入空格



