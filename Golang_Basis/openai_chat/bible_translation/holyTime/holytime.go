package main

import (
	"context"
	"fmt"
	"github.com/sashabaranov/go-openai"
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
	//file, err := xlsx.OpenFile("./Golang_Basis/openai_chat/bible_translation/holyTime/HolyTime.xlsx")
	//if err != nil {
	//	log.Fatal(err)
	//}
	//
	//// 读取第一个工作表
	//sheet := file.Sheets[0]
	//fmt.Println(sheet)
	//// 遍历所有行
	//for rowIndex, row := range sheet.Rows {
	//	if rowIndex == 0 { // 跳过标题行
	//		continue
	//	}
	//
	//	// 读取"Chapter and Verse"列，这里假设是第4列（列索引从0开始）
	//	if len(row.Cells) <= 1 {
	//		continue
	//	}
	//	originalText := row.Cells[1].String()
	//	fmt.Println(originalText)
	//	// 如果originalText为空/空字符 则跳过
	//	if originalText == "" {
	//		continue
	//	}
	//	// 调用OpenAI API进行重写
	//	rewrittenText_de := rewriteWithOpenAI(originalText, "de")
	//	rewrittenText_fr := rewriteWithOpenAI(originalText, "fr")
	//	fmt.Println(rewrittenText_de)
	//	fmt.Println(rewrittenText_fr)
	//	//将重写后的数据写回到Excel的同一列
	//	row.Cells[2].Value = rewrittenText_de
	//	row.Cells[3].Value = rewrittenText_fr
	//
	//	//保存修改后的Excel文件
	//	err = file.Save("./Golang_Basis/openai_chat/bible_translation/holyTime/HolyTime_de_fr_lent.xlsx")
	//	if err != nil {
	//		log.Fatal(err)
	//	}
	//}
	originalText := "As we delve into today's readings, we find ourselves immersed in the themes of love, commitment, and the essence of God's commandments. These scriptures hold profound lessons that resonate with us as we journey through Lent: A Journey to the Cross. Let's reflect on what these passages reveal.\n\nDeuteronomy 6:1-9 calls attention to one of the most central affirmations in Judaism, the Shema. This passage emphasizes the importance of loving God wholeheartedly, with every fiber of our being—heart, soul, and strength. Moses instructs the Israelites to keep these commandments close, teaching them diligently to their children, speaking of them when sitting at home and when out walking, when lying down, and when rising up. This constant mindfulness suggests that our faith should permeate every aspect of our daily lives. It's a reminder that loving God isn't an occasional act but a continual state of being. As we contemplate these words, we might ask ourselves how we incorporate our love for God into the mundane routines of our own lives. Do we take moments throughout our day to reflect on His presence and His commandments?\n\nIn Matthew 22:34-40, Jesus is approached by a Pharisee, testing Him with the question of which commandment in the law is the greatest. Jesus responds with clarity, elevating the commandment to love God with all your heart, soul, and mind as the greatest. He then links it with a second, equally important command: to love your neighbor as yourself. These two commandments encapsulate the entirety of the law and the prophets, serving as the foundation of Christian ethics. This passage invites us to examine whether we balance these commandments in our own lives. It challenges us to consider how we can better express our love for God through our interactions with others. Are there ways we can extend grace and kindness in everyday situations that might otherwise frustrate us?\n\n1 John 4:7-21 further explores this theme of love, urging us to love one another because love is from God, and everyone who loves is born of God and knows God. The passage eloquently states that God is love, and those who abide in love abide in God. This profound truth underscores the idea that our ability to love others is a direct reflection of our connection to God. The text encourages us to look beyond superficial actions, highlighting that true love casts out fear and that perfect love manifests through God's presence within us. In an era where fear often seems pervasive, how can we let love guide us instead? How might embracing this divine love transform not only our personal journeys but also the communities we are a part of?\n\nThese scriptures weave together a tapestry of divine love and human responsibility. They remind us that the essence of our faith is love—a love that compels us to draw nearer to God and to one another. The Shema's call for wholehearted devotion, Jesus' intertwining of love for God and neighbor, and John's reflection on love as a defining characteristic of the divine life all coalesce into a message both challenging and comforting.\n\nAs we move through Lent, reflecting on Christ's sacrifice and preparing our hearts for Easter, let these teachings inspire us to live more fully in the light of God's love. Like the Israelites instructed to bind God's words on their hands and foreheads, we too are called to visibly carry our faith into the world. Consider the subtle yet profound influence of consistently living out these commandments in our daily interactions. Small acts of love and kindness, rooted in our devotion to God, have the power to transform lives, including our own.\n\nIn closing, ponder this: How does the recognition of God's love influence your perception of self-worth and purpose? Can you identify areas of your life where love could replace fear, fostering a deeper relationship with God and those around you? As we close today's session, may these reflections guide you to embrace the transforming power of love, allowing it to shape your journey forward. Let the warmth of God's love illuminate your path as you continue this Lenten journey. I look forward to our next session, where we'll uncover more of these timeless truths. Until then, may peace and love be your companions."
	rewrittenText_fr := rewriteWithOpenAI(originalText, "fr")
	fmt.Println(rewrittenText_fr)
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
