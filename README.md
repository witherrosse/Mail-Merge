## Mail Merge - How it works

This is a simple **mail merge program** that creates personalized letters. It takes a template letter and replaces a placeholder with names from a list.

### Project files

- `main.py` – the main script
- `Input/Names/invited_names.txt` – list of names (one per line)
- `Input/Letters/starting_letter.txt` – letter template with `[name]` placeholder
- `Output/ReadyToSend/` – folder where personalized letters are saved

### What is used

- File handling: `open()`, `read()`, `write()`, `readlines()`
- String methods: `replace()`, `strip()`
- `with` statement: to automatically close files
- f-strings: to create dynamic file names

### How it works

1. **Read names**  
   Opens `invited_names.txt` and reads all names into a list

2. **Read letter template**  
   Opens `starting_letter.txt` and reads the entire content

3. **Replace placeholder**  
   For each name in the list:
   - Removes extra spaces or new lines with `strip()`
   - Replaces `[name]` with the actual name
   - Creates a new letter

4. **Save new letter**  
   Writes the personalized letter to `Output/ReadyToSend/` folder  
   File name example: `letter_for_John.docx`

### Folder structure

```
Project/
├── main.py
├── Input/
│   ├── Names/
│   │   └── invited_names.txt
│   └── Letters/
│       └── starting_letter.txt
└── Output/
    └── ReadyToSend/
        ├── letter_for_John.docx
        ├── letter_for_Jane.docx
        └── ...
```

### Example

**starting_letter.txt:**
```
Dear [name],

You are invited to our party!

Best regards,
Team
```

**Output for name "John":**
```
Dear John,

You are invited to our party!

Best regards,
Team
```

### Features

- Automatically creates multiple personalized letters
- Keeps original template unchanged
- Works with any number of names
- Saves each letter as a separate file

---

Save time by automating personalized letters!
