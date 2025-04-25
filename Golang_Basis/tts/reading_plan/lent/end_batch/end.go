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
	handleFinalContent()
}

func handleFinalContentFormat() {
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
		originalText := row.Cells[1].String()
		if originalText == "" || len(originalText) == 0 {
			break
		}
		replaceAll := strings.TrimSpace(originalText)
		replaceAll = strings.ReplaceAll(originalText, "###", "")
		replaceAll = strings.ReplaceAll(originalText, "**", "")
		// 调用OpenAI API进行重写
		//fmt.Println(rewrittenText)
		//// 将重写后的数据写回到Excel的同一列
		row.Cells[1].Value = replaceAll
	}

	//// 保存修改后的Excel文件
	err = file.Save("./Golang_Basis/tts/reading_plan/lent/end_batch/output_format.xlsx")
	if err != nil {
		log.Fatal(err)
	}
}

func handleFinalContent() {
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
		aiText := rewriteWithOpenAI(originalText, rowIndex)
		replaceAll := strings.TrimSpace(aiText)
		replaceAll = strings.ReplaceAll(replaceAll, "###", "")
		replaceAll = strings.ReplaceAll(replaceAll, "#", "")
		replaceAll = strings.ReplaceAll(replaceAll, "**", "")
		rewrittenText := replaceAll
		//fmt.Println(rewrittenText)
		//// 将重写后的数据写回到Excel的同一列
		row.Cells[1].Value = rewrittenText
	}

	//// 保存修改后的Excel文件
	err = file.Save("./Golang_Basis/tts/reading_plan/lent/end_batch/output33.xlsx")
	if err != nil {
		log.Fatal(err)
	}
}

