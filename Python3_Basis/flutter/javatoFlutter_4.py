import re
import os

# Java类型到Dart类型的映射
type_mapping = {
    "byte[]":"List<int>",
    "int": "int",
    "Integer": "int",
    "short": "int",
    "Short": "int",
    "String": "String",
    "List<": "List",
    "Map": "Map",
    "double": "double",
    "float": "double",  # 将Java的float映射为Dart的double
    "Double": "double",  # 将Java的float映射为Dart的double
    "Float": "double",  # 将Java的float映射为Dart的double
    "boolean": "bool",
    "Boolean": "bool",
    "long": "int",
    "Long": "int",
    "byte": "int",
    "BigDecimal": "int",
}

not_dir = ["microclass", "menopause", "panax","alexa","warranty","ring","ring2","seckill","tradplus","questionnaire"]
not_class = ["ErpData", "CaptchaCode", "CreateGroupChannelRequest", "FeishuWholeSalesRequest", "AppStoreCallback"
    , "SessionInfo", "Tip", "ConversionApiInfo", "CervicalMucus","FeishuCooperationRequest","TribePush","Web2IndexCategory",
             "UserTrainingInfo","SmartInteraction","SmartInteraction","UserUnlockFunctionRecord","ShopBanner","ProductCompositionDto",
             "SubscriptionGiftRecord"]
not_enum = ["SpecialDay", "CaptchaCode","Package"]

ll = ["List", "Map", "String", "HashMap", "EnumField", "Lists", "SetNullResponse", "SerializedName", "Double",
      "ObjcExclude", "Setter", "Integer", "Objects", "Getter", "Target", "ArrayList","Arrays"
    , "DaoModel", "Maps", "TypeToken", "Strings", "UUID", "Retention", "RetentionPolicy", "ElementType"]

def convert_type(java_type):
    """Convert Java type to Dart type."""
    for java, dart in type_mapping.items():
        if java in java_type:
            if "List<" in java_type:
                inner_type = java_type[5:-1]
                return f"List<{convert_type(inner_type)}>?"
            return dart + "?"
    if "." in java_type:
        return java_type.replace('.', '') + "?"
    return java_type + "?"

def parse_enum(enum_code, class_name,enum_name, aaa):
    if "value" not in enum_code and "int" not in enum_code:
        enum_name=class_name+enum_name
        # 处理字符串数据，提取注释和标志
        lines = enum_code.strip().splitlines()
        flags = []
        current_comment = None

        for line in lines:
            line = line.strip()
            if line.startswith("//"):
                # 如果是注释行，保存当前注释
                current_comment = line[2:].strip()
            elif line.endswith(","):
                # 如果是标志行，去掉末尾逗号，并将标志和注释加入列表
                flag = line[:-1].strip()
                flags.append({"name": flag, "comment": current_comment})
                current_comment = None  # 重置注释

        # 生成 Dart 枚举代码
        dart_code = f"enum {enum_name} " + "{\n"
        for flag in flags:
            if flag["comment"]:
                dart_code += f"  // {flag['comment']}\n"
            dart_code += f"  {flag['name']},\n"
        dart_code+="  ;\n"
        dart_code += f"\n  const {enum_name}();\n"
        dart_code +="}\n"
        return enum_name, dart_code


    """Parse Java enum and return Dart enum as a string."""
    enum_name_match = re.search(r"enum (\w+)", enum_code)
    # 匹配整个 enum 块，提取大括号之间的内容
    # 匹配整个 enum 块，提取大括号之间的内容，直到第一个 ;
    enum_content_pattern = re.compile(
        r"\{\s*([^;]*)\s*;",  # 捕获 { 和第一个 ; 之间的内容
        re.DOTALL
    )
    # 查找匹配项
    match = enum_content_pattern.search(enum_code)

    enum_name = class_name + enum_name_match.group(1)
    if enum_name in not_enum:
        raise ValueError("不需要的枚举")
    enum_content = match.group(1).rstrip()
    # Dart枚举定义
    dart_code = f"enum {enum_name} {{\n"
    dart_code += aaa + enum_content + "\n"

    attribute_pattern = re.compile(r"private(?:\s+final)?\s+(\w+)\s+(\w+);")
    attributes = attribute_pattern.findall(enum_code)
    dart_code += ";\n\n"
    if len(attributes):
        # 根据提取的字段数量生成属性
        for java_type, field_name in attributes:
            dart_type = convert_type(java_type)
            dart_code += f"  final {dart_type} {field_name};\n"

        str1 = f"  const {enum_name}("
        str2 = ");"
        for java_type, field_name in attributes:
            str1 += "this." + field_name + ","

        # 去除最后一位符串
        str1 = str1[:-1]
        str1 += str2
        dart_code += str1 + "\n"

    dart_code += "}\n"

    return enum_name, dart_code

