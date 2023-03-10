from Cocoa import NSObject, NSApplication, NSApp, NSWindow, NSButton, NSSound, NSPanel #пофиг на ошибки
from PyObjCTools import AppHelper
from AppKit import NSWorkspace
import Foundation
from pycocoa import NSWindowStyleMaskResizable, NSColor
from Foundation import NSBundle


class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, aNotification):
        print("Hello, World!")

    def sayHello_(self, sender):
        print("Hello again, World!")


def main():
    app = NSApplication.sharedApplication()

    # we must keep a reference to the delegate object ourselves,
    # NSApp.setDelegate_() doesn't retain it. A local variable is
    # enough here.
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)

    win = NSPanel.alloc()
    frame = ((200.0, 300.0), (250.0, 100.0))
    win.initWithContentRect_styleMask_backing_defer_(frame, 129, 2, True)
    #print(win._.collectionBehavior)
    win._.level = 24
    win._.collectionBehavior = 257
    win._.styleMask = 129
    print(win._.styleMask)
    print(win._.collectionBehavior)
    #TODO ._. это получение доступа к полям
    #win._.styleMask = 0
    #win._.alphaValue = 0.5
    #print(win._.styleMask)
    print(win._.styleMask)
    win.setTitle_("HelloWorld")
    #win.setLevel_(3)  # floating window
    workspace = NSWorkspace.sharedWorkspace()
    app_name = "Discord"
    print(workspace.fullPathForApplication_(app_name))
    #workspace.launchApplication_(app_name)

    bundle = NSBundle.mainBundle()
    path = bundle.pathForResource_ofType_("3b0cecbf4ec6a5e013d6fa5e2a249e23","jpg")
    print(path)

    hello = NSButton.alloc().initWithFrame_(((10.0, 10.0), (80.0, 80.0)))
    win.contentView().addSubview_(hello)
    hello.setBezelStyle_(4)
    hello.setTitle_("Hello!")
    hello.setTarget_(app.delegate())
    hello.setAction_("sayHello:")

    beep = NSSound.alloc()
    beep.initWithContentsOfFile_byReference_("/System/Library/Sounds/Tink.Aiff", 1)
    hello.setSound_(beep)

    bye = NSButton.alloc().initWithFrame_(((100.0, 10.0), (80.0, 80.0)))
    win.contentView().addSubview_(bye)
    bye.setBezelStyle_(4)
    bye.setTarget_(app)
    bye.setAction_("stop:")
    bye.setEnabled_(1)
    bye.setTitle_("Goodbye!")

    adios = NSSound.alloc()
    adios.initWithContentsOfFile_byReference_("/System/Library/Sounds/Basso.aiff", 1)
    bye.setSound_(adios)

    win.display()
    win.orderFrontRegardless()  # but this one does

    AppHelper.runEventLoop()


if __name__ == "__main__":
    main()