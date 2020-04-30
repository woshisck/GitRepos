# This Python file uses the following encoding: utf-8
#############################################################################
##
## Copyright (C) 2019 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of Qt for Python.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 3 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL3 included in the
## packaging of this file. Please review the following information to
## ensure the GNU Lesser General Public License version 3 requirements
## will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 2.0 or (at your option) the GNU General
## Public license version 3 or any later version approved by the KDE Free
## Qt Foundation. The licenses are as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-2.0.html and
## https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

"""
This file contains the exact signatures for all functions in module
PySide2.QtXml, except for defaults which are replaced by "...".
"""

# Module PySide2.QtXml
import PySide2
from PySide2.support.signature import typing
from PySide2.support.signature.mapping import (
    Virtual, Missing, Invalid, Default, Instance)

class Object(object): pass

import shiboken2 as Shiboken
Shiboken.Object = Object

import PySide2.QtCore
import PySide2.QtXml


class QDomAttr(PySide2.QtXml.QDomNode):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, x:PySide2.QtXml.QDomAttr): ...
    def __copy__(self): ...
    def name(self) -> str: ...
    def nodeType(self) -> PySide2.QtXml.QDomNode.NodeType: ...
    def ownerElement(self) -> PySide2.QtXml.QDomElement: ...
    def setValue(self, arg__1:str): ...
    def specified(self) -> bool: ...
    def value(self) -> str: ...


class QDomCDATASection(PySide2.QtXml.QDomText):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, x:PySide2.QtXml.QDomCDATASection): ...
    def __copy__(self): ...
    def nodeType(self) -> PySide2.QtXml.QDomNode.NodeType: ...


class QDomCharacterData(PySide2.QtXml.QDomNode):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, x:PySide2.QtXml.QDomCharacterData): ...
    def __copy__(self): ...
    def appendData(self, arg:str): ...
    def data(self) -> str: ...
    def deleteData(self, offset:int, count:int): ...
    def insertData(self, offset:int, arg:str): ...
    def length(self) -> int: ...
    def nodeType(self) -> PySide2.QtXml.QDomNode.NodeType: ...
    def replaceData(self, offset:int, count:int, arg:str): ...
    def setData(self, arg__1:str): ...
    def substringData(self, offset:int, count:int) -> str: ...


class QDomComment(PySide2.QtXml.QDomCharacterData):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, x:PySide2.QtXml.QDomComment): ...
    def __copy__(self): ...
    def nodeType(self) -> PySide2.QtXml.QDomNode.NodeType: ...


