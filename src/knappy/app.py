from textual.app import App, ComposeResult
from textual.widgets import DataTable
from knappy.core.models import validate_items
from knappy.util.listtable import gen_datatable

DATA_ROWS = gen_datatable()


class Knapp(App):
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*DATA_ROWS[0])
        table.add_rows(DATA_ROWS[1:])


app = Knapp()


def main() -> None:
    app.run()
