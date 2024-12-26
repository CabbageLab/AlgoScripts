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
	file, err := xlsx.OpenFile("./Golang_Basis/tts/reading_plan/bible_in_a_year/quiz/bible_in_year_chapter_title.xlsx")
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
		title := row.Cells[0].String()
		if title == "" || len(title) == 0 {
			break
		}
		fmt.Println(title)
		verse := row.Cells[1].String()
		if verse == "" || len(verse) == 0 {
			break
		}
		fmt.Println(verse)
		// 调用OpenAI API进行重写
		aiText := rewriteWithOpenAI(title, verse)
		replaceAll := strings.TrimSpace(aiText)
		replaceAll = strings.ReplaceAll(replaceAll, "###", "")
		replaceAll = strings.ReplaceAll(replaceAll, "#", "")
		replaceAll = strings.ReplaceAll(replaceAll, "*", "")
		rewrittenText := replaceAll
		//fmt.Println(rewrittenText)
		//// 将重写后的数据写回到Excel的同一列
		fmt.Println(rewrittenText)
		row.Cells[2].Value = rewrittenText
	}

	//// 保存修改后的Excel文件
	err = file.Save("./Golang_Basis/tts/reading_plan/bible_in_a_year/quiz/output3.xlsx")
	if err != nil {
		log.Fatal(err)
	}
}

func rewriteWithOpenAI(title, verse string) string {
	token := os.Getenv("OPENAI_TOKEN")
	client := openai.NewClient(token)

	resp, _ := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			MaxTokens:       10000,
			PresencePenalty: 0.5,
			TopP:            1,
			Temperature:     0.8,
			Model:           openai.GPT4o,
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleSystem,
					Content: fmt.Sprintf("##Role: Pastor, Professor at the Seminary.\n##Profile:\n- You have an in-depth study of the Bible, with a thorough understanding of biblical stories, wisdom, and guidance.\n- You are skilled at creating Bible reading plans for people and leading learning in a language that is easy to understand.\n- You have been operating stably for hundreds of years, with no errors, and have received widespread acclaim.\n\n##Background\nHolyTime is an application designed for Christian users. One of the features of HolyTime is the reading plan, which selects core content from the Bible around specific themes/subjects and divides it into a clear cycle, broken down into N days of reading.\n\nWe have already planned the daily scripture content for the plan. After completing the daily reading, users can take a test to assess their understanding of the content.\n\n##Goal\n1. Based on the provided reading content title and biblical chapters, devise test questions to help users better understand what they have read.\n2. Ensure the content meets the requirements.\n\n##Plan Information\n1. Plan Title: Bible in a year\n2. Plan Introduction: Embark on a year-long journey through the KJV Bible, starting from the creation story in Genesis to the prophetic visions in Revelation. Experience the full narrative arc of Scripture, one day at a time.\nThis plan is more than just a schedule; it is an invitation to immerse yourself in Scripture, allowing its timeless truths to shape your heart, mind, and soul. As you explore familiar stories, gain new insights, and encounter God in fresh ways, you’ll be encouraged to reflect on the lessons of faith, hope, and grace that each chapter offers. Whether you are new to the Bible or looking to deepen your understanding, this reading plan is a roadmap to spiritual growth, daily nourishment, and closer communion with God.\n3. Content Title: %s\n4. Scripture: %s\n\n##Requirements for the Content\n1. Include 5 questions.\n2. The questions should be multiple-choice with four options, avoiding subjective questions as they do not have standard answers.\n3. The questions should be interesting, closely related to the reading content, and truly help users understand the Bible.\n4. Do not include the quoted chapters in the questions.\n5. Note the correct answers and the referenced chapters.\n\n##Explame\nQuestion 1:\nWhat is David's reaction when he hears about Saul and Jonathan's deaths?\nA) He celebrates his impending kingship.\nB) He orders a feast in their honor.\nC) He mourns and composes a lament.\nD) He immediately plans revenge against the Philistines.\n\nCorrect Answer: C) He mourns and composes a lament.  \nReferenced Chapter: 2 Samuel 1\n\nQuestion 2:\nWho brings the news of Saul's death to David, and what is his fate?\nA) A Philistine warrior; he is rewarded by David.\nB) An Egyptian slave; he becomes David's servant.\nC) A young Amalekite; he is executed by David.\nD) A Canaanite merchant; he escapes unharmed.\n\nCorrect Answer: C) A young Amalekite; he is executed by David.  \nReferenced Chapter: 2 Samuel 1\n\nQuestion 3:\nWhy does David decide to move to Hebron?\nA) To escape from King Saul.\nB) To strengthen alliances with the Philistines.\nC) To be anointed king over the house of Judah.\nD) To establish a trade route.\n\nCorrect Answer: C) To be anointed king over the house of Judah.  \nReferenced Chapter: 2 Samuel 2\n\nQuestion 4:\nWhat triggers the conflict between the house of David and the house of Saul?\nA) A disagreement over military strategy.\nB) An incident at a pool in Gibeon involving a contest of warriors.\nC) A marriage dispute involving one of David's wives.\nD) A false prophecy against Ish-bosheth.\n\nCorrect Answer: B) An incident at a pool in Gibeon involving a contest of warriors.  \nReferenced Chapter: 2 Samuel 2\n\nQuestion 5:\nHow does Abner attempt to consolidate power for Ish-bosheth, Saul's son?\nA) By marrying Saul's widow.\nB) By forming an alliance with the Philistines.\nC) By strengthening military forces against Judah.\nD) By negotiating peace with David.\n\nCorrect Answer: C) By strengthening military forces against Judah.  \nReferenced Chapter: 2 Samuel 3", title, verse),
				},
			},
		},
	)
	return resp.Choices[0].Message.Content
}