class QDomDocument(PySide2.QtXml.QDomNode):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doctype:PySide2.QtXml.QDomDocumentType): ...
    @typing.overload
    def __init__(self, name:str): ...
    @typing.overload
    def __init__(self, x:PySide2.QtXml.QDomDocument): ...
    def __copy__(self): ...
    def createAttribute(self, name:str) -> PySide2.QtXml.QDomAttr: ...
    def createAttributeNS(self, nsURI:str, qName:str) -> PySide2.QtXml.QDomAttr: ...
    def createCDATASection(self, data:str) -> PySide2.QtXml.QDomCDATASection: ...
    def createComment(self, data:str) -> PySide2.QtXml.QDomComment: ...
    def createDocumentFragment(self) -> PySide2.QtXml.QDomDocumentFragment: ...
    def createElement(self, tagName:str) -> PySide2.QtXml.QDomElement: ...
    def createElementNS(self, nsURI:str, qName:str) -> PySide2.QtXml.QDomElement: ...
    def createEntityReference(self, name:str) -> PySide2.QtXml.QDomEntityReference: ...
    def createProcessingInstruction(self, target:str, data:str) -> PySide2.QtXml.QDomProcessingInstruction: ...
    def createTextNode(self, data:str) -> PySide2.QtXml.QDomText: ...
    def doctype(self) -> PySide2.QtXml.QDomDocumentType: ...
    def documentElement(self) -> PySide2.QtXml.QDomElement: ...
    def elementById(self, elementId:str) -> PySide2.QtXml.QDomElement: ...
    def elementsByTagName(self, tagname:str) -> PySide2.QtXml.QDomNodeList: ...
    def elementsByTagNameNS(self, nsURI:str, localName:str) -> PySide2.QtXml.QDomNodeList: ...
    def implementation(self) -> PySide2.QtXml.QDomImplementation: ...
    def importNode(self, importedNode:PySide2.QtXml.QDomNode, deep:bool) -> PySide2.QtXml.QDomNode: ...
    def nodeType(self) -> PySide2.QtXml.QDomNode.NodeType: ...
    @typing.overload
    def setContent(self, dev:PySide2.QtCore.QIODevice, errorMsg:str, errorLine:int, errorColumn:int) -> bool: ...
    @typing.overload
    def setContent(self, dev:PySide2.QtCore.QIODevice, namespaceProcessing:bool, errorMsg:str, errorLine:int, errorColumn:int) -> bool: ...
    @typing.overload
    def setContent(self, source:PySide2.QtXml.QXmlInputSource, namespaceProcessing:bool, errorMsg:str, errorLine:int, errorColumn:int) -> bool: ...
    @typing.overload
    def setContent(self, source:PySide2.QtXml.QXmlInputSource, reader:PySide2.QtXml.QXmlReader, errorMsg:str, errorLine:int, errorColumn:int) -> bool: ...
    @typing.overload
    def setContent(self, text:PySide2.QtCore.QByteArray, errorMsg:str, errorLine:int, errorColumn:int) -> bool: ...
    @typing.overload
    def setContent(self, text:PySide2.QtCore.QByteArray, namespaceProcessing:bool, errorMsg:str, errorLine:int, errorColumn:int) -> bool: ...
    @typing.overload
    def setContent(self, text:str, errorMsg:str, errorLine:int, errorColumn:int) -> bool: ...
    @typing.overload
    def setContent(self, text:str, namespaceProcessing:bool, errorMsg:str, errorLine:int, errorColumn:int) -> bool: ...
    def toByteArray(self, arg__1:int=...) -> PySide2.QtCore.QByteArray: ...
    def toString(self, arg__1:int=...) -> str: ...


class QDomDocumentFragment(PySide2.QtXml.QDomNode):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, x:PySide2.QtXml.QDomDocumentFragment): ...
    def __copy__(self): ...
    def nodeType(self) -> PySide2.QtXml.QDomNode.NodeType: ...


class QDomDocumentType(PySide2.QtXml.QDomNode):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, x:PySide2.QtXml.QDomDocumentType): ...
    def __copy__(self): ...
    def entities(self) -> PySide2.QtXml.QDomNamedNodeMap: ...
    def internalSubset(self) -> str: ...
    def name(self) -> str: ...
    def nodeType(self) -> PySide2.QtXml.QDomNode.NodeType: ...
    def notations(self) -> PySide2.QtXml.QDomNamedNodeMap: ...
    def publicId(self) -> str: ...
    def systemId(self) -> str: ...


class QDomElement(PySide2.QtXml.QDomNode):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, x:PySide2.QtXml.QDomElement): ...
    def __copy__(self): ...
    def attribute(self, name:str, defValue:str=...) -> str: ...
    def attributeNS(self, nsURI:str, localName:str, defValue:str=...) -> str: ...
    def attributeNode(self, name:str) -> PySide2.QtXml.QDomAttr: ...
    def attributeNodeNS(self, nsURI:str, localName:str) -> PySide2.QtXml.QDomAttr: ...
    def attributes(self) -> PySide2.QtXml.QDomNamedNodeMap: ...
    def elementsByTagName(self, tagname:str) -> PySide2.QtXml.QDomNodeList: ...
    def elementsByTagNameNS(self, nsURI:str, localName:str) -> PySide2.QtXml.QDomNodeList: ...
    def hasAttribute(self, name:str) -> bool: ...
    def hasAttributeNS(self, nsURI:str, localName:str) -> bool: ...
    def nodeType(self) -> PySide2.QtXml.QDomNode.NodeType: ...
    def removeAttribute(self, name:str): ...
    def removeAttributeNS(self, nsURI:str, localName:str): ...
    def removeAttributeNode(self, oldAttr:PySide2.QtXml.QDomAttr) -> PySide2.QtXml.QDomAttr: ...
    @typing.overload
    def setAttribute(self, name:str, value:str): ...
    @typing.overload
    def setAttribute(self, name:str, value:float): ...
    @typing.overload
    def setAttribute(self, name:str, value:float): ...
    @typing.overload
    def setAttribute(self, name:str, value:int): ...
    @typing.overload
    def setAttribute(self, name:str, value:int): ...
    @typing.overload
    def setAttribute(self, name:str, value:int): ...
    @typing.overload
    def setAttribute(self, name:str, value:int): ...
    @typing.overload
    def setAttributeNS(self, nsURI:str, qName:str, value:str): ...
    @typing.overload
    def setAttributeNS(self, nsURI:str, qName:str, value:float): ...
    @typing.overload
    def setAttributeNS(self, nsURI:str, qName:str, value:int): ...
    @typing.overload
    def setAttributeNS(self, nsURI:str, qName:str, value:int): ...
    @typing.overload
    def setAttributeNS(self, nsURI:str, qName:str, value:int): ...
    @typing.overload
    def setAttributeNS(self, nsURI:str, qName:str, value:int): ...
    def setAttributeNode(self, newAttr:PySide2.QtXml.QDomAttr) -> PySide2.QtXml.QDomAttr: ...
    def setAttributeNodeNS(self, newAttr:PySide2.QtXml.QDomAttr) -> PySide2.QtXml.QDomAttr: ...
    def setTagName(self, name:str): ...
    def tagName(self) -> str: ...
    def text(self) -> str: ...


