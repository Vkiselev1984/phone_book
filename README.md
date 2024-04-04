# PHONE BOOK
## _An electronic phone book in Python_

[![N|Solid](https://sun9-9.userapi.com/impg/NhiY1HWoXxlDtOZxKFmgjFmCTJJAc9D_F0xIuA/GStiEdExS2o.jpg?size=1280x1040&quality=96&sign=8ffd548d996f9c83d18af5189a20e34a&c_uniq_tag=jf6-E2DhKgGnt58x60BKRqkhWyr_gOlcvYNhhIhjhGY&type=album)]()

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/Vkiselev1984/phone_book)

The reference book was created in Python as a laboratory assignment for the lesson "Working with files"
Using the command line, the user can interact with the directory by entering commands:

- Добавить запись в справочник: add_person
- Прочитать записи: show_table
- Скопировать запись: copy_person
- Скопировать весь справочник: copy_table
- Удалить запись: delete_person
- Очистить вторую таблицу: clear_copy_table
- Показать скопированный справочник show_copy_table
- Выйти: exit

## Features

- Import a HTML file and watch it magically convert to Markdown
- Drag and drop images (requires your Dropbox account be linked)
- Import and save files from GitHub, Dropbox, Google Drive and One Drive
- Drag and drop markdown and HTML files into Dillinger
- Export documents as Markdown, HTML and PDF

Markdown is a lightweight markup language based on the formatting conventions
that people naturally use in email.
As [John Gruber] writes on the [Markdown site][df1]

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually- written in Markdown! To get a feel
for Markdown's syntax, type some text into the left window and
watch the results in the right.

## Plugins

The reference book uses the tabulate module, which allows you to display tabular data beautifully. It is not included in the standard Python library, so tabulate needs to be installed:

| Plugin | README |
| ------ | ------ |
| tabulate 0.9.0 | [0.9.0][PlDb] |

```sh
python -m venv venv
venv\Scripts\activate   
pip install tabulate 
```


## License

MIT

**Free Software, Hell Yeah!**

[PlDb]: <https://pypi.org/project/tabulate/>

