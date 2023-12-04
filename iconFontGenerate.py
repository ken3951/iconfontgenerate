import sys, os
import json

# Python 3 版本校验(必须使用 Python 3)
if sys.version_info[0] < 3:
    raise "Must be using Python 3"

if len(sys.argv) < 2 :
    print('缺少iconfont对应json文件')
    sys.exit(0)

# 加载iconfont json文件
iconfont_json_file = sys.argv[1]

# 参数定义
origin_file_name = os.path.basename(iconfont_json_file)

temp_file_name = "temp_IconFontDefine.swift"
target_file_name = "IconFontDefine.swift"

with open(iconfont_json_file, 'r', encoding='utf-8') as json_file, open(temp_file_name, 'w+', encoding='utf-8') as temp_file:
    print("文件打开...")
     
    json_text = json_file.read()
     
    new_dict = json.loads(json_text)
    print("加载入文件完成...")

    font_family = new_dict['font_family']
    glyphs = new_dict['glyphs']
    glyphs.sort(key = lambda x:x['font_class'])
    sorted_glyphs = glyphs

    iconfont_define = ''
    iconfont_define += '\n\n' '/// 脚本生成代码，请勿手动修改'
    iconfont_define += '\n\n' + '/// iconfont字体名称'
    iconfont_define += '\n' + 'let iconFontName = "' + font_family + '"'
    iconfont_define += '\n\n' '/// iconfont资源' + '\n'
    iconfont_define += 'public enum IconFontSource: String {'

    for item_dict in sorted_glyphs:
        icon_name = item_dict['name']
        font_class = item_dict['font_class'].replace('-','_')
        unicode = item_dict['unicode']
        iconfont_define += '\n' + '\t'
        iconfont_define += 'case '+ font_class + ' = "\\u{' + unicode + '}"'
        
    iconfont_define += '\n'
    iconfont_define += '}'

    temp_file.write(iconfont_define)
    if os.path.exists(target_file_name):
        os.remove(target_file_name)
    os.rename(temp_file_name,target_file_name)
    
    print('文件生成结束...')


# 代码生成结果预览
# let iconFontName = "iconfont"

# public enum IconFontSource: String {
# 	case COD = "\u{e650}"
# 	case FAQ = "\u{e66d}"
# 	case POST = "\u{e661}"
# }