class QDomEntity(PySide2.QtXml.QDomNode):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, x:PySide2.QtXml.QDomEntity): ...
    def __copy__(self): ...
    def nodeType(self) -> PySide2.QtXml.QDomNode.NodeType: ...
    def notationName(self) -> str: ...
    def publicId(self) -> str: ...
    def systemId(self) -> str: ...


class QDomEntityReference(PySide2.QtXml.QDomNode):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, x:PySide2.QtXml.QDomEntityReference): ...
    def __copy__(self): ...
    def nodeType(self) -> PySide2.QtXml.QDomNode.NodeType: ...


class QDomImplementation(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtXml.QDomImplementation): ...
    def __copy__(self): ...
    def createDocument(self, nsURI:str, qName:str, doctype:PySide2.QtXml.QDomDocumentType) -> PySide2.QtXml.QDomDocument: ...
    def createDocumentType(self, qName:str, publicId:str, systemId:str) -> PySide2.QtXml.QDomDocumentType: ...
    def hasFeature(self, feature:str, version:str) -> bool: ...
    @staticmethod
    def invalidDataPolicy() -> PySide2.QtXml.QDomImplementation.InvalidDataPolicy: ...
    def isNull(self) -> bool: ...
    @staticmethod
    def setInvalidDataPolicy(policy:PySide2.QtXml.QDomImplementation.InvalidDataPolicy): ...


