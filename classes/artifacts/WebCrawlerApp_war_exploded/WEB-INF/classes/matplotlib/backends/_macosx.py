# encoding: utf-8
# module matplotlib.backends._macosx
# from /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/matplotlib/backends/_macosx.so
# by generator 1.136
""" Mac OS X native backend """
# no imports

# functions

def choose_save_file(*args, **kwargs): # real signature unknown
    """ Closes the window. """
    pass

def set_cursor(*args, **kwargs): # real signature unknown
    """ Sets the active cursor. """
    pass

def show(*args, **kwargs): # real signature unknown
    """
    Show all the figures and enter the main loop.
    This function does not return until all Matplotlib windows are closed,
    and is normally not needed in interactive sessions.
    """
    pass

# classes

class FigureCanvas(object):
    """ A FigureCanvas object wraps a Cocoa NSView object. """
    def draw(self, *args, **kwargs): # real signature unknown
        """ Draws the canvas. """
        pass

    def invalidate(self, *args, **kwargs): # real signature unknown
        """ Invalidates the canvas. """
        pass

    def remove_rubberband(self, *args, **kwargs): # real signature unknown
        """ Removes the current rubberband rectangle. """
        pass

    def set_rubberband(self, *args, **kwargs): # real signature unknown
        """ Specifies a new rubberband rectangle and invalidates it. """
        pass

    def start_event_loop(self, *args, **kwargs): # real signature unknown
        """ Runs the event loop until the timeout or until stop_event_loop is called. """
        pass

    def stop_event_loop(self, *args, **kwargs): # real signature unknown
        """ Stops the event loop that was started by start_event_loop. """
        pass

    def write_bitmap(self, *args, **kwargs): # real signature unknown
        """
        Saves the figure to the specified file as a bitmap
        (bmp, gif, jpeg, or png).
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass


class FigureManager(object):
    """ A FigureManager object wraps a Cocoa NSWindow object. """
    def destroy(self, *args, **kwargs): # real signature unknown
        """ Closes the window associated with the figure manager. """
        pass

    def get_window_title(self, *args, **kwargs): # real signature unknown
        """ Returns the title of the window associated with the figure manager. """
        pass

    def set_window_title(self, *args, **kwargs): # real signature unknown
        """ Sets the title of the window associated with the figure manager. """
        pass

    def show(self, *args, **kwargs): # real signature unknown
        """ Shows the window associated with the figure manager. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass


class GraphicsContext(object):
    """
    A GraphicsContext object wraps a Quartz 2D graphics context
    (CGContextRef). Most methods either draw into the graphics context
    (moveto, lineto, etc.) or set the drawing properties (set_linewidth,
    set_joinstyle, etc.).
    """
    def draw_gouraud_triangle(self, *args, **kwargs): # real signature unknown
        """ Draws a Gouraud-shaded triangle in the graphics context. """
        pass

    def draw_image(self, *args, **kwargs): # real signature unknown
        """ Draw an image at (x,y) in the graphics context. """
        pass

    def draw_markers(self, *args, **kwargs): # real signature unknown
        """ Draws a marker in the graphics context at each of the vertices in path. """
        pass

    def draw_mathtext(self, *args, **kwargs): # real signature unknown
        """ Draw a TeX string at (x,y) as a bitmap in the graphics context. """
        pass

    def draw_path(self, *args, **kwargs): # real signature unknown
        """ Draw a path in the graphics context and strokes and (if rgbFace is not None) fills it. """
        pass

    def draw_path_collection(self, *args, **kwargs): # real signature unknown
        """ Draw a collection of paths in the graphics context. """
        pass

    def draw_quad_mesh(self, *args, **kwargs): # real signature unknown
        """ Draws a mesh in the graphics context. """
        pass

    def draw_text(self, *args, **kwargs): # real signature unknown
        """ Draw a string at (x,y) with the given properties in the graphics context. """
        pass

    def get_text_width_height_descent(self, *args, **kwargs): # real signature unknown
        """ Returns the width, height, and descent of the text. """
        pass

    def restore(self, *args, **kwargs): # real signature unknown
        """ Restores the current graphics context from the stack. """
        pass

    def save(self, *args, **kwargs): # real signature unknown
        """ Saves the current graphics context onto the stack. """
        pass

    def set_alpha(self, *args, **kwargs): # real signature unknown
        """ Sets the opacitiy level for objects drawn in a graphics context """
        pass

    def set_antialiased(self, *args, **kwargs): # real signature unknown
        """ Sets anti-aliasing on or off for a graphics context. """
        pass

    def set_capstyle(self, *args, **kwargs): # real signature unknown
        """ Sets the style for the endpoints of lines in a graphics context. """
        pass

    def set_clip_path(self, *args, **kwargs): # real signature unknown
        """ Sets the clipping path. """
        pass

    def set_clip_rectangle(self, *args, **kwargs): # real signature unknown
        """ Sets the clipping path to the area defined by the specified rectangle. """
        pass

    def set_dashes(self, *args, **kwargs): # real signature unknown
        """ Sets the pattern for dashed lines in a graphics context. """
        pass

    def set_dpi(self, *args, **kwargs): # real signature unknown
        """ Sets the dpi for a graphics context. """
        pass

    def set_foreground(self, *args, **kwargs): # real signature unknown
        """ Sets the current stroke and fill color to a value in the DeviceRGB color space. """
        pass

    def set_graylevel(self, *args, **kwargs): # real signature unknown
        """ Sets the current stroke and fill color to a value in the DeviceGray color space. """
        pass

    def set_joinstyle(self, *args, **kwargs): # real signature unknown
        """ Sets the style for the joins of connected lines in a graphics context. """
        pass

    def set_linewidth(self, *args, **kwargs): # real signature unknown
        """ Sets the line width for a graphics context. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass


class NavigationToolbar(object):
    """ NavigationToolbar """
    def get_active(self, *args, **kwargs): # real signature unknown
        """ Returns a list of integers identifying which items in the menu are selected. """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """ Updates the toolbar menu. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass


class NavigationToolbar2(object):
    """ NavigationToolbar2 """
    def set_message(self, *args, **kwargs): # real signature unknown
        """ Set the message to be displayed on the toolbar. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass


class Timer(object):
    """ A Timer object wraps a CFRunLoopTimerRef and can add it to the event loop. """
    def _timer_start(self, *args, **kwargs): # real signature unknown
        """ Initialize and start the timer. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass


