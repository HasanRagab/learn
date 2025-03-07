class OldPrinter:
    def print_text(self, text):
        print(f"Old Printer: {text}")

class NewPrinter:
    def print_document(self, text):
        print(f"New Printer: {text}")

class PrinterAdapter:
    def __init__(self, old_printer: OldPrinter):
        self.old_printer = old_printer

    def print_document(self, text):
        self.old_printer.print_text(text)

old_printer = OldPrinter()
adapter = PrinterAdapter(old_printer)

adapter.print_document("Hello Adapter!")
