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
	//fmt.Println(prompt)
	//userMessageV2 := "根据 Genesis 2:25-26 原文内容进行版本比较, 使用默认版本 NIV(Adam and his wife were both....must not eat from any tree in the garden’?) 对比其他版本 一一对比 列表如下: [ESV(And the man and his wife..... eat of any tree in the garden’?) ,KJV(And they were both naked....every tree of the garden?) ,LSG(E ambos estavam nus....de toda a árvore do jardim?)]," +
	//	"根据部分内容推出省略....的全部内容并挑出重点内容进行对比,一定要使用各自的原文进行对比,输出的内容使用 ENGLISH语言."
	//userMessageV2 := "根据 Genesis 2:25-28 3段落verse原文内容进行版本比较, 使用默认版本 NIV(Adam and his wife were both....省略3段verse) 对比其他版本 一一对比 列表如下: [ESV(And the man and his wife.....省略3段verse) ,KJV(And they were both naked....省略3段verse) ,LSG(E ambos estavam nus....省略3段verse)]," +
	//	"联想出省略....后的3段落verse全部内容进行对比,使用整个句子进行对比,输出的内容使用 ENGLISH语言."
	//userMessageV2 := "compare 书名是Genesis 第2章节 verse序列号段是1-3, 使用版本NIV 与" +
	//	"其他版本 [ESV,KJV,LSG]列表版本一一对比,挑出重点内容进行对比,主要是输出关键不同点,一定要使用各自的原文,输出的内容使用 ENGLISH语言"
	userMessageV2 := "compare Genesis 2:1-3，niv vs kjv vs esv，current vision is kjv"

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
					Content: userMessageV2,
				},
			},
		},
	)
	fmt.Println(resp.Choices[0].Message.Content)
}
