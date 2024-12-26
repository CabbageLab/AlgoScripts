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
	"strings"
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
	file, err := xlsx.OpenFile("./Golang_Basis/tts/reading_plan/tough_love/content/faith_content.xlsx")
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
		introduction_key := row.Cells[0].String()
		introduction_key_for := strings.TrimSpace(introduction_key)
		if introduction_key_for == "" || len(introduction_key_for) == 0 {
			break
		}
		introduction_key_for = strings.ReplaceAll(introduction_key_for, " ", "_")
		introduction_key_for = strings.ReplaceAll(introduction_key_for, ":", "_")
		introduction_content := row.Cells[1].String()
		introduction_content = introduction_key + "\n <break time=\"1000ms\" /> " + introduction_content
		fmt.Println(introduction_key)
		fmt.Println(introduction_key_for)
		fmt.Println(introduction_content)
		fmt.Println("=============")
		handleTTS3(introduction_key_for, introduction_content)
	}

}

func handleTTS3(introduction_key, prayer string) string {
	voiceRate := "-10%"
	ssml := fmt.Sprintf(`
    <speak version='1.0' xml:lang='en-US'>
        <voice xml:lang='en-US' xml:gender='Female' name='en-US-AvaMultilingualNeural'>
           	<prosody rate="%s">
             	%s
			<break time="2000ms" />
			</prosody>
        </voice>
    </speak>
    `, voiceRate, prayer)

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
	keyName := fmt.Sprintf("wepray_business/reading_plan/tough_love/%s.mp3", introduction_key)
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

	DOMAIN_FF := os.Getenv("DOMAIN_FF")

	fileURL := fmt.Sprintf("%s/%s", DOMAIN_FF, keyName)
	fmt.Printf("Audio file uploaded successfully. File URL: %s\n", fileURL)
	// 打开文件，如果文件不存在则创建，文件存在则追加内容
	file_txt, err := os.OpenFile("./Golang_Basis/tts/reading_plan/tough_love/content/urls.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	// 创建一个新的写入器
	writer := bufio.NewWriter(file_txt)
	writer.WriteString(fileURL + "\n")
	writer.Flush()
	file_txt.Close()
	return fileURL
}
