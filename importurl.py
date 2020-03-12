import urllib.request

url1 = "https://www.google.com.tr/imgres?imgurl=http%3A%2F%2Fidora.milliyet.com.tr%2FYeniAnaResim%2F2017%2F02%2F28%2Fassassin-s-creed-empire-a-ait-yeni-gorseller-internete-sizdi-8645299.Jpeg&imgrefurl=http%3A%2F%2Fwww.milliyet.com.tr%2Fassassin-s-creed-empire-a-ait-teknoloji-haber-2404977%2F&docid=VyYjGhCvnOT5dM&tbnid=pHBagrrnaDQtIM%3A&vet=10ahUKEwjYoLXTq_DeAhXGkywKHXHvDecQMwiFASg_MD8..i&w=606&h=340&bih=626&biw=1366&q=g%C3%B6rseller&ved=0ahUKEwjYoLXTq_DeAhXGkywKHXHvDecQMwiFASg_MD8&iact=mrc&uact=8"
url2 = "https://wome.com.tr/images/galeri/genel-gorseller/3.jpg"
url3 = "https://wome.com.tr/images/galeri/genel-gorseller/1.jpg"
urllistesi = [url1,url2,url3]

say = 1

for url in urllistesi:
    urllib.request.urlretrieve(url,"Resim" + str(say)+".jpg")
    say+=1

    

