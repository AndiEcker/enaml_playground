""" example for enaml issue: attr is no longer accessible after looper.iterable update. """
import enaml
from enaml.qt.qt_application import QtApplication
import atom.api


class FrameworkApp(QtApplication):
    """ used for to add additional atom members. """
    looper_container_list = atom.api.ContainerList(default=['a', 'b', 'c'])


if __name__ == '__main__':
    with enaml.imports():
        # noinspection PyUnresolvedReferences
        from enaml_attr_gone_view import Main

    app = FrameworkApp()

    view = Main(test_attr=app, app=app)
    view.show()

    app.start()
