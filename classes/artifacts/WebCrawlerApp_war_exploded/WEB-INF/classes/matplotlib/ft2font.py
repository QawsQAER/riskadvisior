# encoding: utf-8
# module matplotlib.ft2font
# from /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/matplotlib/ft2font.so
# by generator 1.136
""" The ft2font module """
# no imports

# Variables with simple values

BOLD = 2

EXTERNAL_STREAM = 1024

FAST_GLYPHS = 128

FIXED_SIZES = 2
FIXED_WIDTH = 4

GLYPH_NAMES = 512

HORIZONTAL = 16

ITALIC = 1

KERNING = 64

KERNING_DEFAULT = 0
KERNING_UNFITTED = 1
KERNING_UNSCALED = 2

LOAD_CROP_BITMAP = 64L

LOAD_DEFAULT = 0L

LOAD_FORCE_AUTOHINT = 32L

LOAD_IGNORE_GLOBAL_ADVANCE_WIDTH = 512L

LOAD_IGNORE_TRANSFORM = 2048L

LOAD_LINEAR_DESIGN = 8192L

LOAD_MONOCHROME = 4096L

LOAD_NO_AUTOHINT = 32768L
LOAD_NO_BITMAP = 8L
LOAD_NO_HINTING = 2L
LOAD_NO_RECURSE = 1024L
LOAD_NO_SCALE = 1L

LOAD_PEDANTIC = 128L
LOAD_RENDER = 4L

LOAD_TARGET_LCD = 196608L

LOAD_TARGET_LCD_V = 262144L

LOAD_TARGET_LIGHT = 65536L
LOAD_TARGET_MONO = 131072L
LOAD_TARGET_NORMAL = 0L

LOAD_VERTICAL_LAYOUT = 16L

MULTIPLE_MASTERS = 256

SCALABLE = 1

SFNT = 8

VERTICAL = 1

__freetype_version__ = '2.4.12'

# no functions
# classes