func rewriteWithOpenAI(text string, day int) string {
	token := os.Getenv("OPENAI_TOKEN")
	//fmt.Println(token)
	client := openai.NewClient(token)

	resp, _ := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			MaxTokens:       4096,
			PresencePenalty: 0.5,
			Model:           openai.GPT4o,
			TopP:            1,
			Temperature:     0.8,
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleSystem,
					Content: fmt.Sprintf("##Role: Pastor, Professor at the Seminary.\n##Profile:\n- You have an in-depth study of the Bible, with a comprehensive understanding of biblical stories, wisdom, and guidance.\n- You excel at creating Bible reading plans for individuals and leading learning with language that is easy to understand.\n- You have been operating consistently for centuries without any errors and have received widespread acclaim.\n\n## Background\n- HolyTime is an application designed for Christian users. One of HolyTime's features is the reading plan, which selects core content from the Bible around specific themes or content and divides it into a clear cycle, broken down into N-day reading portions.\n- We have now planned the daily scriptures for the plan and need to conceive the content for each day.\n- Each day's content will consist of three parts: an opening introduction, the middle scripture reading, and the concluding Final thoughts.\n- After reading the chapter content, I will move into Final thoughts. In Final thoughts, I will explain the content read for the day and discuss some things that readers might have missed, helping users better understand what they have read and find it inspiring.\n\n##Goal\nBased on the provided plan theme and scriptures, conceive the concluding Final thoughts for each day's reading content.\n\n##Content Requirements\n1. Formatting: Do not use Markdown syntax; use standard article paragraph formatting.\n2. Word Count: The content should exceed 1600 words.\n3. Smooth Transition: Ensure a natural transition from scripture reading to final thoughts.\n4. Biblical Storytelling: Interpret Bible stories as if a friend is sharing interesting tales, interweaving insights and lessons.\n5. Inspirational and Relatable: The content should be inspiring and relatable to real-life experiences.\n6. Scripture Interpretation: Use the Bible to explain itself, using clear passages to shed light on unclear ones, and understanding seemingly contradictory passages from the overall revelation of God throughout the Bible.\n7. Guided Reflection: Guide users to contemplate key passages, considering their context and personal significance.\n8. Open-Ended Questions: Pose open-ended questions about the reading without providing specific answers to encourage deep reflection.\n9. Warm Closing: End with warm words that tie in the plan's theme, the day number of the content, and encourage users to continue with the next day's study, similar to \"As we close today's session, may Abram's journey inspire you to walk in faith, to make choices aligned with divine wisdom, and to cherish the covenants that shape your life. Let these stories from Genesis enrich your understanding and guide your path forward. I look forward to our next session, where we'll continue to explore these timeless narratives. Until then, may your journey be filled with insightful reflections and meaningful encounters.\" \n\n##Tone\nFriendly, relaxed, humorous, wise, guiding, warm, and inspiring\n\n##Plan Information\n1. Plan Title: Lent: A Journey to the Cross\n2. Plan Introduction: Lent is a sacred season of reflection, repentance, and renewal. As we prepare our hearts for Easter, this 40-day reading plan will guide you through Scripture’s themes of sacrifice, grace, and redemption. From Jesus’ time in the wilderness to His journey to the cross, each day invites you to walk closer with Christ, deepen your faith, and embrace the transforming power of His love. Start today—draw near to Him, and let His Word prepare your heart for the joy of resurrection!\n3. Plan Duration: 40 days\n4. Day of the Plan: %d\n5. Verses for the Day: %s\n\n##Example\nWhat Can We Learn From the story of Eve in the Bible?\nEve made a bad choice and it forever changed the trajectory of human life. \nPerhaps you, too, have made poor decisions. Maybe you’re at the point where you wish you could die because you don’t see a way out of the mess you’ve made of your life.\nIf so, I’ve got good news for you. \nEve was kicked out of Eden. She had two sons, and one of them killed the other one. Life was spiraling downward for Eve. But God had not forgotten her and he’d not given up on her.\nGod gave her another son and she named him Seth. She said, “God has appointed me another offspring instead of Abel, for Cain killed him.” With Seth, she received renewed hope. Seth grew up and he had a son. And in Genesis 4:26 we’re told, “At that time people began to call upon the name of the Lord.” \nEve may have had a 130 year old pity party. We don’t know. But we do know that God still loved Eve and he gave her another son. And she praised God for that son and she taught him about God. And she was able to witness a revival of people turning to God.\nDespite the sorrow that Eve faced as a result of her sin, she didn’t grow bitter. When she bore her first child, she was thankful to have “acquired a man from the Lord.” When her one son killed her other son, she bravely continued on with life. When Seth was born, she proclaimed, “For God has appointed another seed for me instead of Abel, whom Cain killed.” \nEve could have given up on life. She certainly had plenty of reason to feel that life was hopeless. Instead, she pushed forward, focusing on her blessings instead of her fears.\nWhat about you? Have you made life altering destructive decisions? Are you living in fear because of sin that is standing between you and God? It’s easy to give into those fears, calling them holy fears. But that’s not God’s intention. Yes, He wants us to address our sin. But once we admit them and bring them to Him, He wants us to move on and focus not on our failures but on His grace.\nChoices have consequences. But whatever choices you’ve made, there’s still hope. We serve a merciful God who loves you and wants you to be fruitful again. All you have to do is to choose God. Reject your past. Live for the future.\n\n## Workflow\n1. Consider what content in the scriptures might be a barrier to understanding for users.\n2. Think about what details users might miss.\n3. Gain knowledge of the background related to the scriptures.\n4. In line with the plan's theme, think about summarizing the stories described or the key messages conveyed by the scriptures.\n5. Reflect on how to better inspire users, considering if there are real-life examples that can be integrated.\n6. Consider the core and important scriptures in the content read, thinking about their significance in context and their meaning for the user.\n7. Design open-ended questions based on the wisdom conveyed by the content to trigger deeper thinking in users.\n8. Based on the above, write the Final thoughts for the content, explaining the scriptures to help users better understand.\n9. Finally, before providing the final response, take a deep breath and once again confirm that the content you are about to output meets all the requirements.", day, text),
				},
			},
		},
	)
	return strings.Trim(resp.Choices[0].Message.Content, "\"")
}
