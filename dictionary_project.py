import flet as ft


def main(page: ft.Page):
    page.title = "Flet Mini Dictionary App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    # 1. The Data Source (Local Dictionary)
    dictionary_data = {
        "Lexicon": "The vocabulary of a person, language, or branch of knowledge. For example: A chef's professional lexicon includes terms like 'julienne' and 'mirepoix'.",
        "Ephemeral": "Lasting for a very short time; transient. Example: The beauty of a sunset is ephemeral, existing only for a few moments.",
        "Quixotic": "Exceedingly idealistic; unrealistic and impractical. Example: He had a quixotic desire to reform the entire school system overnight.",
        "Serendipity": "The occurrence and development of events by chance in a happy or beneficial way. Example: It was pure serendipity that she found the exact book she needed in a dusty old shop.",
        "Ubiquitous": "Present, appearing, or found everywhere. Example: In the modern age, smartphones have become truly ubiquitous.",
        "Python": "A high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.",
        "Flet": "A framework that allows you to build interactive multi-user web, desktop, and mobile apps in your favorite language without prior experience in frontend development.",
        "Variable": "A symbolic name associated with a value and whose associated value may be changed.",
        "Function": "A block of code which only runs when it is called. You can pass data, known as parameters, into a function.",
        "Algorithm": "A set of instructions designed to perform a specific task. This can be a simple process, such as multiplying two numbers, or a complex operation, such as playing a compressed video file.",
        "Backend": "The server-side of an application and everything that communicates between the database and the browser.",
        "Frontend": "The part of the web that you can see and interact with. It includes the structure, design, behavior, and content of everything seen on the browser screen.",
        "API": "Application Programming Interface. A set of rules that allows different software applications to communicate with each other.",
        "Database": "An organized collection of structured information, or data, typically stored electronically in a computer system.",
        "Loop": "A programming structure that repeats a sequence of instructions until a specific condition is met."
    }

    # 2. Right Side: The Display Area Controls
    head_title = ft.Text(
        value="Welcome to Goremi's mini dictionary",
        size=40,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.INDIGO_700,
    )
    word_title = ft.Text(
        value="Select a word",
        size=40,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.INDIGO_700,
    )

    word_definition = ft.Text(
        value="Click on a button on the left or use the search bar to find its definition.",
        size=18,
        selectable=True,
        color=ft.Colors.BLUE_GREY_700
    )

    # 3. Event Handler: What happens when a button is clicked
    def display_word(e):
        selected_word = e.control.text
        # Update the right side controls
        word_title.value = selected_word
        word_definition.value = dictionary_data[selected_word]

        # Trigger a UI update
        page.update()

    # 4. Left Side: The List View (placeholder for buttons)
    button_list = ft.ListView(
        expand=True,
        spacing=10,
        padding=10,
        auto_scroll=False
    )

    # 5. Core Search Logic: Function to filter and update the list
    def update_word_list(search_term: str):
        # 1. Clear the existing controls
        button_list.controls.clear()

        # 2. Convert search term to lower case for case-insensitive search
        search_term = search_term.lower()

        # 3. Filter the dictionary keys
        filtered_words = [
            word for word in dictionary_data.keys()
            if search_term in word.lower()
        ]

        # 4. Re-generate buttons for filtered words
        for word in filtered_words:
            button_list.controls.append(
                ft.OutlinedButton(
                    text=word,
                    on_click=display_word,
                    height=50,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                    )
                )
            )

        # 5. Update the UI to show the new list
        page.update()

    # 6. Search Bar Control
    search_bar = ft.TextField(
        label="Search for a word...",
        hint_text="Type a word to filter the list",
        on_change=lambda e: update_word_list(e.control.value),  # Calls the function on every key press
        height=50
    )

    # INITIAL LOAD: Populate the list with ALL words when the app starts
    update_word_list("")

    # 7. The Layout Construction
    layout = ft.Row(
        controls=[
            # Left Container (Search + List)
            ft.Container(
                content=ft.Column(
                    controls=[
                        search_bar,  # <<< ADDED SEARCH BAR HERE
                        ft.Divider(height=10, thickness=0),
                        button_list,
                    ],
                    expand=True,
                ),
                width=250,
                border=ft.border.only(right=ft.BorderSide(1, ft.Colors.GREY_300)),
                padding=ft.padding.only(right=20)
            ),

            # Right Container (The Display)
            ft.Container(
                content=ft.Column(
                    controls=[
                        head_title,
                        ft.Divider(thickness=20),
                        word_title,
                        ft.Divider(),
                        word_definition
                    ],
                    scroll=ft.ScrollMode.AUTO,
                    alignment=ft.MainAxisAlignment.START,
                ),
                expand=True,
                padding=ft.padding.only(left=20, top=10),
            )
        ],
        expand=True
    )

    page.add(layout)


# Run the app
ft.app(target=main)