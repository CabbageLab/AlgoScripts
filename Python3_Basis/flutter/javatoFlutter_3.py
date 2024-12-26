import re
import os

# Java类型到Dart类型的映射
type_mapping = {
    "int": "int",
    "Integer": "int",
    "short": "int",
    "String": "String",
    "List": "List",
    "Map": "Map",
    "double": "double",
    "float": "double",  # 将Java的float映射为Dart的double
    "Double": "double",  # 将Java的float映射为Dart的double
    "Float": "double",  # 将Java的float映射为Dart的double
    "boolean": "bool",
    "long": "int",
}

ll = ["List", "Map", "String", "HashMap", "EnumField", "Lists", "SetNullResponse", "SerializedName", "Double",
      "ObjcExclude", "Setter", "Integer", "Gender", "Objects", "Getter"
    , "DaoModel", "Maps", "TypeToken"]

def convert_type(java_type):
    """Convert Java type to Dart type."""
    for java, dart in type_mapping.items():
        if java in java_type:
            if "List<" in java_type:
                inner_type = java_type[java_type.index('<') + 1: java_type.rindex('>')]
                return f"List<{convert_type(inner_type)}>?"
            return dart + "?"
    return java_type + "?"

def parse_enum(enum_code, class_name):
    """Parse Java enum and return Dart enum as a string."""
    enum_name_match = re.search(r"enum (\w+)", enum_code)
    value_pattern = re.compile(r"(\w+)\((\d+)\)")

    if not enum_name_match:
        raise ValueError("No enum found in the provided code")

    enum_name = class_name + enum_name_match.group(1)
    values = value_pattern.findall(enum_code)

    # Dart枚举定义，支持值映射和fromValue方法
    dart_code = f"enum {enum_name} {{\n"
    if len(values) == 0:
        dart_code += "//枚举多字段的 暂时不支持 todo\n}"
        return enum_name, dart_code
    for value_name, value in values:
        dart_code += f"  {value_name}({value}),\n"
    dart_code += ";\n\n"
    dart_code += "  final int value;\n\n"
    dart_code += f"  const {enum_name}(this.value);\n\n"
    dart_code += f"  int get getValue => value;\n\n"
    dart_code += f"  static {enum_name} fromValue(int value) {{\n"
    dart_code += f"    return {enum_name}.values.firstWhere((e) => e.value == value, orElse: () => {enum_name}.{values[0][0]});\n"
    dart_code += "  }\n"
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
        if imp.split('.')[-1] not in ll:
            referenced_models.add(imp.split('.')[-1])  # 获取类名

    dart_code = f"import 'package:json_annotation/json_annotation.dart';\n"
    for model in referenced_models:
        dart_code += f"import '{model}.dart';\n"
    print(referenced_classs)
    # if "List" in fieldName:
    #     dart_code = f"import 'List.dart';\n"
    for imported_class in referenced_classs:
        flag = False
        for name in referenced_models:
            if name in imported_class:
                flag = True
                dart_code += f"import '{calculate_import_path(package_name, imported_class)}';\n"

    dart_code += f"\npart '{class_name}.dart';\n\n"
    dart_code += f"@JsonSerializable()\nclass {class_name} {{\n"

    for java_type, field_name in fields:
        dart_type = convert_type(java_type)
        dart_code += f"  final {dart_type} {field_name};\n"

    dart_code += f"\n  {class_name}({{\n"
    for _, field_name in fields:
        dart_code += f"    required this.{field_name},\n"
    dart_code += "  });\n"

    dart_code += f"\n  factory {class_name}.fromJson(Map<String, dynamic> json) => _${class_name}FromJson(json);\n"
    dart_code += f"  Map<String, dynamic> toJson() => _${class_name}ToJson(this);\n"
    dart_code += "}\n"

    return package_path, class_name, dart_code, nested_enums

def save_to_dart_file(base_dir, package_path, file_name, dart_code):
    output_path = os.path.join(base_dir, package_path)
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

def convert_java_models_in_directory(java_dir, dart_base_dir):
    """Convert all Java model files and enums in the specified directory to Dart files."""
    for root, _, files in os.walk(java_dir):
        for file in files:
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
                            enum_name, dart_code = parse_enum(java_code, "")
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

                    # Save each enum in a separate file
                    for enum_name, enum_content in nested_enums:
                        _, dart_enum_code = parse_enum(f"enum {enum_name} {{{enum_content}}}", class_name)
                        print(111)
                        save_to_dart_file(dart_base_dir, package_path, class_name + enum_name, dart_enum_code)

                except ValueError as e:
                    print(f"Error processing {java_file_path}: {e}")
                except Exception as e:
                    print(f"Unexpected error processing {java_file_path}: {e}")

# 调用转换函数
java_directory = "/Users/yinpeng/JavaWorkSpace/lollypop/lollypop-common/src/main/java/cn/lollypop/be/model"
dart_output_directory = "/Users/yinpeng/GoWorkSpace/AlgoScripts/Python3_Basis/flutter"
convert_java_models_in_directory(java_directory, dart_output_directory)
