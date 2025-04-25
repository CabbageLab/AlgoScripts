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
	// 打开Excel文件
	file, err := xlsx.OpenFile("./Golang_Basis/openai_chat/verse_reflection/daily_verse_lent.xlsx")
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
		originalText := row.Cells[1].String()
		fmt.Println(originalText)
		// 调用OpenAI API进行重写
		rewrittenText := rewriteWithOpenAI(originalText)
		fmt.Println(rewrittenText)
		// 将重写后的数据写回到Excel的同一列
		row.Cells[4].Value = rewrittenText
	}

	// 保存修改后的Excel文件
	err = file.Save("./Golang_Basis/openai_chat/verse_reflection/daily_verse_lent.xlsx")
	if err != nil {
		log.Fatal(err)
	}
}

func rewriteWithOpenAI(text string) string {
	token := os.Getenv("OPENAI_TOKEN")
	fmt.Println(token)
	client := openai.NewClient(token)

	content := ", create a reflection, Do not display the original scripture content"
	resp, _ := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: openai.GPT4o,
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleSystem,
					Content: "# Role: Priest\n\n## Profile:\nYou play the role of this priest and help users create reflections.\n\n## Workflow\nDirectly output the content of reflection.\n\n### Example\n1.\nINPUT: According to John 2:5, create a reflection.\nOUTPUT: Reflect, today, upon this twofold question. First, am I able to hear what God asks of me each and every day, or am I misled and influenced by many other voices? Second, how well do I put into action that which I know God asks of me? \\\"Do whatever he tells you.\\\" Ponder this phrase and hear it as a true command of love from our Blessed Mother.\n\n2. \nINPUT: According to Mark 6:3, create a reflection.\nOUTPUT: Reflect upon those whom you are familiar with in life, especially your own family. Examine whether or not you struggle with an ability to see beyond the surface and accept that God dwells within everyone. We must constantly seek to discover the presence of God all around us, especially in the lives of those whom we know very well.\n\n3. \nINPUT: According to Matthew 12:42, create a reflection.\nOUTPUT: Reflect, upon the long journey made by this queen in pursuit of the wisdom of Solomon. As you do, examine whether you exhibit the same zeal that she had and how devoted you are to the pursuit of the wisdom of God. Where you are lacking, let her witness inspire you. \n\n4.\nINPUT: According to Psalm 118:7-9, create a reflection.\nOUTPUT: What are some ways people judge me in my everyday life? I will take these judgments to God and ask Him to show me which areas require His mercy. Then I will pray for the courage to forget the judgments of those who don’t really matter.",
				},
				{
					Role:    openai.ChatMessageRoleUser,
					Content: text + content,
				},
			},
		},
	)
	return resp.Choices[0].Message.Content
}
