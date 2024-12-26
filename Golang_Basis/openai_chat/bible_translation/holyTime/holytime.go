package main

import (
	"context"
	"fmt"
	"github.com/sashabaranov/go-openai"
	"github.com/tealeg/xlsx"
	"log"
	"os"
)

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/14 21:13
   @题目     :
   @参考     :
   @时间复杂度:
*/

func main() {
	file, err := xlsx.OpenFile("./Golang_Basis/openai_chat/bible_translation/holyTime/HolyTime.xlsx")
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
		// 读取"Chapter and Verse"列，这里假设是第4列（列索引从0开始）
		if len(row.Cells) <= 1 {
			continue
		}
		originalText := row.Cells[1].String()
		fmt.Println(originalText)
		// 如果originalText为空/空字符 则跳过
		if originalText == "" {
			continue
		}
		// 调用OpenAI API进行重写
		rewrittenText_de := rewriteWithOpenAI(originalText, "de")
		rewrittenText_fr := rewriteWithOpenAI(originalText, "fr")
		fmt.Println(rewrittenText_de)
		fmt.Println(rewrittenText_fr)
		// 将重写后的数据写回到Excel的同一列
		row.Cells[2].Value = rewrittenText_de
		row.Cells[3].Value = rewrittenText_fr
	}

	// 保存修改后的Excel文件
	err = file.Save("./Golang_Basis/openai_chat/bible_translation/holyTime/HolyTime_de_fr.xlsx")
	if err != nil {
		log.Fatal(err)
	}
}

func rewriteWithOpenAI(text string, language string) string {
	prompt := ""
	de_prompt := "You are a translation master, highly skilled in both English and German. Your task is to translate the following English text into fluent and accurate German. Please ensure that the translation maintains the meaning, tone, and nuances of the original text."
	fr_prompt := "You are a translation expert, proficient in both English and French. Your task is to translate the following English text into fluent and accurate French. Please ensure that the translation captures the meaning, tone, and nuances of the original text.\n\n"
	if language == "de" {
		prompt = de_prompt
	} else if language == "fr" {
		prompt = fr_prompt
	} else {
		return ""
	}

	token := os.Getenv("OPENAI_TOKEN")
	fmt.Println(token)
	client := openai.NewClient(token)

	resp, _ := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: openai.GPT4o,
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleSystem,
					Content: prompt,
				},
				{
					Role:    openai.ChatMessageRoleUser,
					Content: text,
				},
			},
		},
	)
	if len(resp.Choices) == 0 {
		return ""
	}
	return resp.Choices[0].Message.Content
}
