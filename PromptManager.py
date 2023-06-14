import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QListWidget, QMessageBox, QLabel, QDialog, QLineEdit, QDialogButtonBox
from PyQt5.QtGui import QClipboard

class PromptDialog(QDialog):
    def __init__(self, name="", prompt="", negative_prompt="", parent=None):
        super(PromptDialog, self).__init__(parent)
        self.setWindowTitle("Editar Prompt")

        self.name_edit = QLineEdit()
        self.prompt_edit = QTextEdit()
        self.negative_prompt_edit = QTextEdit()

        self.name_edit.setText(name)
        self.prompt_edit.setPlainText(prompt)
        self.negative_prompt_edit.setPlainText(negative_prompt)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Nombre:"))
        layout.addWidget(self.name_edit)
        layout.addWidget(QLabel("Prompt:"))
        layout.addWidget(self.prompt_edit)
        layout.addWidget(QLabel("Negative Prompt:"))
        layout.addWidget(self.negative_prompt_edit)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def get_values(self):
        name = self.name_edit.text()
        prompt = self.prompt_edit.toPlainText()
        negative_prompt = self.negative_prompt_edit.toPlainText()
        return name, prompt, negative_prompt


class PromptListForm(QWidget):
    def __init__(self, data, parent=None):
        super(PromptListForm, self).__init__(parent)
        self.data = data

        self.prompt_list = QListWidget()
        self.prompt_list.itemClicked.connect(self.show_prompt)

        self.prompt_text_edit = QTextEdit()
        self.prompt_text_edit.setReadOnly(True)

        self.negative_prompt_text_edit = QTextEdit()
        self.negative_prompt_text_edit.setReadOnly(True)

        self.copy_prompt_button = QPushButton("Copiar Prompt")
        self.copy_negative_prompt_button = QPushButton("Copiar Negative Prompt")

        self.copy_prompt_button.clicked.connect(self.copy_prompt)
        self.copy_negative_prompt_button.clicked.connect(self.copy_negative_prompt)

        self.edit_button = QPushButton("Editar")
        self.delete_button = QPushButton("Eliminar")
        self.add_button = QPushButton("Agregar")

        self.edit_button.clicked.connect(self.edit_prompt)
        self.delete_button.clicked.connect(self.delete_prompt)
        self.add_button.clicked.connect(self.add_prompt)

        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        left_layout.addWidget(QLabel("Nombres disponibles:"))
        left_layout.addWidget(self.prompt_list)
        left_layout.addWidget(self.edit_button)
        left_layout.addWidget(self.delete_button)
        left_layout.addWidget(self.add_button)

        right_layout.addWidget(QLabel("Prompt:"))
        right_layout.addWidget(self.prompt_text_edit)
        right_layout.addWidget(QLabel("Negative Prompt:"))
        right_layout.addWidget(self.negative_prompt_text_edit)
        right_layout.addWidget(self.copy_prompt_button)
        right_layout.addWidget(self.copy_negative_prompt_button)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)

        self.populate_list()

    def populate_list(self):
        self.prompt_list.clear()
        for index, row in self.data.iterrows():
            self.prompt_list.addItem(row["name"])

    def show_prompt(self, item):
        name = item.text()
        prompt = self.data.loc[self.data["name"] == name, "prompt"].values[0]
        negative_prompt = self.data.loc[self.data["name"] == name, "negative_prompt"].values[0]

        self.prompt_text_edit.setPlainText(str(prompt))
        self.negative_prompt_text_edit.setPlainText(str(negative_prompt))

    def copy_prompt(self):
        prompt = self.prompt_text_edit.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(str(prompt))

    def copy_negative_prompt(self):
        negative_prompt = self.negative_prompt_text_edit.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(str(negative_prompt))

    def edit_prompt(self):
        current_item = self.prompt_list.currentItem()
        if current_item is not None:
            name = current_item.text()
            prompt = self.data.loc[self.data["name"] == name, "prompt"].values[0]
            negative_prompt = self.data.loc[self.data["name"] == name, "negative_prompt"].values[0]

            dialog = PromptDialog(name, str(prompt), str(negative_prompt))
            if dialog.exec_() == QDialog.Accepted:
                new_name, new_prompt, new_negative_prompt = dialog.get_values()
                self.data.loc[self.data["name"] == name, "name"] = new_name
                self.data.loc[self.data["name"] == name, "prompt"] = new_prompt
                self.data.loc[self.data["name"] == name, "negative_prompt"] = new_negative_prompt
                self.populate_list()
                self.save_data()

    def delete_prompt(self):
        current_item = self.prompt_list.currentItem()
        if current_item is not None:
            name = current_item.text()
            self.data = self.data[self.data["name"] != name]
            self.populate_list()
            self.save_data()

    def add_prompt(self):
        dialog = PromptDialog()
        if dialog.exec_() == QDialog.Accepted:
            name, prompt, negative_prompt = dialog.get_values()
            self.data = pd.concat([self.data, pd.DataFrame({"name": [name], "prompt": [prompt], "negative_prompt": [negative_prompt]})], ignore_index=True)
            self.populate_list()
            self.save_data()

    def save_data(self):
        self.data.to_csv("datos.csv", index=False)


if __name__ == "__main__":
    app = QApplication([])
    data = pd.read_csv("datos.csv")
    form = PromptListForm(data)
    form.show()
    app.exec_()

