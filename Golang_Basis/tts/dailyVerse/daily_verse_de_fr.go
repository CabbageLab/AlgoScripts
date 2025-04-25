package main

import (
	"bufio"
	"bytes"
	"fmt"
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/credentials"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3"
	"github.com/tealeg/xlsx"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/09/10 11:38
    @题目     :
    @参考     :
    @时间复杂度:
    @空间复杂度:

 数据范围:

*/

func main() {
	//prayer := ""
	file, err := xlsx.OpenFile("./Golang_Basis/tts/dailyVerse/daily verse_de_fr.xlsx")
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
		name := row.Cells[0].String()
		prayer_en := row.Cells[1].String()
		prayer_de := row.Cells[2].String()
		prayer_fr := row.Cells[3].String()
		if name == "" || len(name) == 0 {
			break
		}
		fmt.Println(name)
		fmt.Println(prayer_en)
		handleTTS3(name, prayer_en, "en")
		handleTTS3(name, prayer_de, "de")
		handleTTS3(name, prayer_fr, "fr")
	}

}

// 常量en_ssml
var en_ssml = `
<speak version='1.0' xml:lang='en-US'>
        <voice xml:lang='en-US' xml:gender='Female' name='en-US-AvaMultilingualNeural'>
           %s
        </voice>
</speak>
`

// 常量de_ssml
var de_ssml = `
<speak version='1.0' xml:lang='de-DE'>
    <voice xml:lang='de-DE' xml:gender='Female' name='de-DE-SeraphinaMultilingualNeural'>
       %s
    </voice>
</speak>
`

// 常量fr_ssml
var fr_ssml = `
<speak version='1.0' xml:lang='fr-FR'>
    <voice xml:lang='fr-FR' xml:gender='Female' name='fr-FR-DeniseNeural'>
		<prosody rate="%s">
			%s
		</prosody>
    </voice>
</speak>
`

func handleTTS3(introduction_key, introduction_content, language string) string {
	ss := ""
	ssml := ""
	if language == "de" {
		ss = de_ssml
		ssml = fmt.Sprintf(ss, introduction_content)

	} else if language == "fr" {
		ss = fr_ssml
		voiceRate := "-15%"
		ssml = fmt.Sprintf(ss, voiceRate, introduction_content)
	} else {
		ss = en_ssml
		ssml = fmt.Sprintf(ss, introduction_content)
	}

	fmt.Println(ssml)
	tts_key := os.Getenv("TTS_KEY")
	fmt.Println(tts_key)
	// Define the headers
	headers := map[string]string{
		"X-Microsoft-OutputFormat":  "audio-24khz-96kbitrate-mono-mp3",
		"Content-Type":              "application/ssml+xml",
		"Ocp-Apim-Subscription-Key": tts_key,
	}

	url := "https://westus.tts.speech.microsoft.com/cognitiveservices/v1"
	req, err := http.NewRequest("POST", url, bytes.NewBuffer([]byte(ssml)))
	if err != nil {
		log.Fatalf("Error creating request: %v", err)
	}
	for key, value := range headers {
		req.Header.Set(key, value)
	}

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		log.Fatalf("Error making request: %v", err)
	}
	defer resp.Body.Close()

	audioData, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalf("Error reading response body: %v", err)
	}

	// Define AWS S3 credentials
	bucketName := os.Getenv("BUCKET_NAME")
	keyName := fmt.Sprintf("wepray_business/verse_lent/%s/%s.mp3", language, introduction_key)
	accessKeyID := os.Getenv("ACCESS_KEY_ID")
	secretAccessKey := os.Getenv("SECRET_KEY")
	regionName := "us-west-1"

	// Create an S3 client
	sess, err := session.NewSession(&aws.Config{
		Region:      aws.String(regionName),
		Credentials: credentials.NewStaticCredentials(accessKeyID, secretAccessKey, ""),
	})
	if err != nil {
		log.Fatalf("Error creating AWS session: %v", err)
	}
	s3Client := s3.New(sess)

	// Upload the audio data to S3
	_, err = s3Client.PutObject(&s3.PutObjectInput{
		Bucket:      aws.String(bucketName),
		Key:         aws.String(keyName),
		Body:        bytes.NewReader(audioData),
		ContentType: aws.String("audio/mpeg"),
	})
	if err != nil {
		log.Fatalf("Error uploading to S3: %v", err)
	}

	domain_ff := os.Getenv("DOMAIN_FF")
	fileURL := fmt.Sprintf("%s/%s", domain_ff, keyName)
	fmt.Printf("Audio file uploaded successfully. File URL: %s\n", fileURL)
	// 打开文件，如果文件不存在则创建，文件存在则追加内容
	file_txt, err := os.OpenFile("./Golang_Basis/tts/dailyVerse/prayer_fr_urls.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	// 创建一个新的写入器
	writer := bufio.NewWriter(file_txt)
	writer.WriteString(fileURL + "\n")
	writer.Flush()
	file_txt.Close()
	return fileURL
}
