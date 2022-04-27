import sys
import time
def print_slow(text):
	for letter in text :
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.1)

	
print_slow('Kotlin Nerede Kullanılır?' "\n"
   'Kullanım alanı geniş olan bir dil olsa da Kotlin günümüzde en çok Android uygulamaların geliştirilmesinde kullanılıyor. VueJS ve ReactJS gibi popüler kitaplıkların kullanılmasına da olanak sağlayan yazılım dili, sunucu ve istemci taraflı geliştirmelerde de kullanılmaktadır.'"\n"
'Kolay ve anlaşılır bir yazılım dili olmasından dolayı Kotlin’in öğrenim süreci diğer yazılım dillerine kıyasla daha kısadır.'  "\n"
 ' Ayrıca, Google’ın desteğini arkasına alması ve yine Google’ın Android işletim sistemi için geleceğin dili olduğunu öngörmesinden dolayı popularitesi sürekli artan bir dildir. ' "\n"
 'Kotlin’in eksi yönleri olarak ise öğrenim kaynaklarının diğer popüler yazılım dillerine göre daha kısıtlı olması ve hala istenilen popülariteye ulaşmamış olması gösterilebilir.' "\n"
 'Fakat bunlara rağmen, hala Android tabanlı uygulama geliştiren veya geliştirmek isteyen developerlar için en iyi seçeneklerden birisi olarak görünüyor.')