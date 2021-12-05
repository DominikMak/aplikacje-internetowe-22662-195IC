# Laboratorium nr 4 - REST API z DRF
## Stworzyłem api odpowiadające za obsługę postów na blogu jak i użytkowników tego bloga.
1. Widok panelu administratora zawiera wszystkie utworzone modele:
* Adresy E-mail,
* Tokeny,
* Użytkownicy i grupy,
* Posty,
![1](zrzuty/1.PNG)
2. Został utworzony interfejs REST API.
![2](zrzuty/2.PNG)
* Widoczna jest lista utworzonych postów. Dane dotyczące postów wyświetlane są dzięki serializerowi:
    - id: id posta tworzona automatycznie,
    - autor: id autora,
    - title: tytuł posta,
    - body: treść posta,
    - created_at: dane odnośnie czasu utworzenia posta.
* Poniżej widoczna jest opcja dodania nowego posta:
![3](zrzuty/3.PNG)
![4](zrzuty/4.PNG)
* Po wybraniu opcji 'GET -> JSON' dane wyświetlane są w postaci obiektu JSON.
![5](zrzuty/5.PNG)
![6](zrzuty/6.PNG)
* Po wylogowaniu się, jako niezalogowany użytkownik mogę wyświetlić listę postów jednak nie mam dostępu do edycji poszczególnych postów np. (/api/v1/1):
![7](zrzuty/7.PNG)
![8](zrzuty/8.PNG)
![9](zrzuty/9.PNG)
* Widoczna jest również lista użytkowników:
![10](zrzuty/10.PNG)
* Poniżej znajduje się możliwość dodania nowego użytkownika.
![11](zrzuty/11.PNG)
![12](zrzuty/12.PNG)
3. Po przejściu pod adres "/docs/" wyświetlana jest dokumentacja utworzonego API wraz z możliwością testowania poszczególnych elementów.
![14](zrzuty/14.PNG)
![15](zrzuty/15.PNG)
![16](zrzuty/16.PNG)
4. 'Swagger' został również skonfigurowany dla aplikacji: 
![17](zrzuty/17.PNG)
* Przykład testowania:
![18](zrzuty/18.PNG)
![19](zrzuty/19.PNG)