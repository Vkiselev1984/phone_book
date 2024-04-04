# PHONE BOOK
## _An electronic phone book in Python_

[![N|Solid](https://sun9-9.userapi.com/impg/NhiY1HWoXxlDtOZxKFmgjFmCTJJAc9D_F0xIuA/GStiEdExS2o.jpg?size=1280x1040&quality=96&sign=8ffd548d996f9c83d18af5189a20e34a&c_uniq_tag=jf6-E2DhKgGnt58x60BKRqkhWyr_gOlcvYNhhIhjhGY&type=album)]()

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/Vkiselev1984/phone_book)

The reference book was created in Python as a laboratory assignment for the lesson "Working with files"
Using the command line, the user can interact with the directory by entering commands:

- Add an entry to the directory: add_person
- Read entries: show_table
- Copy Entry: copy_person
- Copy the entire directory: copy_table
- Delete an entry: delete_person
- Clear the second table: clear_copy_table
- Show the copied reference book show_copy_table
- Exit: exit

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

**Free Software**

[PlDb]: <https://pypi.org/project/tabulate/>

