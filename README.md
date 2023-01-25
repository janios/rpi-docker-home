# rpi-docker-home

Repo utilizado para configurar servidores en raspberry pi

Seguir los siguiente pasos

1.- Configurar ip fija
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

    modificar fstba con la uuid y el directorio donde se montara

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

    





