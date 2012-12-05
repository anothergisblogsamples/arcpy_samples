"""
    @contact: anothergisblog.blogspot.com
    @description: zips a shapefile
    @requirements: Python 2.7.x, ArcGIS 10.1
    @copyright: anothergisblog
"""
import os
import zipfile
from arcpy import env
import arcpy

def trace():
    """
        trace finds the line, the filename and error
        message and returns it to the user
    """
    import inspect
    import traceback
    import sys
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    # script name + line number
    line = tbinfo.split(", ")[1]
    filename = inspect.getfile( inspect.currentframe() )
    # Get Python syntax error
    #
    synerror = traceback.format_exc().splitlines()[-1]
    return line, filename, synerror
def main(*argv):
    """
       Performs the zipping of a shapefile and writes it out
       to either a user specified directory, or to the system
       scratch folder (new at 10.1)
       Inputs:
          shapeFile - path to shapefile
          saveFolder - folder path - optional
       Output(s):
          returns a zip file path as type string
    """
    try:
        shapeFile = argv[0]
        saveFolder = argv[1] #optional

        if saveFolder is None or os.path.isdir(saveFolder) == False:
            saveFolder = env.scratchFolder

        baseName = os.path.basename(shapeFile).split('.')[0]
        baseFolder = os.path.split(shapeFile)[0]
        print saveFolder
        zipFile = saveFolder + os.sep + baseName + ".zip"
        with zipfile.ZipFile(file=zipFile,
                             mode='w',
                             compression=zipfile.ZIP_DEFLATED,
                             allowZip64=True) as myzip:
            for f in os.listdir(baseFolder):
                splitF = os.path.splitext(f)
                if splitF[0].upper() == baseName.upper() and \
                   splitF[1].upper() != '.LOCK':
                    myzip.write(os.path.join(baseFolder, f),
                                f)
                del f
                del splitF
        del baseName
        del baseFolder
        arcpy.SetParameterAsText(3, zipFile)
    except arcpy.ExecuteError:
        line, filename, synerror = trace()
        arcpy.AddError("error on line: %s" % line)
        arcpy.AddError("error in file name: %s" % filename)
        arcpy.AddError("with error message: %s" % synerror)
        arcpy.AddError("ArcPy Error Message: %s" % arcpy.GetMessages(2))
    except:
        line, filename, synerror = trace()
        arcpy.AddError("error on line: %s" % line)
        arcpy.AddError("error in file name: %s" % filename)
        arcpy.AddError("with error message: %s" % synerror)
if __name__ == "__main__":
    env.overwriteOutput = True
    argv = tuple(arcpy.GetParameterAsText(i)
        for i in xrange(arcpy.GetArgumentCount()))
    main(*argv)