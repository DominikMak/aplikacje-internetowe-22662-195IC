from django.shortcuts import render
from django.views.generic import TemplateView, ListView
import requests
from bs4 import BeautifulSoup
from lxml import html

class HomePageView(TemplateView):
    template_name = 'webscraping/home.html'

#znajdowanie elementu na stronie
def find_element(request):
    if request.method == "POST":
        link = request.POST.get('web_link', None)
        element = request.POST.get('element', None)
        url = link
        source=requests.get(url).text 
        all_links = []

        soup = BeautifulSoup(source, "html.parser")
        items = soup.find_all(element)
        amount = len(items)

        for i in items:
            id_elementu = i.get('id')
            id_elementu = id_elementu.strip() if id_elementu is not None else ""

            klasa = i.get('class')

            if klasa is None:
                klasa = ""

            text = i.text

            text = text.strip() if text is not None else ""

            href = i.get('href')
            href = href.strip() if href is not None else ""

            src = i.get('src')
            if src is None:
                src = ""

            alt = i.get('alt')
            alt = alt.strip() if alt is not None else ""

            content = i.get('content')
            content = content.strip() if content is not None else ""

            name = i.get('name')
            name = name.strip() if name is not None else ""

            all_links.append({"id_elementu": id_elementu, "klasa": klasa, "text": text, "href": href, "src": src, "alt": alt, "content": content, "name": name})

        return render(request, 'webscraping/search_results.html', {'all_links':all_links, 'amount': amount})

    return render(request, 'webscraping/home.html')


class FindIDView(TemplateView):
    template_name='webscraping/search_id.html'

def search_id(request):
    if request.method == "POST":
        website_link = request.POST.get('web_link', None)
        id_elementu = request.POST.get('idd', None)
        url = website_link
        source=requests.get(url).text
        soup = BeautifulSoup(source, "html.parser")

        item = soup.find(id=id_elementu)
        if item is not None:
            item = item.prettify()
            amount = 1
        else:
            item = ""
            amount = 0

        return render(request, 'webscraping/search_results_id.html', {'item':item, 'amount':amount})

    return render(request, 'webscraping/search_id.html')

class FindClassView(TemplateView):
    template_name='webscraping/search_class.html'

def search_class(request):
    if request.method == "POST":
        website_link = request.POST.get('web_link', None)
        klasa = request.POST.get('klasa', None)
        element = request.POST.get('element', None)
        url = website_link
        source=requests.get(url).text 
        all_links = []
        soup = BeautifulSoup(source, "html.parser")
        items = soup.find_all(element, class_=klasa)
        amount = len(items)

        for i in items:
            el = i.name

            id_elementu = i.get('id')
            id_elementu = id_elementu.strip() if id_elementu is not None else ""

            klasa = i.get('class')
            if klasa is None:
                klasa = ""

            text = i.text
            text = text.strip() if text is not None else ""

            href = i.get('href')
            href = href.strip() if href is not None else ""

            src = i.get('src')
            if src is None:
                src = ""
                
            alt = i.get('alt')
            alt = alt.strip() if alt is not None else ""

            content = i.get('content')
            content = content.strip() if content is not None else ""

            name = i.get('name')
            name = name.strip() if name is not None else ""
            
            all_links.append({"el": el,"id_elementu": id_elementu, "klasa": klasa, "text": text, "href": href, "src": src, "alt": alt, "content": content, "name": name})

        return render(request, 'webscraping/search_results_class.html', {'all_links':all_links, 'amount':amount})

    return render(request, 'webscraping/search_class.html')

#lxml scraping
def examples(request):
    #lxml przyklad 1
    url = 'https://zacniewski.github.io/about/'
    #xpath do wybranego elementu
    path = '//*[@id="layoutSidenav_content"]/main/div/div/div'
    #odpowiedz
    response = requests.get(url)

    byte_data = response.content

    source_code = html.fromstring(byte_data)

    tree = source_code.xpath(path)

    ex1 = tree[0].text_content()

    #przyklad 2
    url = 'https://www.bbcgoodfood.com/recipes/ultimate-spaghetti-carbonara-recipe'

    path = '//*[@id="__next"]/div[3]/main/div/div/div[1]/div[1]/div[2]/div[2]/div/section[2]/div'
    response = requests.get(url)
    byte_data = response.content
    source_code = html.fromstring(byte_data)
    tree = source_code.xpath(path)
    ex2 = tree[0].text_content()
    
    #przyklad 3 - firany
    page = requests.get(
    "https://www.eurofirany.com.pl/sklep-online/firany-1041"
    )
    soup = BeautifulSoup(page.content, "html.parser")
    items = []
    firany = soup.select("div.category")[:20]
    amount = len(firany)
    for firana in firany:
        name = firana.select("span.card-title-name")[0].text
        opis = firana.select("span.card-title-param")[0].text
        items.append({"name": name, "opis": opis })

    #przyklad 4
    page = requests.get("https://www.w3schools.com/htmL/html_head.asp")
    soup = BeautifulSoup(page.content, "html.parser")
    page_head = soup.head

    return render(request, 'webscraping/random.html', {'ex1': ex1, 'ex2': ex2, 'items': items, "amount": amount, "page_head": page_head })
