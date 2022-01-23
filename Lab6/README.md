# Laboratorium nr 6 - Zezwolenia i uwierzytelnianie w DRF
1. Viewsets:
</br>Jako że jest to kontynuacja Laboratorium nr 4 to już w poprzednim zadaniu uwzględniłem obsługę viewsets do wyświetlania postów oraz listy użytkowników:
</br>

![1](zrzuty/1.PNG)

</br>

2. Routers:

</br>Podobnie jak w punkcie powyżej routers wykorzystałem w celu dodania ścieżki dla list postów oraz użytkowników:
</br>

![4](zrzuty/4.PNG)

</br>

3. Serializer:
</br> Serializer został wykorzystany dla utworzenia listy użytkowników oraz postów:
</br>

![5](zrzuty/5.PNG)

</br>

4. Uzyskany efekt:
</br>

![2](zrzuty/2.PNG)

</br>

![3](zrzuty/3.PNG)

</br>

5. Uwierzytelnianie:
W sekcji 'DEFAULT_AUTHENTICATION_CLASSES' pliku 'settings' dodane zostały:
* SessionAuthentication,
* TokenAuthentication,
</br>

![6](zrzuty/6.PNG)

</br>
Następnie w celu zaimplementowania Token Authentication należy dodać aplikację authtoken w pliku settings:
</br>

![7](zrzuty/7.PNG)

</br>
Po dokonaniu powyższych kroków w panelu administratora pojawia się sekcja Tokens w której przechowywane będą tokeny wykorzystywane przy logowaniu oraz wylogowywaniu użytkowników:
</br>

![8](zrzuty/8.PNG)

</br>
Kolejnym krokiem jest umożliwienie logowania oraz wylogowania użytkownika w tym celu w pliku settings dodane zostało 'rest_auth':
</br>

![9](zrzuty/9.PNG)

</br>
Po czym w pliku 'urls' dodana została ścieżka do 'rest_auth':
</br>

![10](zrzuty/10.PNG)

</br>
Po dodaniu tej ścieżki do pliku urls możliwe staje się logowanie oraz wylogowanie użytkownika poprzez ścieżki:
* ../rest-auth/login/
* ../rest-auth/logout/
</br>

![11](zrzuty/11.PNG)

</br>

![12](zrzuty/12.PNG)

</br>
Jak widać logowanie przebiegło prawidłowo a w wyniku uzyskujemy token sesji użytkownika:
</br>

![13](zrzuty/13.PNG)

</br>

![14](zrzuty/14.PNG)

</br>
Jak widać wylogowanie użytkownika również przebiegło bez zarzutu.
</br>

![15](zrzuty/15.PNG)

</br>
A token sesji użytkownika dłużej nie istnieje w zakładce Tokens w panelu administratora.

Oraz resetowanie hasła użytkownika poprzez:
* ../rest-auth/password/reset
</br>

![16](zrzuty/16.PNG)

</br>

Następnie w celu utworzenia możliwości rejestracji nowego użytkownika wykorzystuję django-allauth oraz django.contrib.sites:

</br>

![17](zrzuty/18.PNG)

</br>

![18](zrzuty/19.PNG)

</br>

W celu wysyłania wiadomości E-mail potwierdzającej reset hasła wykorzystałem django.core.mail.backends:
</br>

![20](zrzuty/20.PNG)

</br>

Dzięki tym krokom po przejściu we wcześniej zdefiniowaną ścieżkę otrzymuje możliwość zarejestrowania nowego użytkownika:

</br>

![21](zrzuty/21.PNG)

</br>

![22](zrzuty/22.PNG)

</br>

![23](zrzuty/23.PNG)

</br>

Jak widać rejestracja przebiegła pomyślnie a po zarejestrowaniu się w konsoli pojawia się treść Maila potwierdzającego rejestracje.

6. Prosty licznik odwiedzin strony z wykorzystaniem cookies:

W celu stworzenia licznika utworzyłem nowy widok o nazwie 'counter' po uprzednim zaimportowaniu bibliotek:

* `from datatime import datetime`
* `from django.http import HttpResponse`

</br>

![24](zrzuty/24.PNG)

</br>

Po uprzednim dodaniu ścieżki w pliku 'url': `path('', counter, name="counter")`

Po odwiedzeniu strony po raz pierwszy wyświetlona zostanie informacja: `Witaj nieznajomy!` a po każdym kolejnym odświeżeniu strony będzie wyświetlała się informacja o liczbie odwiedzeń:
</br>

![25](zrzuty/25.PNG)

</br>

![26](zrzuty/26.PNG)