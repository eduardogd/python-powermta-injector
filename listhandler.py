"""
Copyright (c) 2012, William Betts
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution. 
3. Redistributions of source code must reproduce the author lines at the top 
   of the original files. You may add to them (i.e. mention you modified the 
   file), but you may not subtract from them.
4. If redistributed in binary form you may not strip the author lines from any
   files before compiling.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies, 
either expressed or implied, of the FreeBSD Project.

Author: William Betts
File: listhandler.py
Date: 8-01-2012

Comment:
    This class handles processing the email list for the injector.
"""

class ListHandler(object):
    def __init__(self, listname):
        try:
            with open('lists/' + listname) as fh: 
               self.__list = [line.strip() for line in fh.readlines()]
               fh.close()
        except IOError as e:
            e.strerror = 'The list %s doesn\'t exist' % (listname)
            raise e


    def GetAddress(self):
        if (len(self.__list) > 0):
            address = self.__list[0]
            del self.__list[0]
            return address
        else:
            return None