class QDomNamedNodeMap(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtXml.QDomNamedNodeMap): ...
    def __copy__(self): ...
    def contains(self, name:str) -> bool: ...
    def count(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def item(self, index:int) -> PySide2.QtXml.QDomNode: ...
    def length(self) -> int: ...
    def namedItem(self, name:str) -> PySide2.QtXml.QDomNode: ...
    def namedItemNS(self, nsURI:str, localName:str) -> PySide2.QtXml.QDomNode: ...
    def removeNamedItem(self, name:str) -> PySide2.QtXml.QDomNode: ...
    def removeNamedItemNS(self, nsURI:str, localName:str) -> PySide2.QtXml.QDomNode: ...
    def setNamedItem(self, newNode:PySide2.QtXml.QDomNode) -> PySide2.QtXml.QDomNode: ...
    def setNamedItemNS(self, newNode:PySide2.QtXml.QDomNode) -> PySide2.QtXml.QDomNode: ...
    def size(self) -> int: ...


class QDomNode(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtXml.QDomNode): ...
    def __copy__(self): ...
    def __lshift__(self, arg__1:PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    def appendChild(self, newChild:PySide2.QtXml.QDomNode) -> PySide2.QtXml.QDomNode: ...
    def attributes(self) -> PySide2.QtXml.QDomNamedNodeMap: ...
    def childNodes(self) -> PySide2.QtXml.QDomNodeList: ...
    def clear(self): ...
    def cloneNode(self, deep:bool=...) -> PySide2.QtXml.QDomNode: ...
    def columnNumber(self) -> int: ...
    def firstChild(self) -> PySide2.QtXml.QDomNode: ...
    def firstChildElement(self, tagName:str=...) -> PySide2.QtXml.QDomElement: ...
    def hasAttributes(self) -> bool: ...
    def hasChildNodes(self) -> bool: ...
    def insertAfter(self, newChild:PySide2.QtXml.QDomNode, refChild:PySide2.QtXml.QDomNode) -> PySide2.QtXml.QDomNode: ...
    def insertBefore(self, newChild:PySide2.QtXml.QDomNode, refChild:PySide2.QtXml.QDomNode) -> PySide2.QtXml.QDomNode: ...
    def isAttr(self) -> bool: ...
    def isCDATASection(self) -> bool: ...
    def isCharacterData(self) -> bool: ...
    def isComment(self) -> bool: ...
    def isDocument(self) -> bool: ...
    def isDocumentFragment(self) -> bool: ...
    def isDocumentType(self) -> bool: ...
    def isElement(self) -> bool: ...
    def isEntity(self) -> bool: ...
    def isEntityReference(self) -> bool: ...
    def isNotation(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isProcessingInstruction(self) -> bool: ...
    def isSupported(self, feature:str, version:str) -> bool: ...
    def isText(self) -> bool: ...
    def lastChild(self) -> PySide2.QtXml.QDomNode: ...
    def lastChildElement(self, tagName:str=...) -> PySide2.QtXml.QDomElement: ...
    def lineNumber(self) -> int: ...
    def localName(self) -> str: ...
    def namedItem(self, name:str) -> PySide2.QtXml.QDomNode: ...
    def namespaceURI(self) -> str: ...
    def nextSibling(self) -> PySide2.QtXml.QDomNode: ...
    def nextSiblingElement(self, taName:str=...) -> PySide2.QtXml.QDomElement: ...
    def nodeName(self) -> str: ...
    def nodeType(self) -> PySide2.QtXml.QDomNode.NodeType: ...
    def nodeValue(self) -> str: ...
    def normalize(self): ...
    def ownerDocument(self) -> PySide2.QtXml.QDomDocument: ...
    def parentNode(self) -> PySide2.QtXml.QDomNode: ...
    def prefix(self) -> str: ...
    def previousSibling(self) -> PySide2.QtXml.QDomNode: ...
    def previousSiblingElement(self, tagName:str=...) -> PySide2.QtXml.QDomElement: ...
    def removeChild(self, oldChild:PySide2.QtXml.QDomNode) -> PySide2.QtXml.QDomNode: ...
    def replaceChild(self, newChild:PySide2.QtXml.QDomNode, oldChild:PySide2.QtXml.QDomNode) -> PySide2.QtXml.QDomNode: ...
    def save(self, arg__1:PySide2.QtCore.QTextStream, arg__2:int, arg__3:PySide2.QtXml.QDomNode.EncodingPolicy=...): ...
    def setNodeValue(self, arg__1:str): ...
    def setPrefix(self, pre:str): ...
    def toAttr(self) -> PySide2.QtXml.QDomAttr: ...
    def toCDATASection(self) -> PySide2.QtXml.QDomCDATASection: ...
    def toCharacterData(self) -> PySide2.QtXml.QDomCharacterData: ...
    def toComment(self) -> PySide2.QtXml.QDomComment: ...
    def toDocument(self) -> PySide2.QtXml.QDomDocument: ...
    def toDocumentFragment(self) -> PySide2.QtXml.QDomDocumentFragment: ...
    def toDocumentType(self) -> PySide2.QtXml.QDomDocumentType: ...
    def toElement(self) -> PySide2.QtXml.QDomElement: ...
    def toEntity(self) -> PySide2.QtXml.QDomEntity: ...
    def toEntityReference(self) -> PySide2.QtXml.QDomEntityReference: ...
    def toNotation(self) -> PySide2.QtXml.QDomNotation: ...
    def toProcessingInstruction(self) -> PySide2.QtXml.QDomProcessingInstruction: ...
    def toText(self) -> PySide2.QtXml.QDomText: ...


class QDomNodeList(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtXml.QDomNodeList): ...
    def __copy__(self): ...
    def at(self, index:int) -> PySide2.QtXml.QDomNode: ...
    def count(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def item(self, index:int) -> PySide2.QtXml.QDomNode: ...
    def length(self) -> int: ...
    def size(self) -> int: ...


class QDomNotation(PySide2.QtXml.QDomNode):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, x:PySide2.QtXml.QDomNotation): ...
    def __copy__(self): ...
    def nodeType(self) -> PySide2.QtXml.QDomNode.NodeType: ...
    def publicId(self) -> str: ...
    def systemId(self) -> str: ...


class QDomProcessingInstruction(PySide2.QtXml.QDomNode):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, x:PySide2.QtXml.QDomProcessingInstruction): ...
    def __copy__(self): ...
    def data(self) -> str: ...
    def nodeType(self) -> PySide2.QtXml.QDomNode.NodeType: ...
    def setData(self, d:str): ...
    def target(self) -> str: ...


class QDomText(PySide2.QtXml.QDomCharacterData):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, x:PySide2.QtXml.QDomText): ...
    def __copy__(self): ...
    def nodeType(self) -> PySide2.QtXml.QDomNode.NodeType: ...
    def splitText(self, offset:int) -> PySide2.QtXml.QDomText: ...


class QXmlAttributes(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, arg__1:PySide2.QtXml.QXmlAttributes): ...
    def __copy__(self): ...
    def append(self, qName:str, uri:str, localPart:str, value:str): ...
    def clear(self): ...
    def count(self) -> int: ...
    @typing.overload
    def index(self, qName:str) -> int: ...
    @typing.overload
    def index(self, uri:str, localPart:str) -> int: ...
    def length(self) -> int: ...
    def localName(self, index:int) -> str: ...
    def qName(self, index:int) -> str: ...
    def swap(self, other:PySide2.QtXml.QXmlAttributes): ...
    @typing.overload
    def type(self, index:int) -> str: ...
    @typing.overload
    def type(self, qName:str) -> str: ...
    @typing.overload
    def type(self, uri:str, localName:str) -> str: ...
    def uri(self, index:int) -> str: ...
    @typing.overload
    def value(self, index:int) -> str: ...
    @typing.overload
    def value(self, qName:str) -> str: ...
    @typing.overload
    def value(self, uri:str, localName:str) -> str: ...


class QXmlContentHandler(Shiboken.Object):

    def __init__(self): ...
    def characters(self, ch:str) -> bool: ...
    def endDocument(self) -> bool: ...
    def endElement(self, namespaceURI:str, localName:str, qName:str) -> bool: ...
    def endPrefixMapping(self, prefix:str) -> bool: ...
    def errorString(self) -> str: ...
    def ignorableWhitespace(self, ch:str) -> bool: ...
    def processingInstruction(self, target:str, data:str) -> bool: ...
    def setDocumentLocator(self, locator:PySide2.QtXml.QXmlLocator): ...
    def skippedEntity(self, name:str) -> bool: ...
    def startDocument(self) -> bool: ...
    def startElement(self, namespaceURI:str, localName:str, qName:str, atts:PySide2.QtXml.QXmlAttributes) -> bool: ...
    def startPrefixMapping(self, prefix:str, uri:str) -> bool: ...


class QXmlDTDHandler(Shiboken.Object):

    def __init__(self): ...
    def errorString(self) -> str: ...
    def notationDecl(self, name:str, publicId:str, systemId:str) -> bool: ...
    def unparsedEntityDecl(self, name:str, publicId:str, systemId:str, notationName:str) -> bool: ...


class QXmlDeclHandler(Shiboken.Object):

    def __init__(self): ...
    def attributeDecl(self, eName:str, aName:str, type:str, valueDefault:str, value:str) -> bool: ...
    def errorString(self) -> str: ...
    def externalEntityDecl(self, name:str, publicId:str, systemId:str) -> bool: ...
    def internalEntityDecl(self, name:str, value:str) -> bool: ...


class QXmlDefaultHandler(PySide2.QtXml.QXmlContentHandler, PySide2.QtXml.QXmlErrorHandler, PySide2.QtXml.QXmlDTDHandler, PySide2.QtXml.QXmlEntityResolver, PySide2.QtXml.QXmlLexicalHandler, PySide2.QtXml.QXmlDeclHandler):

    def __init__(self): ...
    def attributeDecl(self, eName:str, aName:str, type:str, valueDefault:str, value:str) -> bool: ...
    def characters(self, ch:str) -> bool: ...
    def comment(self, ch:str) -> bool: ...
    def endCDATA(self) -> bool: ...
    def endDTD(self) -> bool: ...
    def endDocument(self) -> bool: ...
    def endElement(self, namespaceURI:str, localName:str, qName:str) -> bool: ...
    def endEntity(self, name:str) -> bool: ...
    def endPrefixMapping(self, prefix:str) -> bool: ...
    def error(self, exception:PySide2.QtXml.QXmlParseException) -> bool: ...
    def errorString(self) -> str: ...
    def externalEntityDecl(self, name:str, publicId:str, systemId:str) -> bool: ...
    def fatalError(self, exception:PySide2.QtXml.QXmlParseException) -> bool: ...
    def ignorableWhitespace(self, ch:str) -> bool: ...
    def internalEntityDecl(self, name:str, value:str) -> bool: ...
    def notationDecl(self, name:str, publicId:str, systemId:str) -> bool: ...
    def processingInstruction(self, target:str, data:str) -> bool: ...
    def resolveEntity(self, publicId:str, systemId:str, ret:PySide2.QtXml.QXmlInputSource) -> bool: ...
    def setDocumentLocator(self, locator:PySide2.QtXml.QXmlLocator): ...
    def skippedEntity(self, name:str) -> bool: ...
    def startCDATA(self) -> bool: ...
    def startDTD(self, name:str, publicId:str, systemId:str) -> bool: ...
    def startDocument(self) -> bool: ...
    def startElement(self, namespaceURI:str, localName:str, qName:str, atts:PySide2.QtXml.QXmlAttributes) -> bool: ...
    def startEntity(self, name:str) -> bool: ...
    def startPrefixMapping(self, prefix:str, uri:str) -> bool: ...
    def unparsedEntityDecl(self, name:str, publicId:str, systemId:str, notationName:str) -> bool: ...
    def warning(self, exception:PySide2.QtXml.QXmlParseException) -> bool: ...


class QXmlEntityResolver(Shiboken.Object):

    def __init__(self): ...
    def errorString(self) -> str: ...
    def resolveEntity(self, publicId:str, systemId:str, ret:PySide2.QtXml.QXmlInputSource) -> bool: ...


class QXmlErrorHandler(Shiboken.Object):

    def __init__(self): ...
    def error(self, exception:PySide2.QtXml.QXmlParseException) -> bool: ...
    def errorString(self) -> str: ...
    def fatalError(self, exception:PySide2.QtXml.QXmlParseException) -> bool: ...
    def warning(self, exception:PySide2.QtXml.QXmlParseException) -> bool: ...


class QXmlInputSource(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, dev:PySide2.QtCore.QIODevice): ...
    def data(self) -> str: ...
    def fetchData(self): ...
    def fromRawData(self, data:PySide2.QtCore.QByteArray, beginning:bool=...) -> str: ...
    def next(self) -> typing.Char: ...
    def reset(self): ...
    @typing.overload
    def setData(self, dat:PySide2.QtCore.QByteArray): ...
    @typing.overload
    def setData(self, dat:str): ...


class QXmlLexicalHandler(Shiboken.Object):

    def __init__(self): ...
    def comment(self, ch:str) -> bool: ...
    def endCDATA(self) -> bool: ...
    def endDTD(self) -> bool: ...
    def endEntity(self, name:str) -> bool: ...
    def errorString(self) -> str: ...
    def startCDATA(self) -> bool: ...
    def startDTD(self, name:str, publicId:str, systemId:str) -> bool: ...
    def startEntity(self, name:str) -> bool: ...


class QXmlLocator(Shiboken.Object):

    def __init__(self): ...
    def columnNumber(self) -> int: ...
    def lineNumber(self) -> int: ...


class QXmlNamespaceSupport(Shiboken.Object):

    def __init__(self): ...
    def popContext(self): ...
    def prefix(self, arg__1:str) -> str: ...
    @typing.overload
    def prefixes(self) -> typing.List: ...
    @typing.overload
    def prefixes(self, arg__1:str) -> typing.List: ...
    def processName(self, arg__1:str, arg__2:bool, arg__3:str, arg__4:str): ...
    def pushContext(self): ...
    def reset(self): ...
    def setPrefix(self, arg__1:str, arg__2:str): ...
    def splitName(self, arg__1:str, arg__2:str, arg__3:str): ...
    def uri(self, arg__1:str) -> str: ...


class QXmlParseException(Shiboken.Object):

    @typing.overload
    def __init__(self, name:str=..., c:int=..., l:int=..., p:str=..., s:str=...): ...
    @typing.overload
    def __init__(self, other:PySide2.QtXml.QXmlParseException): ...
    def columnNumber(self) -> int: ...
    def lineNumber(self) -> int: ...
    def message(self) -> str: ...
    def publicId(self) -> str: ...
    def systemId(self) -> str: ...


class QXmlReader(Shiboken.Object):

    def __init__(self): ...
    def DTDHandler(self) -> PySide2.QtXml.QXmlDTDHandler: ...
    def contentHandler(self) -> PySide2.QtXml.QXmlContentHandler: ...
    def declHandler(self) -> PySide2.QtXml.QXmlDeclHandler: ...
    def entityResolver(self) -> PySide2.QtXml.QXmlEntityResolver: ...
    def errorHandler(self) -> PySide2.QtXml.QXmlErrorHandler: ...
    def feature(self, name:str, ok:bool) -> bool: ...
    def hasFeature(self, name:str) -> bool: ...
    def hasProperty(self, name:str) -> bool: ...
    def lexicalHandler(self) -> PySide2.QtXml.QXmlLexicalHandler: ...
    def parse(self, input:PySide2.QtXml.QXmlInputSource) -> bool: ...
    def property(self, name:str, ok:bool) -> int: ...
    def setContentHandler(self, handler:PySide2.QtXml.QXmlContentHandler): ...
    def setDTDHandler(self, handler:PySide2.QtXml.QXmlDTDHandler): ...
    def setDeclHandler(self, handler:PySide2.QtXml.QXmlDeclHandler): ...
    def setEntityResolver(self, handler:PySide2.QtXml.QXmlEntityResolver): ...
    def setErrorHandler(self, handler:PySide2.QtXml.QXmlErrorHandler): ...
    def setFeature(self, name:str, value:bool): ...
    def setLexicalHandler(self, handler:PySide2.QtXml.QXmlLexicalHandler): ...
    def setProperty(self, name:str, value:int): ...


class QXmlSimpleReader(PySide2.QtXml.QXmlReader):

    def __init__(self): ...
    def DTDHandler(self) -> PySide2.QtXml.QXmlDTDHandler: ...
    def contentHandler(self) -> PySide2.QtXml.QXmlContentHandler: ...
    def declHandler(self) -> PySide2.QtXml.QXmlDeclHandler: ...
    def entityResolver(self) -> PySide2.QtXml.QXmlEntityResolver: ...
    def errorHandler(self) -> PySide2.QtXml.QXmlErrorHandler: ...
    def feature(self, name:str, ok:bool) -> bool: ...
    def hasFeature(self, name:str) -> bool: ...
    def hasProperty(self, name:str) -> bool: ...
    def lexicalHandler(self) -> PySide2.QtXml.QXmlLexicalHandler: ...
    @typing.overload
    def parse(self, input:PySide2.QtXml.QXmlInputSource) -> bool: ...
    @typing.overload
    def parse(self, input:PySide2.QtXml.QXmlInputSource, incremental:bool) -> bool: ...
    def parseContinue(self) -> bool: ...
    def property(self, name:str, ok:bool) -> int: ...
    def setContentHandler(self, handler:PySide2.QtXml.QXmlContentHandler): ...
    def setDTDHandler(self, handler:PySide2.QtXml.QXmlDTDHandler): ...
    def setDeclHandler(self, handler:PySide2.QtXml.QXmlDeclHandler): ...
    def setEntityResolver(self, handler:PySide2.QtXml.QXmlEntityResolver): ...
    def setErrorHandler(self, handler:PySide2.QtXml.QXmlErrorHandler): ...
    def setFeature(self, name:str, value:bool): ...
    def setLexicalHandler(self, handler:PySide2.QtXml.QXmlLexicalHandler): ...
    def setProperty(self, name:str, value:int): ...

# eof
