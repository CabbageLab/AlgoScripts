package main

import (
	"fmt"
	"github.com/tealeg/xlsx"
	"io/ioutil"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/09/05 11:12
    @题目     :
    @参考     :
    @时间复杂度:
    @空间复杂度:

 数据范围:

*/

func main() {
	// 调用函数提取指定范围内的段落内容
	// 打开Excel文件
	file, err := xlsx.OpenFile("./Golang_Basis/openai_chat/bible/kjv_verse_content.xlsx")
	if err != nil {
		log.Fatal(err)
	}

	// 读取第一个工作表
	sheet := file.Sheets[0]
	fmt.Println(sheet)
	// 遍历所有行
	for rowIndex, row := range sheet.Rows {
		if rowIndex == 0 { // 跳过标题行
			continue
		}
		originalText := row.Cells[0].String()
		fmt.Println(originalText)
		if originalText == "" || len(originalText) == 0 {
			break
		}
		originalText = strings.ReplaceAll(originalText, "Psalms", "Psalm")
		content := getcontent(originalText)
		row.Cells[1].Value = content
	}
	//// 保存修改后的Excel文件
	err = file.Save("./Golang_Basis/openai_chat/bible/output_christmas.xlsx")
	if err != nil {
		log.Fatal(err)
	}

}

func getcontent(verses string) string {
	result := ""
	split := strings.Split(verses, " ")
	chapter := ""
	start := 0
	end := 0
	start_s := 0
	end_s := 0
	if len(split) <= 2 {
		chapter = split[0]
		if strings.Contains(split[1], ":") {
			aa := strings.Split(split[1], ":")
			start, _ = strconv.Atoi(aa[0])
			end, _ = strconv.Atoi(aa[0])

			aaa := strings.Split(aa[1], "-")
			start_s, _ = strconv.Atoi(aaa[0])
			if len(aaa) == 1 {
				end_s, _ = strconv.Atoi(aaa[0])
			} else {
				end_s, _ = strconv.Atoi(aaa[1])
			}
		} else {
			aa := strings.Split(split[1], "-")
			if len(aa) == 1 {
				atoi, _ := strconv.Atoi(aa[0])
				start = atoi
				end = atoi
			} else {
				atoi, _ := strconv.Atoi(aa[0])
				start = atoi
				atoi2, _ := strconv.Atoi(aa[1])
				end = atoi2
			}
		}

	} else {
		chapter = split[0] + " " + split[1]
		if strings.Contains(split[2], ":") {
			aa := strings.Split(split[2], ":")
			start, _ = strconv.Atoi(aa[0])
			end, _ = strconv.Atoi(aa[0])

			aaa := strings.Split(aa[1], "-")
			start_s, _ = strconv.Atoi(aaa[0])
			if len(aaa) == 1 {
				end_s, _ = strconv.Atoi(aaa[0])
			} else {
				end_s, _ = strconv.Atoi(aaa[1])
			}
		} else {
			aa := strings.Split(split[2], "-")
			if len(aa) == 1 {
				atoi, _ := strconv.Atoi(aa[0])
				start = atoi
				end = atoi
			} else {
				atoi, _ := strconv.Atoi(aa[0])
				start = atoi
				atoi2, _ := strconv.Atoi(aa[1])
				end = atoi2
			}
		}
	}

	fmt.Println(chapter)
	fmt.Println(start)
	fmt.Println(end)
	fmt.Println(start_s)
	fmt.Println(end_s)
	for i := start; i <= end; i++ {
		verseContent, err := getVerseContent(chapter, strconv.Itoa(i), start_s, end_s)
		if err != nil {
			fmt.Println("错误:", err)
			os.Exit(1)
		}
		//fmt.Println("提取指定范围内的段落内容:")
		result += verseContent
		fmt.Println(verseContent)
	}
	return result
}

// getVerseContent 从指定文件中提取指定范围内的段落内容
func getVerseContent(chapter, fileName string, start_s, end_s int) (string, error) {
	// 构建文件路径
	filePath := fmt.Sprintf("Golang_Basis/openai_chat/bible/KJV/%s/%s.txt", chapter, fileName)

	// 读取文件内容
	content, err := ioutil.ReadFile(filePath)
	if err != nil {
		return "", fmt.Errorf("无法读取文件: %v", err)
	}

	// 将内容转换为字符串
	text := string(content)

	// 正则表达式提取标签内的数值和内容，处理标签之间的文本
	re := regexp.MustCompile(`<bmstyle[^>]*?>(\d+)</bmstyle>([^<]*)`)
	matches := re.FindAllStringSubmatch(text, -1)

	result := ""

	// 遍历所有匹配的段落
	for _, match := range matches {
		if len(match) > 2 {
			// 提取段落编号
			number, err := strconv.Atoi(match[1])
			if err != nil {
				return "", fmt.Errorf("解析段落编号出错: %v", err)
			}
			if start_s > 0 && end_s > 0 {
				if number >= start_s && number <= end_s {
					// 去除内容中可能的换行和多余空格
					content := strings.TrimSpace(match[2])
					// 将内容添加到结果中
					//fmt.Printf("段落 %d: %s\n", number, content)
					result += content
					result += "\n"
				}
			} else {
				// 去除内容中可能的换行和多余空格
				content := strings.TrimSpace(match[2])
				// 将内容添加到结果中
				//fmt.Printf("段落 %d: %s\n", number, content)
				result += content
				result += "\n"
			}

		} else {
			fmt.Printf("匹配结果不符合预期: %v\n", match)
		}
	}

	return result, nil
}
