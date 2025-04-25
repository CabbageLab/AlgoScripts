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
	file, err := xlsx.OpenFile("./Golang_Basis/tts/reading_plan_de_fr/lent_intro.xlsx")
	if err != nil {
		log.Fatal(err)
	}

	// 读取第一个工作表
	sheet := file.Sheets[0]
	fmt.Println(sheet)
	// 遍历所有行
	for rowIndex, row := range sheet.Rows {
		if rowIndex <= 0 { // 跳过标题行
			continue
		}
		name := row.Cells[0].String()
		//将content_ 替换为空
		//name = strings.Replace(name, "content_", "", 1)
		prayer_en := row.Cells[1].String()
		prayer_de := row.Cells[2].String()
		prayer_fr := row.Cells[3].String()
		//en_text := row.Cells[1].String()
		if name == "" || len(name) == 0 {
			break
		}
		fmt.Println(name)
		fmt.Println(prayer_en)
		fmt.Println(prayer_de)
		fmt.Println(prayer_fr)
		//name := "christmas_intro_6"
		//prayer_de := "Hallo! Heute beschäftigen wir uns mit der Demut Jesu und den erstaunlichen Anstrengungen, die er für unsere Erlösung unternommen hat. Die Worte des Paulus im Philipperbrief werden uns dankbar machen, und der Hebräerbrief erinnert uns an die Vorherrschaft Christi. Lassen Sie uns darüber nachdenken, wie das Baby in der Krippe kam, um uns alle zu retten."
		handleTTS3(name, prayer_en, "en", "lent")
		handleTTS3(name, prayer_de, "de", "lent")
		handleTTS3(name, prayer_fr, "fr", "lent")
	}
	//name := "testament_final_166"
	//prayer_de := "Während wir die heutige Lesung von 1. Korinther 15 abschließen, nehmen wir uns einen Moment Zeit, um über die tiefgründigen Einsichten nachzudenken, die dieses Kapitel bietet. Es ist ein Abschnitt voller reicher theologischer Themen und praktischer Implikationen für unser tägliches Leben. Der Apostel Paulus spricht über den Kern des christlichen Glaubens: die Auferstehung Jesu Christi und ihre Bedeutung für die Gläubigen.\n\nIn 1. Korinther 15 verteidigt Paulus leidenschaftlich die Realität der Auferstehung. Dieses Kapitel wird oft als eines der wichtigsten im Neuen Testament angesehen, da es die fundamentale Rolle der Auferstehung im christlichen Glauben unterstreicht. Ohne dieses Eckereignis, so argumentiert Paulus, würde die gesamte Struktur des christlichen Glaubens zusammenbrechen. Er erläutert akribisch, dass die Auferstehung nicht nur ein historisches Ereignis ist, sondern ein entscheidender Akt, der Vergangenheit, Gegenwart und Zukunft transformiert.\n\nDas Kapitel beginnt damit, dass Paulus die Korinther Gemeinde an das Evangelium erinnert, das er gepredigt hat, das sie empfangen haben und in dem sie fest stehen. Er betont, dass Christus für unsere Sünden gestorben, begraben und am dritten Tag auferstanden ist, alles gemäß der Schrift. Diese prägnante Zusammenfassung unterstreicht die Erfüllung von Prophezeiungen und den göttlichen Plan, der durch das Leben, den Tod und die Auferstehung Jesu am Werk ist. Für viele Leser mag die Auferstehung wie ein abstraktes Konzept erscheinen. Paulus verankert sie jedoch in der Realität, indem er Augenzeugen aufzählt, die dem auferstandenen Christus begegnet sind, einschließlich seiner selbst. Diese greifbaren Beweise stärken das Vertrauen der Gläubigen in die Wahrheit der Auferstehung.\n\nEin Detail, das leicht übersehen werden könnte, ist die Erwähnung von Frauen unter den ersten Zeugen der Auferstehung, wie sie in den Evangelien erwähnt werden. In einem historischen Kontext, in dem die Zeugenaussagen von Frauen oft geringgeschätzt wurden, hebt diese Einbeziehung die radikale Natur der Botschaft des Evangeliums hervor und Gottes Wahl, seine bedeutendste Tat durch diejenigen zu offenbaren, die die Gesellschaft oft übersehen. Es fordert uns heraus, darüber nachzudenken, wen wir heute möglicherweise unterschätzen, und erinnert uns daran, dass Gottes Wahrheit aus unerwarteten Quellen kommen kann.\n\nDas Kapitel befasst sich auch mit den Konsequenzen der Auferstehung für die Gläubigen. Paulus argumentiert, dass, wenn es keine Auferstehung gibt, Christus nicht auferweckt wurde, und wenn Christus nicht auferweckt wurde, unser Glaube vergeblich ist. Diese klare Aussage lädt uns ein, über die Zentralität der Auferstehung in unserem eigenen Leben nachzudenken. Wie beeinflusst die Gewissheit des Lebens nach dem Tod unsere täglichen Entscheidungen und unser Denken?\n\nPaulus fährt fort, die transformative Kraft der Auferstehung zu erforschen. Das Bild des Samens, der sterben muss, um neues Leben hervorzubringen, illustriert schön das Konzept der Verwandlung. Diese Metapher ermutigt uns, über Bereiche in unserem Leben nachzudenken, in denen wir vielleicht loslassen oder bestimmte Aspekte „sterben“ lassen müssen, damit neues Leben entstehen kann. Welche alten Gewohnheiten, Ängste oder Zweifel müssen wir begraben, um die Fülle des Lebens zu erfahren, die Gott verspricht?\n\nDarüber hinaus spricht Paulus über den Auferstehungsleib und kontrastiert ihn mit unserer derzeitigen physischen Form. Er beschreibt ihn als unvergänglich, herrlich und kraftvoll – einen geistlichen Leib. Diese Hoffnung auf eine zukünftige Verwandlung gibt uns die Gewissheit, dass unsere gegenwärtigen Kämpfe und Begrenzungen vorübergehend sind. Sie inspiriert uns, mit einer ewigen Perspektive zu leben, in das zu investieren, was wirklich zählt, und an der Verheißung der Erneuerung festzuhalten.\n\nMit Paulus’ triumphaler Erklärung – „Der Tod ist verschlungen in den Sieg“ – werden wir eingeladen, uns unseren Ängsten und Unsicherheiten in Bezug auf den Tod zu stellen. In einer Zeit, in der der Tod oft von Angst und Vermeidung umgeben ist, bietet dieser Abschnitt eine Botschaft der Hoffnung und des Sieges. Er versichert uns, dass der Tod nicht das letzte Wort hat; vielmehr ist er ein besiegter Feind.\n\nBeim Nachdenken über diese Themen hier einige offene Fragen: Wie beeinflusst die Auferstehung Ihr Verständnis von Leben und Tod? Was bedeutet es für Sie persönlich, dass der Tod besiegt ist? Gibt es Bereiche in Ihrem Leben, in denen Sie die transformative Kraft der Auferstehung annehmen müssen, alte Dinge loslassen und neue Dinge entstehen lassen?\n\nSchließlich fordert uns Paulus in seinem Schlusswort in 1. Korinther 15:58 zum Handeln auf: „Daher, meine geliebten Brüder, seid standhaft, unerschütterlich, nehmt zu in dem Werk des Herrn allezeit, da ihr wisst, dass eure Arbeit nicht vergeblich ist im Herrn.“ Diese Ermahnung ermutigt uns, in unserem Glauben fest zu bleiben und im Dienst fleißig zu sein. Es ist eine Erinnerung daran, dass unsere Bemühungen, auch wenn sie manchmal unbemerkt oder ungewürdigt bleiben, von ewiger Bedeutung sind.\n\nZum Abschluss der heutigen Sitzung sollen uns die Themen Auferstehung und Verwandlung inspirieren, mit Hoffnung und Ziel zu leben. Möge die Gewissheit des Sieges über den Tod Sie dazu ermutigen, den Herausforderungen des Lebens mit Mut und Glauben zu begegnen. Morgen werden wir unsere Reise in die Tiefen des Neuen Testaments fortsetzen, um weitere Wahrheiten zu entdecken, die unseren Weg mit Gott leiten und formen. Bis dahin möge die Hoffnung auf die Auferstehung Ihr Herz mit Frieden und Freude erfüllen."
	//handleTTS3(name, prayer_de, "de", "testament")

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

func handleTTS3(introduction_key, introduction_content, language, prayer_name string) string {
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
	keyName := fmt.Sprintf("wepray_business/reading_plan/%s/%s/%s.mp3", language, prayer_name, introduction_key)
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
	file_txt, err := os.OpenFile("./Golang_Basis/tts/reading_plan_de_fr/reading_plan_fr_urls_lent.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	// 创建一个新的写入器
	writer := bufio.NewWriter(file_txt)
	writer.WriteString(fileURL + "\n")
	writer.Flush()
	file_txt.Close()
	return fileURL
}
