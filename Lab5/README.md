### Laboratorium 5 - Web Scraping

Stworzyłem aplikację w Django pozwalającą na web scraping wybranych stron internetowych:

#### Wyszukiwanie wybranego elementu na wybranej stronie internetowej.
![1](mysite/webscraping/static/screenshots/1.PNG)

Po podaniu w formularzu adresu strony internetowej oraz nazwy elementu ('np. "div", "p", itp.) wyświetlone zostaną wszystkie podane elementy.

![2](mysite/webscraping/static/screenshots/2.PNG)

Jako przykład podałem moją ulubioną stronę internetową oraz wyszukałem element 'body'.

![3](mysite/webscraping/static/screenshots/3.PNG)

Po wybraniu opcji "wyszukaj" wyświetlana jest informacja na temat znalezionego elementu.
W tym przypadku element "body" zawiera jedynie tekst.

![4](mysite/webscraping/static/screenshots/4.PNG)

Kolejna zakładka umożliwia wyszukiwanie elementów na wybranej stronie internetowej za pomocą ID danego elementu.

![5](mysite/webscraping/static/screenshots/5.PNG)

Jako adres strony internetowej podałem stronę Wikipedi na temat "Web Scrapeingu". Jako ID elementu podałem "content" po wcześniejszym zbadaniu kodu źródłowego strony znalazłem element "div" o ID "content".

![6](mysite/webscraping/static/screenshots/6.PNG)

Po wciśnięciu przycisku wyszukaj wyświetlana jest zawartośc elementu DIV o ID "content".

![7](mysite/webscraping/static/screenshots/7.PNG)

Kolejna zakładka pozwala na wyszukiwanie elementu na podanej stronie który należy do podanej klasy.

![8](mysite/webscraping/static/screenshots/8.PNG)

Jako stronę wybrałem moją drugą ulubioną witrynę na której wyszukuję element "div" o klasie "inner-content".

![9](mysite/webscraping/static/screenshots/9.PNG)
![10](mysite/webscraping/static/screenshots/10.PNG)

Jak widać znaleziono 22 elementy div o klasie inner-content.

![11](mysite/webscraping/static/screenshots/11.PNG)

Ostatnia zakładka wyświetla wyniki pobrane z różnych stron internetowych za pomocą "Beautiful Soup", "lxml" oraz "XPath".
Powyżej znajduje się zrzut ekranu wyniku pobranego ze strony "zacniewski.github.io/about/" a konkretnie zawartości wybranego przeze mnie elementu "div".

![12](mysite/webscraping/static/screenshots/12.PNG)

Powyżej znajduje się kod zawarty w pliku "views.py" odpowiedzialny za pobranie powyższego wyniku.
Poprzez zbadanie kodu źródłowego strony skopiowałem "XPath" do interesującego mnie div'a po czym do zmiennej "byte_data" zapisywane są dane w postaci bajtów które następnie zapisywane są do zmiennej "source_code" po sparsowaniu. Po czym tworzona jest lista za pomocą ".xpath()" a interesujące mnie informacje są na pierwszym miejscu tej listy.

![13](mysite/webscraping/static/screenshots/13.PNG)

![14](mysite/webscraping/static/screenshots/14.PNG)

W analogiczny sposób pobierany jest przepis na spaghetti.

![15](mysite/webscraping/static/screenshots/15.PNG)
![16](mysite/webscraping/static/screenshots/17.PNG)

W kolejnym przykładzie ze strony sprzedającej firany pobierane jest pierwsze 20 (ze względu na dużą liczbę produktów) wyników zawierających nazwę firany oraz jej opis.

![17](mysite/webscraping/static/screenshots/16.PNG)

Za pomocą Beautiful Soup parsowana jest zawartość strony z firanami po czym tworzona jest lista elementów div które zawierają interesujące mnie informacje a następnie w pętli pobierane są kolejne nazwy oraz opisy produktów.

![18](mysite/webscraping/static/screenshots/18.PNG)

W ostatnim przykładzie pobieram ze strony w3schools.com całą zawartość sekcji "head".

![19](mysite/webscraping/static/screenshots/19.PNG)