def parse_java_model(java_code):
    package_match = re.search(r"package\s+([\w\.]+);", java_code)
    class_name_match = re.search(r"public class (\w+)", java_code)
    field_pattern = re.compile(r"^ {2}private (?!final int value)(.+?) (\w+);", re.MULTILINE)
    import_pattern = re.compile(r"import\s+([\w\.]+);")

    if not class_name_match:
        raise ValueError("No class found in the provided Java code")
    if not package_match:
        raise ValueError("No package found in the provided Java code")

    class_name = class_name_match.group(1)

    if class_name in not_class:
        raise ValueError("不需要的class")

    package_name = package_match.group(1)
    package_path = package_match.group(1).replace('.', '/')
    fields = field_pattern.findall(java_code)
    # fields= [('long', 'likeCount'), ('List<Course>', 'courses')]
    print(fields)
    # fieldName = set()
    # fieldModelName = set()
    # for field_name in fields:
    #     if "List" in field_name[0]:
    #         # 把List<Course>的Course单独拿出来
    #         fieldModelName.add(field_name[0][5:-1])
    #         fieldName.add("List")
    #     elif "<" in field_name[0]:
    #         fieldName.add(field_name[0][0:field_name[0].index("<")])
    #     else:
    #         fieldName.add(field_name[0])

    # 查找导入的类
    imports = import_pattern.findall(java_code)

    # 查找嵌套的枚举
    nested_enum_pattern = re.compile(r"public enum (\w+) \{(.+?)\}", re.DOTALL)
    nested_enums = nested_enum_pattern.findall(java_code)

    referenced_models = set()
    referenced_classs = set()
    for java_type, _ in fields:
        if re.match(r"^[A-Z]", java_type):  # 检查是否为非基本类型
            m = java_type.replace("List<", "").replace(">", "")
            if m not in ll:
                referenced_models.add(m)

    for imp in imports:
        referenced_classs.add(imp)
        # if imp.split('.')[-1] not in ll:
        #     referenced_models.add(imp.split('.')[-1])  # 获取类名

    dart_code = f"import 'package:json_annotation/json_annotation.dart';\n"
    for model in referenced_models:
        model = model.replace('.', '')
        dart_code += f"import '{model}.dart';\n"
    print(referenced_classs)
    # if "List" in fieldName:
    #     dart_code = f"import 'List.dart';\n"
    # for imported_class in referenced_classs:
    #     flag = False
    #     for name in referenced_models:
    #         if name in imported_class:
    #             flag = True
    #             dart_code += f"import '{calculate_import_path(package_name, imported_class)}';\n"

    dart_code += f"\npart '{class_name}.g.dart';\n\n"
    dart_code += f"@JsonSerializable()\nclass {class_name} {{\n"

    for java_type, field_name in fields:
        if field_name == "false":
            continue
        dart_type = convert_type(java_type)
        dart_code += f"  {dart_type} {field_name};\n"

    dart_code += "\n  " + class_name + "();\n"

    dart_code += f"\n  factory {class_name}.fromJson(Map<String, dynamic> json) => _${class_name}FromJson(json);\n"
    dart_code += f"  Map<String, dynamic> toJson() => _${class_name}ToJson(this);\n"
    dart_code += "}\n"

    return package_path, class_name, dart_code, nested_enums

