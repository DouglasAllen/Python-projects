from OpenGLContext import testingcontext
BaseContext = testingcontext.getInteractive()
from OpenGL.GL import *
#~ class TestContext( BaseContext ):
    #~ """A subclass of the (dynamically determined) BaseContext,
    #~ by overriding various methods, we could customize the
    #~ functionality of this context, but the tutorial doesn't
    #~ ask us to do this."""
#~ if __name__ == "__main__":
    #~ TestContext.ContextMainLoop()