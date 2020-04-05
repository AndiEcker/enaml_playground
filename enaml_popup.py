""" example for enaml popup view. """
import enaml
from enaml.qt.qt_application import QtApplication

if __name__ == '__main__':
    with enaml.imports():
        # noinspection PyUnresolvedReferences
        from enaml_popup_view import Main

    app = QtApplication()

    view = Main()
    view.show()

    app.start()
