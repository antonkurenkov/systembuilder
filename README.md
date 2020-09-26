# Systembuilder

version: 0.9
![](.github/.README_images/demo.gif)
-----
## Описание проекта
Облачная CI/CD система для автоматизирования процесса сборки-доставки-тестирования кода на основе формально заданных параметров среды.

## Процесс установки
```
git clone https://github.com/antonkurenkov/systembuilder
pip install -r requirements.txt
pip install -e . (для запуска тестов)
```
## Запуск
При запуске передаем имя директории с помощью параметра ``` --path ``` и имя манифеста, который представлен в виде yaml файла. Структуру yaml файла можно увидеть в примере. На выходе мы получаем внутри директории status.json, который, к примеру, может подхватываться из вне с помошью github action.     

``` python app.py --path <path_to_package> --filename <name_of_YAML_file.yaml> ```  
### Рабочий пример: 
``` python app.py --path examples --filename info.yaml ```  
После запуска в директрии examples должен появиться докерфайл и status.json файл с информацией.
  
  
----------------------------------------------------------------------------------------------------------------------
### Status of last deployment:<br>
#### on-pull-request:<br>
<img src="https://github.com/antonkurenkov/systembuilder/workflows/on-pull-request/badge.svg?branch=develop"><br>
#### on-commit:<br>
<img src="https://github.com/antonkurenkov/systembuilder/workflows/on-commit/badge.svg?branch=develop"><br>
#### scheduler:<br>
<img src="https://github.com/antonkurenkov/systembuilder/workflows/scheduler/badge.svg?branch=develop"><br>

