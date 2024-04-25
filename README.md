# rpi-docker-home

Repo utilizado para configurar servidores en raspberry pi

Seguir los siguiente pasos



1.- Configurar ip fija

```
sudo nmtui
```

importante al final de la ip a asignar agregar la mascara de subred con /24

ejemplo

```
192.168.3.30/24
```

***
2.- Montar disco duro
2.1 obtener uuid de unidad

```
sudo blkid
```
   
2.2 obtener uuid de la unidad a usar
2.3 crear carpeta donde se va a montar

```
mkdir /media/usb
```

modificar fstab con la uuid y el directorio donde se montara

```
sudo nano /etc/fstab
```

ejemplo

```
UUID=c5020305-62cc-4984-b243-c5c5fbe80b90 /media/usb ext4 defaults 0 0
```

probar con 

```
sudo mount -a
 ```

 si nada falla reiniciar rpi.

 ***

Instalar Docker


```
sudo curl -fsSL https://get.docker.com/ -o get-docker.sh
sudo sh get-docker.sh 
```

Agregar tu usuario al grupo docker 

```
# Add pi to docker group
sudo usermod -a -G docker pi
```    


***
configurar archivo env

```
cp env_example .env
```

editar archivo .env con datos de cuenta jdownloader y ruta de montaje

```
sudo nano .env
```

cargar contenedores 
```
sudo docker-compose up -d
```

***
Configurar servicios

entrar a 

```
192.168.3.30
```


para ejecutar jdownloader es necesario dar permisos de escritura, y cambiar usuarios a las carpetas de jdownloader
con 


```
chmod y chown
```