class FT2Font(object):
    """ FT2Font """
    def attach_file(self, filename): # real signature unknown; restored from __doc__
        """
        attach_file(filename)
        
        Attach a file with extra information on the font
        (in practice, an AFM file with the metrics of a Type 1 font).
        Throws an exception if unsuccessful.
        """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """
        clear()
        
        Clear all the glyphs, reset for a new set_text
        """
        pass

    def draw_glyphs_to_bitmap(self): # real signature unknown; restored from __doc__
        """
        draw_glyphs_to_bitmap()
        
        Draw the glyphs that were loaded by set_text to the bitmap
        The bitmap size will be automatically set to include the glyphs
        """
        pass

    def draw_glyph_to_bitmap(self, bitmap, x, y, glyph): # real signature unknown; restored from __doc__
        """
        draw_glyph_to_bitmap(bitmap, x, y, glyph)
        
        Draw a single glyph to the bitmap at pixel locations x,y
        Note it is your responsibility to set up the bitmap manually
        with set_bitmap_size(w,h) before this call is made.
        
        If you want automatic layout, use set_text in combinations with
        draw_glyphs_to_bitmap.  This function is intended for people who
        want to render individual glyphs at precise locations, eg, a
        a glyph returned by load_char
        """
        pass

    def get_charmap(self): # real signature unknown; restored from __doc__
        """
        get_charmap()
        
        Returns a dictionary that maps the character codes of the selected charmap
        (Unicode by default) to their corresponding glyph indices.
        """
        pass

    def get_descent(self): # real signature unknown; restored from __doc__
        """
        d = get_descent()
        
        Get the descent of the current string set by set_text in 26.6 subpixels.
        The rotation of the string is accounted for.  To get the descent
        in pixels, divide this value by 64.
        """
        pass

    def get_glyph_name(self, index): # real signature unknown; restored from __doc__
        """
        get_glyph_name(index)
        
        Retrieves the ASCII name of a given glyph in a face.
        """
        pass

    def get_image(self): # real signature unknown; restored from __doc__
        """
        get_image()
        
        Returns the underlying image buffer for this font object.
        """
        pass

    def get_kerning(self, left, right, mode): # real signature unknown; restored from __doc__
        """
        dx = get_kerning(left, right, mode)
        
        Get the kerning between left char and right glyph indices
        mode is a kerning mode constant
          KERNING_DEFAULT  - Return scaled and grid-fitted kerning distances
          KERNING_UNFITTED - Return scaled but un-grid-fitted kerning distances
          KERNING_UNSCALED - Return the kerning vector in original font units
        """
        pass

    def get_name_index(self, name): # real signature unknown; restored from __doc__
        """
        get_name_index(name)
        
        Returns the glyph index of a given glyph name.
        The glyph index 0 means `undefined character code'.
        """
        pass

    def get_num_glyphs(self): # real signature unknown; restored from __doc__
        """
        get_num_glyphs()
        
        Return the number of loaded glyphs
        """
        pass

    def get_path(self): # real signature unknown; restored from __doc__
        """
        get_path()
        
        Get the path data from the currently loaded glyph as a tuple of vertices, codes.
        """
        pass

    def get_ps_font_info(self): # real signature unknown; restored from __doc__
        """
        get_ps_font_info()
        
        Return the information in the PS Font Info structure.
        """
        pass

    def get_sfnt(self, name): # real signature unknown; restored from __doc__
        """
        get_sfnt(name)
        
        Get all values from the SFNT names table.  Result is a dictionary whosekey is the platform-ID, ISO-encoding-scheme, language-code, anddescription.
        """
        pass

    def get_sfnt_table(self, name): # real signature unknown; restored from __doc__
        """
        get_sfnt_table(name)
        
        Return one of the following SFNT tables: head, maxp, OS/2, hhea, vhea, post, or pclt.
        """
        pass

    def get_width_height(self): # real signature unknown; restored from __doc__
        """
        w, h = get_width_height()
        
        Get the width and height in 26.6 subpixels of the current string set by set_text
        The rotation of the string is accounted for.  To get width and height
        in pixels, divide these values by 64
        """
        pass

    def get_xys(self): # real signature unknown; restored from __doc__
        """
        get_xys()
        
        Get the xy locations of the current glyphs
        """
        pass

    def load_char(self, charcode, flags=None): # real signature unknown; restored from __doc__
        """
        load_char(charcode, flags=LOAD_FORCE_AUTOHINT)
        
        Load character with charcode in current fontfile and set glyph.
        The flags argument can be a bitwise-or of the LOAD_XXX constants.
        Return value is a Glyph object, with attributes
          width          # glyph width
          height         # glyph height
          bbox           # the glyph bbox (xmin, ymin, xmax, ymax)
          horiBearingX   # left side bearing in horizontal layouts
          horiBearingY   # top side bearing in horizontal layouts
          horiAdvance    # advance width for horizontal layout
          vertBearingX   # left side bearing in vertical layouts
          vertBearingY   # top side bearing in vertical layouts
          vertAdvance    # advance height for vertical layout
        """
        pass

    def load_glyph(self, glyphindex, flags=None): # real signature unknown; restored from __doc__
        """
        load_glyph(glyphindex, flags=LOAD_FORCE_AUTOHINT)
        
        Load character with glyphindex in current fontfile and set glyph.
        The flags argument can be a bitwise-or of the LOAD_XXX constants.
        Return value is a Glyph object, with attributes
          width          # glyph width
          height         # glyph height
          bbox           # the glyph bbox (xmin, ymin, xmax, ymax)
          horiBearingX   # left side bearing in horizontal layouts
          horiBearingY   # top side bearing in horizontal layouts
          horiAdvance    # advance width for horizontal layout
          vertBearingX   # left side bearing in vertical layouts
          vertBearingY   # top side bearing in vertical layouts
          vertAdvance    # advance height for vertical layout
        """
        pass

    def select_charmap(self, i): # real signature unknown; restored from __doc__
        """
        select_charmap(i)
        
        select charmap i where i is one of the FT_Encoding number
        """
        pass

    def set_charmap(self, i): # real signature unknown; restored from __doc__
        """
        set_charmap(i)
        
        Make the i-th charmap current
        """
        pass

    def set_size(self, ptsize, dpi): # real signature unknown; restored from __doc__
        """
        set_size(ptsize, dpi)
        
        Set the point size and dpi of the text.
        """
        pass

    def set_text(self, s, angle): # real signature unknown; restored from __doc__
        """
        set_text(s, angle)
        
        Set the text string and angle.
        You must call this before draw_glyphs_to_bitmap
        A sequence of x,y positions is returned
        """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


class FT2Image(object):
    """ FT2Image """
    def as_array(self): # real signature unknown; restored from __doc__
        """
        x = image.as_array()
        
        Return the image buffer as a width x height numpy array of ubyte
        """
        pass

    def as_rgba_str(self): # real signature unknown; restored from __doc__
        """
        s = image.as_rgba_str()
        
        Return the image buffer as a RGBA string
        """
        pass

    def as_rgb_str(self): # real signature unknown; restored from __doc__
        """
        s = image.as_rgb_str()
        
        Return the image buffer as a RGB string
        """
        pass

    def as_str(self): # real signature unknown; restored from __doc__
        """
        s = image.as_str()
        
        Return the image buffer as a string
        """
        pass

    def draw_rect(self, x0, y0, x1, y1): # real signature unknown; restored from __doc__
        """
        draw_rect(x0, y0, x1, y1)
        
        Draw a rect to the image.
        """
        pass

    def draw_rect_filled(self, x0, y0, x1, y1): # real signature unknown; restored from __doc__
        """
        draw_rect_filled(x0, y0, x1, y1)
        
        Draw a filled rect to the image.
        """
        pass

    def get_height(self, *args, **kwargs): # real signature unknown
        """ Returns the height of the image """
        pass

    def get_width(self, *args, **kwargs): # real signature unknown
        """ Returns the width of the image """
        pass

    def write_bitmap(self, fname): # real signature unknown; restored from __doc__
        """
        write_bitmap(fname)
        
        Write the bitmap to file fname
        """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


