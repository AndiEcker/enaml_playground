""" taken from https://atom.readthedocs.io/en/latest/examples/ex_containers.html """

# from __future__ import (division, unicode_literals, print_function, absolute_import)

from atom.api import Atom, List, ContainerList, Tuple, Dict


class Data(Atom):
    """ atom """
    dlist = List(default=[1, 2, 3])

    dcont_list = ContainerList(default=[6, 9, 12])

    dtuple = Tuple(default=(5, 4, 3))

    ddict = Dict(default=dict(foo=1, bar='a'))

    dcont_dict = ContainerList(default=[dict(a=1, b=2), dict(c=3, d=4)])

    def _observe_dlist(self, change):
        print(f"list change: {change} // {self}")

    def _observe_dcont_list(self, change):
        print(f"container list change: {change} // {self}")

    def _observe_dtuple(self, change):
        print(f"tuple change: {change} // {self}")

    def _observe_ddict(self, change):
        print(f"dict change: {change} // {self}")

    def _observe_dcont_dict(self, change):
        print(f"container dict change: {change} // {self}")


if __name__ == '__main__':
    data = Data()

    print("dlist -----------------------------------")
    print(data.dlist)
    data.dlist.append('test')       # NO NOTIFICATION
    print(data.dlist)

    print("dcont_list -----------------------------------")
    print(data.dcont_list)
    data.dcont_list.append(1)
    data.dcont_list.pop(0)
    data.dcont_list[-1] = 111
    print(data.dcont_list)

    print("dtuple -----------------------------------")
    print(data.dtuple)
    data.dtuple = (18, 17, 16) + data.dtuple
    # add method only exists for sets: data.dtuple.add(999)
    print(data.dtuple)

    print("ddict -----------------------------------")
    print(data.ddict)
    data.ddict['ham'] = 'spam'          # NO NOTIFICATION
    print(data.ddict)
    ddict_copy = data.ddict.copy()
    assert data.ddict is not ddict_copy
    data.ddict = ddict_copy             # NO NOTIFICATION
    # assert data.ddict is ddict_copy     # FAILING
    print(data.ddict)
    data.ddict = dict(data.ddict)       # NO NOTIFICATION
    print(data.ddict)
    data.ddict.update(dict(x=1, y=22))  # NO NOTIFICATION
    print(data.ddict)
    data.ddict.pop('foo')               # NO NOTIFICATION
    print(data.ddict)

    print("dcont_dict -----------------------------------")
    print(data.dcont_dict)
    data.dcont_dict[0]['z'] = 'tst'     # NO NOTIFICATION
    print(data.dcont_dict)
    dict_copy = data.dcont_dict.copy()
    dict_copy[0]['new'] = 'new_item'
    data.dcont_dict = dict_copy         # NO NOTIFICATION
    print(data.dcont_dict)
    data.dcont_dict.append(dict(r=9))
    print(data.dcont_dict)
    data.dcont_dict.pop(-1)
    print(data.dcont_dict)

    data = None
    print(data)
