package main

import (
	"context"
	"fmt"
	"github.com/sashabaranov/go-openai"
	"io/ioutil"
	"os"
)

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/12/27 17:55
    @题目     :
    @参考     :
    @时间复杂度:
    @空间复杂度:

 数据范围:

*/

func main() {
	token := os.Getenv("OPENAI_TOKEN")
	fmt.Println(token)
	client := openai.NewClient(token)
	filePath := "Golang_Basis/openai_chat/verse_reflection/chat_compare_version.md"
	content, err := ioutil.ReadFile(filePath)
	if err != nil {
		fmt.Printf("读取文件时出错: %v\n", err)
		return
	}
	// 将文件内容赋值给 prompt 字符串
	prompt := string(content)
	fmt.Println("Markdown 内容已成功赋值给 prompt 变量：")
	fmt.Println(prompt)

	resp, _ := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: openai.GPT4oMini,
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleSystem,
					Content: prompt,
				},
				{
					Role:    openai.ChatMessageRoleUser,
					Content: "compare John1:1-5，niv vs kjv vs esv",
				},
			},
		},
	)
	fmt.Println(resp.Choices[0].Message.Content)
}
