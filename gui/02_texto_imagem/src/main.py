import flet as ft


def main(page: ft.Page):

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Olá, Mundo flet Python!!!"),
            ),
            expand=True,  
        )
    )
ft.app(main)
