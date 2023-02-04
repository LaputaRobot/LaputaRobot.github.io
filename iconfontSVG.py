from xml.dom.minidom import parse, Document
import xml.dom.minidom

def getSVGAttrs():
    DOMTree = xml.dom.minidom.parse("bilibili.svg")
    svg = DOMTree.documentElement
    attrs={}
    for k in svg.attributes.keys():
        attr=svg.attributes[k]
        print('{}: {}'.format(attr.name,attr.value))
        attrs[attr.name]=attr.value
    return attrs


def getSVG():
    DOMTree = xml.dom.minidom.parse("bilibili.svg")
    svg = DOMTree.documentElement
    return svg


# 使用minidom解析器打开 XML 文档

DOMTree = xml.dom.minidom.parse("al.svg")

collection = DOMTree.documentElement

symbols = collection.getElementsByTagName("symbol")

svg_attrs=getSVGAttrs()

for symbol in symbols:

    if symbol.hasAttribute('id'):

        id=symbol.getAttribute('id')

        f_name="svg/{}.svg".format(id)

        # print('id: {}'.format(id))
        doc = Document() 
        # svgDomTree = parse(f_name)
        svg_node=doc.createElement('svg')
        for attr in svg_attrs:
            svg_node.setAttribute(attr, svg_attrs[attr])
        doc.appendChild(svg_node)
        # xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" clip-rule="evenodd" height="1024" width="1024" viewBox="0 0 1024 1024"="1.1" xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" clip-rule="evenodd" height="1024" width="1024" viewBox="0 0 1024 1024"
        paths = symbol.getElementsByTagName('path')
        for p in paths:
            svg_node.appendChild(p)
        fp = open(f_name, 'wb') 
        wr=doc.toprettyxml(indent='',  encoding='utf-8')[39:]
        # doc.writexml(fp, indent='', addindent='\t', newl='\n', encoding='utf-8')
        fp.write(wr)
        fp.close()

        # print(len(paths))

    # for path in paths:

    #     print(path.getAttribute('d'))