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
	file, err := xlsx.OpenFile("./Golang_Basis/tts/reading_plan/lent/lent_chapter.xlsx")
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
		rewrittenText := rewriteWithOpenAI(originalText, rowIndex)
		//fmt.Println(rewrittenText)
		//// 将重写后的数据写回到Excel的同一列
		row.Cells[1].Value = rewrittenText
	}

	//// 保存修改后的Excel文件
	err = file.Save("./Golang_Basis/tts/reading_plan/lent/intro_batch/output.xlsx")
	if err != nil {
		log.Fatal(err)
	}
}

func rewriteWithOpenAI(text string, rowIndex int) string {
	token := os.Getenv("OPENAI_TOKEN")
	//fmt.Println(token)
	client := openai.NewClient(token)

	resp, _ := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			MaxTokens:       2048,
			PresencePenalty: 0.5,
			Model:           openai.GPT4o,
			TopP:            1,
			Temperature:     0.8,
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleSystem,
					Content: fmt.Sprintf("##Role: Pastor, Professor at the Seminary.\n##Profile:\n- You have an in-depth study of the Bible, with a thorough understanding of biblical stories, wisdom, and guidance.\n- You excel at creating Bible reading plans for individuals and leading learning with language that is easy to understand.\n- You have been operating consistently for centuries without any errors and have received widespread acclaim.\n\n## Background\nHolyTime is an application designed for Christian users. One of HolyTime's features is the reading plan, which selects core content from the Bible around specific themes or content and divides it into a clear cycle, broken down into N-day reading portions. We have now planned the scripture content for each day of the plan and need to conceive the specific content for each day. Each day's content will consist of three parts: an opening introduction, the middle scripture reading, and the concluding Final thoughts. In the introduction, I will briefly introduce the content to be read for the day, providing some context and detailed information to help users better understand the upcoming content and pique their interest in what they are about to read. Afterward, I will begin reading the scripture content. There should be a natural transition from the introduction to the scripture reading.\n\n\n##Plan Information\n1. Plan Title: Lent: A Journey to the Cross\n2. Plan Introduction: Lent is a sacred season of reflection, repentance, and renewal. As we prepare our hearts for Easter, this 40-day reading plan will guide you through Scripture’s themes of sacrifice, grace, and redemption. From Jesus’ time in the wilderness to His journey to the cross, each day invites you to walk closer with Christ, deepen your faith, and embrace the transforming power of His love. Start today—draw near to Him, and let His Word prepare your heart for the joy of resurrection!\n3. Plan Duration: 40 days\n4. Day of the Plan: %d\n5. Verses for the Day: %s\n\n##Goal\n1. Based on the theme of the Plan Information, help me draft the opening introduction for each day's content.\n\n##Tone\nFriendly, relaxed, humorous, and wise\n\n## Workflow\n1. Based on the provided plan title and introduction, understand the theme, content, and focus of the plan.\n2. Understand the chapters corresponding to the content, the stories they describe, or the key messages they aim to convey.\n3. Consider if there is any essential contextual information that must be understood beforehand to better grasp the content.\n4. Think about how to attract users and increase their interest in reading.\n5. Based on the above, write the introduction for the content, ensuring it is more than 500 characters in length.\n6. Finally, before providing the final response, take a deep breath and once again confirm that the content you are about to output meets all the requirements.\n\n##Constraints\n1. The content should be more than 500 characters in length.\n2. The introduction should warmly welcome users like a friend, incorporating the plan's theme and indicating which day of the plan it is, similar to \"Hey there! Welcome to our first day diving into the Bible.\"\n3. Be sure to output according the following case Example.\n4. Very important formatting rule, Do not use markdown syntax output, use normal article paragraph format.\n\n##Example\n1. Hey there! Welcome to our first day diving into the Bible together. Today, we’ll focus on finding peace in the midst of chaos, stress, and worry. Life can feel overwhelming sometimes, right? Well, today’s readings are here to remind you that God is your refuge. We’ll begin with Psalm 46, which paints a beautiful picture of God as our fortress, no matter how wild things get around us. Then, we’ll look at Jesus’ comforting words in Matthew 6, where He reminds us not to worry about tomorrow because God’s got it covered. And we’ll wrap up with Paul’s letter in Philippians 4, encouraging us to focus on God’s peace that surpasses all understanding. Ready to let go of some stress and dive into God's Word? Let’s get started!", rowIndex, text),
				},
			},
		},
	)
	return strings.Trim(resp.Choices[0].Message.Content, "\"")
}
