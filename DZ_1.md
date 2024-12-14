## Разработать эмулятор для языка оболочки ОС. Вариант 19

Необходимо сделать работу эмулятора как можно более похожей на сеанс shell в UNIX-подобной ОС.
Эмулятор должен запускаться из реальной командной строки, а файл с
виртуальной файловой системой не нужно распаковывать у пользователя.
Эмулятор принимает образ виртуальной файловой системы в виде файла формата
zip. Эмулятор должен работать в режиме CLI.
Конфигурационный файл имеет формат xml и содержит:
• Имя компьютера для показа в приглашении к вводу.
• Путь к архиву виртуальной файловой системы.
• Путь к лог-файлу.
Лог-файл имеет формат csv и содержит все действия во время последнего
сеанса работы с эмулятором. Для каждого действия указаны дата и время.
Необходимо поддержать в эмуляторе команды: 
1. mkdir.
2. echo.
3. ls
4. cd
5. exit
Все функции эмулятора должны быть покрыты тестами, а для каждой из
поддерживаемых команд необходимо написать 2 теста.




## Создание zip

![Задание 1](https://github.com/teeeema/mingazutdinov.a.r/blob/main/DZ_1/1.jpg)

## Создание структуры эмулятора

![Задание 2](https://github.com/teeeema/mingazutdinov.a.r/blob/main/DZ_1/2.jpg)

## Прохождение тестов и запуск эмулятора

![Задание 3](https://github.com/teeeema/mingazutdinov.a.r/blob/main/DZ_1/3.jpg)
![Задание 3](https://github.com/teeeema/mingazutdinov.a.r/blob/main/DZ_1/4.jpg)
