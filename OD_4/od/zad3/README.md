normalne odpalenie poprzez komendę: (obrazek 1.png)  
uwsgi --socket 127.0.0.1:29000 -w demo:app  

uprawnienia root(uid == 0)  

odpalenie z ustawieniem uid  

uwsgi --socket 127.0.0.1:29000 -w demo:app --uid 1000  

uprawnienia użytkownika z uid == 1000 czyli user stworzony w poprzednim zadaniu (obrazek 2.png)  
