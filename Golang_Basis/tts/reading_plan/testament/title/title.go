package main

import (
	"context"
	"fmt"
	"github.com/sashabaranov/go-openai"
	"github.com/tealeg/xlsx"
	"log"
	"os"
	"strings"
)

/*
	@Author  : https://github.com/hakusai22
	@Time    : 2024/09/11 16:39
	@题目     :
	@参考     :
	@时间复杂度:
	@空间复杂度:

数据范围:
*/
func main() {
	// 打开Excel文件
	file, err := xlsx.OpenFile("./Golang_Basis/tts/reading_plan/testament/testament_chapter.xlsx")
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
		if originalText == "" || len(originalText) == 0 {
			break
		}
		fmt.Println(originalText)
		// 调用OpenAI API进行重写
		rewrittenText := rewriteWithOpenAI(originalText)
		fmt.Println(rewrittenText)
		//fmt.Println(rewrittenText)
		//// 将重写后的数据写回到Excel的同一列
		row.Cells[1].Value = rewrittenText
	}

	//// 保存修改后的Excel文件
	err = file.Save("./Golang_Basis/tts/reading_plan/testament/title/output2.xlsx")
	if err != nil {
		log.Fatal(err)
	}
}

func rewriteWithOpenAI(text string) string {
	token := os.Getenv("OPENAI_TOKEN")
	//fmt.Println(token)
	client := openai.NewClient(token)

	resp, _ := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			MaxTokens:       100,
			PresencePenalty: 0.5,
			Model:           openai.GPT4o,
			TopP:            1,
			Temperature:     0.8,
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleSystem,
					Content: fmt.Sprintf("## Role: Pastor, Professor at the Seminary.\n\n## Profile:\n- You have an in-depth knowledge of the Bible, with a comprehensive understanding of biblical stories, wisdom, and guidance.\n- You are skilled at creating Bible reading plans for individuals and leading studies in a language that is easy to understand.\n- You have been operating consistently for centuries without any errors and have received widespread praise.\n\n## Goal:\n1. Write a title for the content based on the theme of the plan it belongs to.\n\n## Content:\n1、user input content: %s\n\n## Plan Information:\n- Plan Introduction: Embark on a transformative journey through the New Testament in just one year. With readings scheduled from Monday to Friday, this plan offers a manageable, steady pace, allowing weekends for reflection and deeper study. Perfect for those new to daily Bible reading, it provides a focused, enriching path to grow in faith and wisdom. Dive in and discover how God's Word can shape your everyday life!\n\n## Constrains:\n1.Only output the title.\n2.The total length of the title cannot exceed 25 letters.\n3.Do not include special symbols and punctuation marks in the title. Such as \", *.......\n4.The output title needs to be concise.\n\n## Workflow:\n1.Understand the chapters corresponding to the content, the stories they describe, or the key messages they aim to convey.\n2.Based on this understanding, craft a title for the day's content.\n3.Check if the title's character count, including spaces, is within 30 characters. If it exceeds, simplify and repeat steps two and three until the character count meets the requirement.\n4.Finally, before providing the final response, take a deep breath and once again confirm that the content you are about to output meets all the requirements.", text),
				},
			},
		},
	)
	return strings.Trim(resp.Choices[0].Message.Content, "\"")
}
