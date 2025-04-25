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
	file, err := xlsx.OpenFile("./Golang_Basis/openai_chat/bible_translation/daily_verse/daily_verse.xlsx")
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
		//将重写后的数据写回到Excel的同一列
		row.Cells[2].Value = rewrittenText_de
		row.Cells[3].Value = rewrittenText_fr
	}

	//保存修改后的Excel文件
	err = file.Save("./Golang_Basis/openai_chat/bible_translation/daily_verse/daily_verse_de_fr_v5.xlsx")
	if err != nil {
		log.Fatal(err)
	}
	//originalText := "As we delve into 2 Corinthians 11, we encounter a chapter that is both revealing and deeply personal, as the Apostle Paul fervently defends his apostleship. This passage offers much for us to absorb, so let's take a moment to explore its depths and uncover its relevance for our lives today.\n\nPaul begins by expressing his concern for the Corinthians, fearing that they have been led astray by false apostles who preach a different Jesus and gospel. Here, Paul is drawing a parallel to the deception of Eve by the serpent in the Garden of Eden. He warns the Corinthians, urging them to remain steadfast in their faith and not be swayed by those who distort the truth. This reminds us of the importance of discernment in our own spiritual journeys. In a world filled with diverse voices and teachings, how do we ensure that we remain anchored in the true gospel? Perhaps it requires a commitment to study and understand Scripture deeply, seeking guidance from trusted mentors and the Holy Spirit.\n\nNext, Paul lists his credentials, not in a boastful manner but as an appeal to his genuine commitment to the church. He speaks of his hardships, sacrifices, and sufferings for the sake of spreading the gospel. From imprisonments to being beaten and left for dead, Paul's experiences speak volumes about his dedication. This brings to mind the question: what are we willing to endure for our beliefs and values? Paul's life challenges us to evaluate what sacrifices we might need to make to remain faithful to our calling.\n\nMoreover, Paul uses a bit of irony and sarcasm, referring to the false apostles as \"super-apostles\" and critiquing their methods. He highlights the difference between his own humble approach and their self-aggrandizing ways. Here, we see a lesson on humility and authenticity. Paul's approach was never to glorify himself but to point others to Christ. How can we embody such humility in our own lives, ensuring that our actions reflect a genuine commitment to serving others rather than seeking personal gain or recognition?\n\nAs we continue through the chapter, Paul touches on the burden he feels for the churches, highlighting his deep concern for their spiritual well-being. This section is a poignant reminder of the responsibility that comes with leadership and mentorship. Whether we find ourselves in positions of influence within our communities, families, or workplaces, we are called to care deeply for those we lead. How can we better support and nurture those around us, just as Paul did for the Corinthians?\n\nIn reflecting on Paul's message, we might also consider the broader themes of perseverance and integrity. Paul's life and ministry were marked by unyielding dedication to the truth, despite the many trials he faced. His example encourages us to persevere in our own paths, trusting that our efforts are not in vain when rooted in love and truth.\n\nAs you meditate on these verses, think about how they apply to your own life. What does it mean for you to maintain integrity in the face of adversity? How can you ensure that your actions and words align with your faith, even when challenged by external pressures? Consider the moments when you might have been tempted to compromise your beliefs—how did you respond, and what might you do differently in the future?\n\nAs we close today's session, let Paul's unwavering commitment inspire you to hold fast to your convictions and embrace the call to serve others with humility and grace. May this chapter from 2 Corinthians deepen your understanding and strengthen your resolve to live out your faith with courage and compassion. I look forward to our next session, where we'll continue to explore the rich tapestry of teachings found within the New Testament. Until then, may your heart be filled with peace and your steps guided by wisdom."
	//rewrittenText_de := rewriteWithOpenAI(originalText, "de")
	//fmt.Println(rewrittenText_de)
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
