/*
 * @Author: hakusai
 * @Date: 2025-04-25 14:45:39
 * @LastEditTime: 2025-04-25 14:46:24
 * @Description: https://github.com/hakusai22
 */
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    // 1. 变量声明
    // Rust默认变量是不可变的(immutable)，类似于Java的final
    let x = 5; // 不可变变量
    let mut y = 10; // 可变变量，类似于普通的Java变量
    y = 20; // 可以修改
    
    // 2. 基本数据类型
    // 整数类型
    let i8_num: i8 = 127; // 8位有符号整数
    let u8_num: u8 = 255; // 8位无符号整数
    let i32_num = 42; // 默认整数类型是i32
    
    // 浮点数
    let f64_num = 3.14; // 默认浮点类型是f64
    let f32_num: f32 = 3.14;
    
    // 布尔值
    let is_true: bool = true;
    
    // 字符和字符串
    let c = 'z'; // 字符类型
    let s = "Hello"; // 字符串切片
    let string = String::from("Hello"); // String类型
    
    // 3. 复合类型
    // 元组
    let tup: (i32, f64, &str) = (500, 6.4, "hello");
    let (x, y, z) = tup; // 解构
    
    // 数组
    let arr = [1, 2, 3, 4, 5]; // 固定长度数组
    let first = arr[0];
    
    println!("Basic types demo:");
    println!("Integer: {}", i32_num);
    println!("Float: {}", f64_num);
    println!("String: {}", string);
    println!("Tuple: {:?}", tup);
    println!("Array: {:?}", arr);

    // 1. if表达式
    let number = 7;
    
    if number < 5 {
        println!("number is less than 5");
    } else if number > 5 {
        println!("number is greater than 5");
    } else {
        println!("number is 5");
    }
    
    // if作为表达式
    let condition = true;
    let number = if condition { 5 } else { 6 };
    
    // 2. 循环
    // loop循环
    let mut counter = 0;
    let result = loop {
        counter += 1;
        if counter == 10 {
            break counter * 2; // 返回值
        }
    };
    
    // while循环
    let mut number = 3;
    while number != 0 {
        println!("{}!", number);
        number -= 1;
    }
    
    // for循环
    let arr = [10, 20, 30, 40, 50];
    for element in arr.iter() {
        println!("value is: {}", element);
    }
    
    // Range循环
    for number in 1..4 { // 不包含4
        println!("{}!", number);
    }

    // 函数调用
    let sum = add(5, 3);
    println!("Sum: {}", sum);
    
    // 创建结构体实例
    let mut rect = Rectangle::new(30, 50);
    
    // 调用方法
    println!("Area: {}", rect.area());
    
    // 调用可变方法
    rect.resize(40, 60);
    println!("New area: {}", rect.area());

    // 1. Result 类型处理可恢复错误
    let f = File::open("hello.txt");
    
    let f = match f {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create("hello.txt") {
                Ok(fc) => fc,
                Err(e) => panic!("Problem creating the file: {:?}", e),
            },
            other_error => panic!("Problem opening the file: {:?}", other_error),
        },
    };
    
    // 2. unwrap和expect
    let f = File::open("hello.txt").unwrap(); // 如果错误则panic
    let f = File::open("hello.txt").expect("Failed to open hello.txt"); // 带自定义消息的panic
    
    // 3. 传播错误
    fn read_username_from_file() -> Result<String, std::io::Error> {
        let f = File::open("hello.txt")?; // ?运算符自动传播错误
        Ok(String::new())
    }

    // 1. 所有权规则
    let s1 = String::from("hello"); // s1是字符串的所有者
    let s2 = s1; // 所有权移动到s2，s1不再有效
    // println!("{}", s1); // 这行会编译错误
    
    // 2. 借用
    let s1 = String::from("hello");
    let len = calculate_length(&s1); // 传递引用
    println!("Length of '{}' is {}.", s1, len);
    
    // 3. 可变借用
    let mut s = String::from("hello");
    change(&mut s);
    println!("{}", s);
    
    // 4. 切片
    let s = String::from("hello world");
    let hello = &s[0..5]; // 字符串切片
    let world = &s[6..11];
    println!("{} {}", hello, world);
}

// 函数定义
fn add(x: i32, y: i32) -> i32 {
    x + y  // 注意：这里没有分号，表示返回值
}

// 结构体定义
struct Rectangle {
    width: u32,
    height: u32,
}

// 为结构体实现方法
impl Rectangle {
    // 构造函数（关联函数，类似于静态方法）
    fn new(width: u32, height: u32) -> Rectangle {
        Rectangle { width, height }
    }
    
    // 方法（需要&self参数）
    fn area(&self) -> u32 {
        self.width * self.height
    }
    
    // 可变方法（需要&mut self）
    fn resize(&mut self, width: u32, height: u32) {
        self.width = width;
        self.height = height;
    }
}

fn calculate_length(s: &String) -> usize {
    s.len()
}

fn change(s: &mut String) {
    s.push_str(" world");
}
