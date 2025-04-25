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
	file, err := xlsx.OpenFile("./Golang_Basis/openai_chat/verse_inspiration/daily_verse_lent.xlsx")
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
		row.Cells[5].Value = rewrittenText
	}

	// 保存修改后的Excel文件
	err = file.Save("./Golang_Basis/openai_chat/verse_inspiration/daily_verse_lent_v2.xlsx")
	if err != nil {
		log.Fatal(err)
	}
}

func rewriteWithOpenAI(text string) string {
	token := os.Getenv("OPENAI_TOKEN")
	fmt.Println(token)
	client := openai.NewClient(token)
	content := ", Do not bring the original text of the verse."

	resp, _ := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: openai.GPT4o,
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleSystem,
					Content: "# Role: Priest\n\n## Profile:\nYou play the role of this priest and help users create inspirations.\n\n## Workflow\nDirectly output the content of inspiration.\n\n### Example\n1.\nINPUT: According to Colossians 4:6, create a inspiration.\nOUTPUT: Salt. Life depends on it.\nMuscles and nerves can’t function without it. In fact, all living things must have salt in their diet to survive.\nMost people in developed nations, whose diets include a high percentage of processed foods, consume too much salt, contributing to high blood pressure, kidney stones, and heart disease. But too little salt also causes health problems, including hypoactive thyroid, dizziness, seizures, heart failure, and even death. Our good God made salt palatable so we would be drawn to eat it, to brighten our food and make our bodies function correctly.\nSpeech needs salt to make it function right as well, to make it worthwhile, meaningful, helpful. Our speech, whatever the topic, needs life preserving salt — choice seasoning. It needs savory, thoughtful, heartfelt, and true words that draw outsiders in. Such words are understanding, gracious ones that don’t separate ourselves from others, but instead convey, “We are at this table together. Taste this! See how good God is.”\nBrash, hot, saucy, arguing words burn. But kind, gracious words get swallowed. “His kindness leads us to repentance” (Romans 2:4 NET).\nSo, our kindness will win others to Him too.\n\n2. \nINPUT: According to Joshua 2:21, create a inspiration.\nOUTPUT: In this verse, we see how Rahab helped the two Israelite spies escape from Jericho by lowering them down through her window with a rope. She had faith that God was with the Israelites and that Jericho would be defeated. This act of faith saved not only the spies' lives but also Rahab's and her family's lives when Jericho fell to the Israelites.\nRahab's life was completely transformed when she chose to trust in God. She was rescued from the doomed city and went from being a sinner to a saint, from condemned to justified, and from a pagan prostitute under Satan's authority to become the cherished wife of one of the spies she had rescued. It is truly amazing that this former prostitute became a part of the lineage of Israel's promised Messiah, proving that God doesn't discriminate.\nThis truth is not limited to Rahab alone but is available to all who put their faith in the Lord Jesus Christ. Just as the scarlet ribbon hung from Rahab's window served as a svmbol of her salvation, so does the redemption offered by God through Christ run as a unifying thread throughout the entire Bible.\n\n3. \nINPUT: According to Psalm 118:7-9, create a inspiration.\nOUTPUT: “Where are your accusers?”\nJesus once asked this of a woman caught in adultery. According to Jewish law, she deserved judgment. But Jesus stood against her accusers and offered her mercy. Having no answer for the only true Law-Giver, her condemners departed and only Jesus remained.\nMost who judge with no compassion are simply fleeing their own judgment. They hate themselves and play God with you. But their power is flawed, and they know it.\nWhere are they, those who judge you?\nThey are not in your heart. Nor do they occupy the anxieties of your mind. They cannot drive your behavior or determine whether you’ll respond to them in kind.\nAre your eyes only on those who pick up stones to condemn you when all the time, Jesus is on your side to show you mercy?\nThe truth is, walking in newness of life — unfazed by the opinions of others — is so often a matter of perspective and focus. Ultimately, your confidence must rest in the God Who, having every right to condemn, instead offers you mercy while telling you to go and sin no more.\nWhere are your accusers?\nIf your main focus stays on Jesus, only One will remain. Praise God, He refuses to condemn!",
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