def save_to_dart_file(base_dir, package_path, file_name, dart_code):
    # output_path = os.path.join(base_dir, package_path)
    output_path = os.path.join(base_dir)
    os.makedirs(output_path, exist_ok=True)
    filename = os.path.join(output_path, f"{file_name}.dart")
    with open(filename, "w") as file:
        file.write(dart_code)
    print(f"File saved to {filename}")

def calculate_import_path(package_name, imported_class):
    """Calculate the relative import path."""
    package_parts = package_name.split('.')
    imported_parts = imported_class.split('.')

    # Determine how many parts to remove from the import path
    common_length = 0
    for i in range(min(len(package_parts), len(imported_parts))):
        if package_parts[i] == imported_parts[i]:
            common_length += 1
        else:
            break

    # Number of parent directories to go up
    num_parent_dirs = len(package_parts) - common_length
    relative_path = '../' * num_parent_dirs

    # Build the import path
    class_name = imported_parts[-1]
    if common_length == len(imported_parts) - 1:
        return f"{relative_path}{class_name}.dart"
    sub_path = '/'.join(imported_parts[common_length:len(imported_parts) - 1])  # Intermediate package parts
    if sub_path:
        return f"{relative_path}{sub_path}/{class_name}.dart"
    return f"{relative_path}/{class_name}.dart"

def convert_java_models_in_directory(java_dir, dart_base_dir,class_list):
    """Convert all Java model files and enums in the specified directory to Dart files."""
    for root, directory, files in os.walk(java_dir):
        # 过滤掉不需要的目录
        directory[:] = [d for d in directory if d not in not_dir]
        for file in files:
            print(file)
            if file not in class_list:
                continue
            if file.endswith(".java"):
                java_file_path = os.path.join(root, file)
                with open(java_file_path, "r") as f:
                    java_code = f.read()
                try:
                    if "class" not in java_code and "enum" in java_code:
                        # 单独枚举文件
                        try:
                            # Extract package path from the file content
                            package_match = re.search(r"package\s+([\w\.]+);", java_code)
                            if not package_match:
                                print(f"Skipping {java_file_path}: No package declaration found.")
                                continue

                            package_path = package_match.group(1).replace('.', '/')
                            enum_name, dart_code = parse_enum(java_code, "", "","  ")
                            save_to_dart_file(dart_base_dir, package_path, enum_name, dart_code)
                        except ValueError as e:
                            print(f"Error processing {java_file_path}: {e}")
                        continue

                    package_match = re.search(r"package\s+([\w\.]+);", java_code)
                    if not package_match:
                        print(f"Skipping {java_file_path}: No package declaration found.")
                        continue

                    package_path = package_match.group(1).replace('.', '/')
                    package_path, class_name, dart_code, nested_enums = parse_java_model(java_code)

                    # Save the model class
                    save_to_dart_file(dart_base_dir, package_path, class_name, dart_code)

                    not_not_eume = ["MessageCenterMessageSpecType", "MessageCenterMessageFastingSpecType",
                                    "SubscriptionActivityPlanPackage"]
                    # Save each enum in a separate file
                    for enum_name, enum_content in nested_enums:
                        if class_name + enum_name in not_not_eume:
                            continue
                        print(enum_name,enum_content)
                        _, dart_enum_code = parse_enum(f"enum {enum_name} {{{enum_content}}}", class_name,enum_name, "    ")
                        print(111)
                        save_to_dart_file(dart_base_dir, package_path, class_name + enum_name, dart_enum_code)

                except ValueError as e:
                    print(f"Error processing {java_file_path}: {e}")
                except Exception as e:
                    print(f"Unexpected error processing {java_file_path}: {e}")

# 调用转换函数
java_directory = "/Users/yinpeng/JavaWorkSpace/lollypop/lollypop-common/src/main/java/cn/lollypop/be/model"
dart_output_directory = "/Users/yinpeng/GoWorkSpace/AlgoScripts/Python3_Basis/flutter/newModel"
# 读取文件并将类名存入列表
with open('flutter_list.txt', 'r') as file:
    class_list = [line.strip() for line in file.readlines()]

print(class_list)
convert_java_models_in_directory(java_directory, dart_output_directory,class_list)
