# encoding: utf-8
# module _CG
# from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/_CG.so
# by generator 1.136
# no doc

# imports
from MacOS import Error


# no functions
# classes

class CGContextRefType(object):
    # no doc
    def CGContextAddArc(self, *args, **kwargs): # real signature unknown
        """ (float x, float y, float radius, float startAngle, float endAngle, int clockwise) -> None """
        pass

    def CGContextAddArcToPoint(self, *args, **kwargs): # real signature unknown
        """ (float x1, float y1, float x2, float y2, float radius) -> None """
        pass

    def CGContextAddCurveToPoint(self, *args, **kwargs): # real signature unknown
        """ (float cp1x, float cp1y, float cp2x, float cp2y, float x, float y) -> None """
        pass

    def CGContextAddLineToPoint(self, *args, **kwargs): # real signature unknown
        """ (float x, float y) -> None """
        pass

    def CGContextAddQuadCurveToPoint(self, *args, **kwargs): # real signature unknown
        """ (float cpx, float cpy, float x, float y) -> None """
        pass

    def CGContextAddRect(self, *args, **kwargs): # real signature unknown
        """ (CGRect rect) -> None """
        pass

    def CGContextBeginPath(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def CGContextClearRect(self, *args, **kwargs): # real signature unknown
        """ (CGRect rect) -> None """
        pass

    def CGContextClip(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def CGContextClipToRect(self, *args, **kwargs): # real signature unknown
        """ (CGRect rect) -> None """
        pass

    def CGContextClosePath(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def CGContextConcatCTM(self, *args, **kwargs): # real signature unknown
        """ (CGAffineTransform transform) -> None """
        pass

    def CGContextDrawPath(self, *args, **kwargs): # real signature unknown
        """ (int mode) -> None """
        pass

    def CGContextEndPage(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def CGContextEOClip(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def CGContextEOFillPath(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def CGContextFillPath(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def CGContextFillRect(self, *args, **kwargs): # real signature unknown
        """ (CGRect rect) -> None """
        pass

    def CGContextFlush(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def CGContextGetCTM(self, *args, **kwargs): # real signature unknown
        """ () -> (CGAffineTransform _rv) """
        pass

    def CGContextGetInterpolationQuality(self, *args, **kwargs): # real signature unknown
        """ () -> (int _rv) """
        pass

    def CGContextGetPathBoundingBox(self, *args, **kwargs): # real signature unknown
        """ () -> (CGRect _rv) """
        pass

    def CGContextGetPathCurrentPoint(self, *args, **kwargs): # real signature unknown
        """ () -> (CGPoint _rv) """
        pass

    def CGContextGetTextMatrix(self, *args, **kwargs): # real signature unknown
        """ () -> (CGAffineTransform _rv) """
        pass

    def CGContextGetTextPosition(self, *args, **kwargs): # real signature unknown
        """ () -> (CGPoint _rv) """
        pass

    def CGContextIsPathEmpty(self, *args, **kwargs): # real signature unknown
        """ () -> (int _rv) """
        pass

    def CGContextMoveToPoint(self, *args, **kwargs): # real signature unknown
        """ (float x, float y) -> None """
        pass

    def CGContextRestoreGState(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def CGContextRotateCTM(self, *args, **kwargs): # real signature unknown
        """ (float angle) -> None """
        pass

    def CGContextSaveGState(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def CGContextScaleCTM(self, *args, **kwargs): # real signature unknown
        """ (float sx, float sy) -> None """
        pass

    def CGContextSelectFont(self, *args, **kwargs): # real signature unknown
        """ (char * name, float size, int textEncoding) -> None """
        pass

    def CGContextSetAlpha(self, *args, **kwargs): # real signature unknown
        """ (float alpha) -> None """
        pass

    def CGContextSetCharacterSpacing(self, *args, **kwargs): # real signature unknown
        """ (float spacing) -> None """
        pass

    def CGContextSetCMYKFillColor(self, *args, **kwargs): # real signature unknown
        """ (float cyan, float magenta, float yellow, float black, float alpha) -> None """
        pass

    def CGContextSetCMYKStrokeColor(self, *args, **kwargs): # real signature unknown
        """ (float cyan, float magenta, float yellow, float black, float alpha) -> None """
        pass

    def CGContextSetFlatness(self, *args, **kwargs): # real signature unknown
        """ (float flatness) -> None """
        pass

    def CGContextSetFontSize(self, *args, **kwargs): # real signature unknown
        """ (float size) -> None """
        pass

    def CGContextSetGrayFillColor(self, *args, **kwargs): # real signature unknown
        """ (float gray, float alpha) -> None """
        pass

    def CGContextSetGrayStrokeColor(self, *args, **kwargs): # real signature unknown
        """ (float gray, float alpha) -> None """
        pass

    def CGContextSetInterpolationQuality(self, *args, **kwargs): # real signature unknown
        """ (int quality) -> None """
        pass

    def CGContextSetLineCap(self, *args, **kwargs): # real signature unknown
        """ (int cap) -> None """
        pass

    def CGContextSetLineJoin(self, *args, **kwargs): # real signature unknown
        """ (int join) -> None """
        pass

    def CGContextSetLineWidth(self, *args, **kwargs): # real signature unknown
        """ (float width) -> None """
        pass

    def CGContextSetMiterLimit(self, *args, **kwargs): # real signature unknown
        """ (float limit) -> None """
        pass

    def CGContextSetRGBFillColor(self, *args, **kwargs): # real signature unknown
        """ (float red, float green, float blue, float alpha) -> None """
        pass

    def CGContextSetRGBStrokeColor(self, *args, **kwargs): # real signature unknown
        """ (float red, float green, float blue, float alpha) -> None """
        pass

    def CGContextSetShouldAntialias(self, *args, **kwargs): # real signature unknown
        """ (int shouldAntialias) -> None """
        pass

    def CGContextSetTextDrawingMode(self, *args, **kwargs): # real signature unknown
        """ (int mode) -> None """
        pass

    def CGContextSetTextMatrix(self, *args, **kwargs): # real signature unknown
        """ (CGAffineTransform transform) -> None """
        pass

    def CGContextSetTextPosition(self, *args, **kwargs): # real signature unknown
        """ (float x, float y) -> None """
        pass

    def CGContextShowText(self, *args, **kwargs): # real signature unknown
        """ (Buffer cstring) -> None """
        pass

    def CGContextShowTextAtPoint(self, *args, **kwargs): # real signature unknown
        """ (float x, float y, Buffer cstring) -> None """
        pass

    def CGContextStrokePath(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def CGContextStrokeRect(self, *args, **kwargs): # real signature unknown
        """ (CGRect rect) -> None """
        pass

    def CGContextStrokeRectWithWidth(self, *args, **kwargs): # real signature unknown
        """ (CGRect rect, float width) -> None """
        pass

    def CGContextSynchronize(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def CGContextTranslateCTM(self, *args, **kwargs): # real signature unknown
        """ (float tx, float ty) -> None """
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


CGContextRef = CGContextRefType


