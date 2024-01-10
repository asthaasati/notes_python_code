import json
import os
import mistune
from datetime import datetime

# File to store notes data
notes_file = 'notes.json'

# Check if the notes file exists, create it if not
if not os.path.exists(notes_file):
    with open(notes_file, 'w') as file:
        json.dump([], file)

def get_notes():
    with open(notes_file, 'r') as file:
        return json.load(file)

def save_notes(notes):
    with open(notes_file, 'w') as file:
        json.dump(notes, file)

def convert_markdown_to_html(markdown_content):
    markdown = mistune.Markdown()
    return markdown(markdown_content)

def create_note():
    notes = get_notes()
    note_content = input('Enter your note in Markdown format:\n')
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html_content = convert_markdown_to_html(note_content)
    new_note = {'content': note_content, 'html_content': html_content, 'created_at': created_at}
    notes.append(new_note)
    save_notes(notes)
    print('Note created successfully.')

def edit_note(index):
    notes = get_notes()
    if 0 <= index < len(notes):
        note_content = input('Edit your note in Markdown format:\n')
        created_at = notes[index]['created_at']
        html_content = convert_markdown_to_html(note_content)
        updated_note = {'content': note_content, 'html_content': html_content, 'created_at': created_at}
        notes[index] = updated_note
        save_notes(notes)
        print('Note updated successfully.')
    else:
        print('Invalid note index.')

def delete_note(index):
    notes = get_notes()
    if 0 <= index < len(notes):
        del notes[index]
        save_notes(notes)
        print('Note deleted successfully.')
    else:
        print('Invalid note index.')

def display_notes():
    notes = get_notes()
    for index, note in enumerate(notes):
        print(f"\nNote {index + 1} (Created at: {note['created_at']}):\n{note['html_content']}")

if __name__ == '__main__':
    while True:
        print("\nOptions:")
        print("1. Create a note")
        print("2. Edit a note")
        print("3. Delete a note")
        print("4. Display notes")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_note()
        elif choice == '2':
            index = int(input("Enter the index of the note to edit: ")) - 1
            edit_note(index)
        elif choice == '3':
            index = int(input("Enter the index of the note to delete: ")) - 1
            delete_note(index)
        elif choice == '4':
            display_notes()
        elif choice == '5':
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')
