import flet as ft


def main(page: ft.Page):
    page.title = "Flet Mini Dictionary App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    # 1. The Data Source (Local Dictionary)
    # In a real app, this might come from a database or JSON file
    dictionary_data = {
        "Lexicon":  "The vocabulary of a person, language, or branch of knowledge. For example: "
                    "A chef's professional lexicon includes terms like 'julienne' and 'mirepoix'."""
                    ,
        "Ephemeral":  "Lasting for a very short time; transient. "
            "Example: The beauty of a sunset is ephemeral, existing only for a few moments.",

        "Quixotic":  "Exceedingly idealistic; unrealistic and impractical. "
            "Example: He had a quixotic desire to reform the entire school system overnight.",

        "Serendipity":  "The occurrence and development of events by chance in a happy or beneficial way. "
            "Example: It was pure serendipity that she found the exact book she needed in a dusty old shop.",

        "Ubiquitous":  "Present, appearing, or found everywhere. "
            "Example:In the modern age, smartphones have become truly ubiquitous.",

        "Python": "A high-level, general-purpose programming language. "
                  "Its design philosophy emphasizes code readability with the use of significant indentation.",

        "Flet": "A framework that allows you to build interactive multi-user web, desktop, "
                "and mobile apps in your favorite language without prior experience in frontend development.",
        "Variable": "A symbolic name associated with a value and whose associated value may be changed.",
        "Function": "A block of code which only runs when it is called. "
                    "You can pass data, known as parameters, into a function.",
        "Algorithm": "A set of instructions designed to perform a specific task. "
                     "This can be a simple process, such as multiplying two numbers, or a complex operation, such as playing a compressed video file.",

        "Backend": "The server-side of an application and everything that communicates between the database and the browser.",

        "Frontend": "The part of the web that you can see and interact with. "
                    "It includes the structure, design, behavior, and content of everything seen on the browser screen.",
        "API": "Application Programming Interface. "
               "A set of rules that allows different software applications to communicate with each other.",
        "Database": "An organized collection of structured information, or data, typically stored electronically in a computer system.",

        "Loop": "A programming structure that repeats a sequence of instructions until a specific condition is met."
    }

    # 2. Right Side: The Display Area Controls
    # We initialize these empty or with a welcome message
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
        value="Click on a button on the left to see its definition here.",
        size=18,
        selectable=True,  # Allows user to copy text
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

    # 4. Left Side: Generating the Buttons
    button_list = ft.ListView(
        expand=True,
        spacing=10,
        padding=10,
        auto_scroll=False
    )

    for word in dictionary_data:
        button_list.controls.append(
            ft.OutlinedButton(
                text=word,
                on_click=display_word,  # Link to the function above
                height=50,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=8),
                )
            )
        )

    # 5. The Layout Construction
    # We use a Row to put the list (left) and display (right) side-by-side
    layout = ft.Row(
        controls=[
            # Left Container (The List)
            ft.Container(
                content=button_list,
                width=250,  # Fixed width for the sidebar
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
                    scroll=ft.ScrollMode.AUTO,  # Make description scrollable if long
                    alignment=ft.MainAxisAlignment.START,
                ),
                expand=True,  # Take up the rest of the screen
                padding=ft.padding.only(left=20, top=10),
            )
        ],
        expand=True  # The Row should fill the page vertically
    )

    page.add(layout)


ft.app(target=main)