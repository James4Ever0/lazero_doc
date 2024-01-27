from gi.repository import Gtk, Vte, GLib, Pango, Gio
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Vte', '2.91')
# if you really want to, use java instead to do terminal emulation.
# no fucking horrible shits, please?
# either replace it or use it.
class TheWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="GTK3 IDE")
        self.set_default_size(600, 300)

        terminal = Vte.Terminal()
        #pty = terminal.pty_new_sync(Vte.PtyFlags.DEFAULT)
        pty = Vte.Pty.new_sync(Vte.PtyFlags.DEFAULT)
        terminal.set_pty(pty)

        pty.spawn_async(
            None,
            ["/bin/python"],
            None,
            GLib.SpawnFlags.DO_NOT_REAP_CHILD,
            None,
            None,
            -1,
            None,
            self.ready
        )

        # self.terminal.get_pty(self.pty)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        scroller = Gtk.ScrolledWindow()
        scroller.set_hexpand(True)
        scroller.set_vexpand(True)
        scroller.add(terminal)
        box.pack_start(scroller, False, True, 2)
        self.add(box)

    def ready(self, pty, task):
        print('pty ', pty)


win = TheWindow()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()
#  what the heck?
# check the implementation of vscode terminal. -> the joke out there.