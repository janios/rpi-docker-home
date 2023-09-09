# rpi-docker-home

Repo utilizado para configurar servidores en raspberry pi

Seguir los siguiente pasos

1.- Configurar ip fija

```
sudo nano /etc/dhcpcd.conf
```
```
interface eth0
static ip_address=192.168.3.30/24
static routers=192.168.3.1
static domain_name_servers=192.168.3.1 8.8.8.8 
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
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
echo "deb [arch=armhf] https://download.docker.com/linux/debian \
     $(lsb_release -cs) stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list
sudo apt-get update && sudo apt-get install -y --no-install-recommends docker-ce docker-compose
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
