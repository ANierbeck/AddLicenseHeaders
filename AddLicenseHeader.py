# -*- coding: utf-8
__author__ = 'anierbeck'

import sys

reload(sys)
sys.setdefaultencoding('utf8')



class FileParser:

    def __init__(self, projectBase):
        self.javaLines = []
        self.pomLines = []
        self.jspLines = []
        self.htmlLines = []
        self.webLines = []
        self.bndLines = []
        self.xmlLines = []
        self.xhtmlLines = []
        self.projectBase = projectBase


    def execute(self, fileName):
        collectLines = False
        with open(self.projectBase+"/target/"+fileName) as ratFile:
            lines = ratFile.readlines()
            for line in lines:
                if "Unapproved licenses:" in line:
                    collectLines = True

                if collectLines and "*******************************" in line:
                    collectLines = False

                if collectLines and len(line) > 0 and ".java" in line:
                    self.javaLines.append(line.strip())

                if collectLines and len(line) > 0 and "pom.xml" in line:
                    self.pomLines.append(line.strip())

                if collectLines and len(line) > 0 and ".jsp" in line:
                    self.jspLines.append(line.strip())

                if collectLines and len(line) > 0 and ".html" in line:
                    self.htmlLines.append(line.strip())

                if collectLines and len(line) > 0 and "web.xml" in line:
                    self.webLines.append(line.strip())

                if collectLines and len(line) > 0 and ".bnd" in line:
                    self.bndLines.append(line.strip())

                if collectLines and len(line) > 0 and ".xml" in line and not "web.xml" in line and not "pom.xml" in line:
                    self.xmlLines.append(line.strip())

                if collectLines and len(line) > 0 and ".xhtml" in line:
                    self.xhtmlLines.append(line.strip())

class AttachHeaderTo:

    def __init__(self, projectBase, header, insertLine):
        self.projectBase = projectBase
        self.header = header
        self.insertLine = insertLine

    def execute(self, listOfFiles):
        for fileName in listOfFiles:
            fileName = self.projectBase + "/" + fileName
            with open(fileName, 'r') as orig:
                data = orig.read()
                with open(fileName, 'w') as modified:
                    if self.insertLine is 0 :
                        modified.write(self.header+data)
                    else:
                        lines = data.splitlines()
                        for x in range(0, self.insertLine):
                            modified.write(lines[x]+"\n")

                        modified.write(self.header)

                        for x in range(self.insertLine, len(lines)):
                            modified.write(lines[x]+"\n")



class AttachHeaderToJava(AttachHeaderTo):

    def __init__(self, projectBase):
        AttachHeaderTo.__init__(self, projectBase, '''/*
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
 * implied.
 *
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
 ''', 0)

class AttachHeaderToPom(AttachHeaderTo):

    def __init__(self, projectBase):
        AttachHeaderTo.__init__(self, projectBase, '''<!--

	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at

	    http://www.apache.org/licenses/LICENSE-2.0

	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.

-->
''', 2)

class AttachHeaderToJsp(AttachHeaderTo):

    def __init__(self, projectBase):
        AttachHeaderTo.__init__(self, projectBase, '''<!--

	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at

	    http://www.apache.org/licenses/LICENSE-2.0

	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.

-->
''', 0)

class AttachHeaderToHtml(AttachHeaderTo):

    def __init__(self, projectBase):
        AttachHeaderTo.__init__(self, projectBase, '''<!--

	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at

	    http://www.apache.org/licenses/LICENSE-2.0

	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.

-->
''', 0)

class AttachHeaderToXml(AttachHeaderTo):

    def __init__(self, projectBase):
        AttachHeaderTo.__init__(self, projectBase, '''<!--

	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at

	    http://www.apache.org/licenses/LICENSE-2.0

	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.

-->
''', 1)

class AttachHeaderToBnd(AttachHeaderTo):

    def __init__(self, projectBase):
        AttachHeaderTo.__init__(self, projectBase, '''#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
''', 0)

if __name__ == '__main__':

    basePath = sys.argv[1]

    fileParser = FileParser(basePath)
    attach2Java = AttachHeaderToJava(basePath)
    attach2Pom = AttachHeaderToPom(basePath)
    attach2jsp = AttachHeaderToJsp(basePath)
    attach2html = AttachHeaderToHtml(basePath)
    attach2xml = AttachHeaderToXml(basePath)
    attach2bnd = AttachHeaderToBnd(basePath)

    fileParser.execute(sys.argv[2])

    attach2Java.execute(fileParser.javaLines)
    attach2Pom.execute(fileParser.pomLines)
    attach2jsp.execute(fileParser.jspLines)
    attach2html.execute(fileParser.htmlLines)
    attach2xml.execute(fileParser.webLines)
    attach2bnd.execute(fileParser.bndLines)
    attach2xml.execute(fileParser.xmlLines)
    attach2xml.execute(fileParser.xhtmlLines)


