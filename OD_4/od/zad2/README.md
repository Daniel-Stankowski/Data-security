php działał z uprawnieniami root (obrazek 1.png)



poprawki
adduser user
usermod -a -G www-data user
vim /etc/php/8.1/fpm/pool.d/www.conf

zmiana z:
user = www-data
group = www-data
na:
user = user
group = user

chown -R user:www-data /od/www/html/
 
po zmianach działał z uprawnieniami user, które można dostosować (obrazek 2.png)