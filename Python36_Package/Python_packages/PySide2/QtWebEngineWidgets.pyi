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
PySide2.QtWebEngineWidgets, except for defaults which are replaced by "...".
"""

# Module PySide2.QtWebEngineWidgets
import PySide2
from PySide2.support.signature import typing
from PySide2.support.signature.mapping import (
    Virtual, Missing, Invalid, Default, Instance)

class Object(object): pass

import shiboken2 as Shiboken
Shiboken.Object = Object

import PySide2.QtCore
import PySide2.QtGui
import PySide2.QtWidgets
import PySide2.QtWebChannel
import PySide2.QtWebEngineCore
import PySide2.QtWebEngineWidgets


class QWebEngineCertificateError(Shiboken.Object):

    def __init__(self, error:int, url:PySide2.QtCore.QUrl, overridable:bool, errorDescription:str): ...
    def error(self) -> PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error: ...
    def errorDescription(self) -> str: ...
    def isOverridable(self) -> bool: ...
    def url(self) -> PySide2.QtCore.QUrl: ...


class QWebEngineContextMenuData(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtWebEngineWidgets.QWebEngineContextMenuData): ...
    def __copy__(self): ...
    def editFlags(self) -> PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.EditFlags: ...
    def isContentEditable(self) -> bool: ...
    def isValid(self) -> bool: ...
    def linkText(self) -> str: ...
    def linkUrl(self) -> PySide2.QtCore.QUrl: ...
    def mediaFlags(self) -> PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaFlags: ...
    def mediaType(self) -> PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaType: ...
    def mediaUrl(self) -> PySide2.QtCore.QUrl: ...
    def misspelledWord(self) -> str: ...
    def position(self) -> PySide2.QtCore.QPoint: ...
    def selectedText(self) -> str: ...
    def spellCheckerSuggestions(self) -> typing.List: ...


class QWebEngineDownloadItem(PySide2.QtCore.QObject):

    def accept(self): ...
    def cancel(self): ...
    def id(self) -> int: ...
    def interruptReason(self) -> PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason: ...
    def interruptReasonString(self) -> str: ...
    def isFinished(self) -> bool: ...
    def isPaused(self) -> bool: ...
    def isSavePageDownload(self) -> bool: ...
    def mimeType(self) -> str: ...
    def page(self) -> PySide2.QtWebEngineWidgets.QWebEnginePage: ...
    def path(self) -> str: ...
    def pause(self): ...
    def receivedBytes(self) -> int: ...
    def resume(self): ...
    def savePageFormat(self) -> PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.SavePageFormat: ...
    def setPath(self, path:str): ...
    def setSavePageFormat(self, format:PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.SavePageFormat): ...
    def state(self) -> PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadState: ...
    def totalBytes(self) -> int: ...
    def type(self) -> PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadType: ...
    def url(self) -> PySide2.QtCore.QUrl: ...


class QWebEngineFullScreenRequest(Shiboken.Object):

    def accept(self): ...
    def origin(self) -> PySide2.QtCore.QUrl: ...
    def reject(self): ...
    def toggleOn(self) -> bool: ...


class QWebEngineHistory(Shiboken.Object):

    def __lshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def __rshift__(self, stream:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def back(self): ...
    def backItem(self) -> PySide2.QtWebEngineWidgets.QWebEngineHistoryItem: ...
    def backItems(self, maxItems:int) -> typing.List: ...
    def canGoBack(self) -> bool: ...
    def canGoForward(self) -> bool: ...
    def clear(self): ...
    def count(self) -> int: ...
    def currentItem(self) -> PySide2.QtWebEngineWidgets.QWebEngineHistoryItem: ...
    def currentItemIndex(self) -> int: ...
    def forward(self): ...
    def forwardItem(self) -> PySide2.QtWebEngineWidgets.QWebEngineHistoryItem: ...
    def forwardItems(self, maxItems:int) -> typing.List: ...
    def goToItem(self, item:PySide2.QtWebEngineWidgets.QWebEngineHistoryItem): ...
    def itemAt(self, i:int) -> PySide2.QtWebEngineWidgets.QWebEngineHistoryItem: ...
    def items(self) -> typing.List: ...


class QWebEngineHistoryItem(Shiboken.Object):

    def __init__(self, other:PySide2.QtWebEngineWidgets.QWebEngineHistoryItem): ...
    def __copy__(self): ...
    def iconUrl(self) -> PySide2.QtCore.QUrl: ...
    def isValid(self) -> bool: ...
    def lastVisited(self) -> PySide2.QtCore.QDateTime: ...
    def originalUrl(self) -> PySide2.QtCore.QUrl: ...
    def swap(self, other:PySide2.QtWebEngineWidgets.QWebEngineHistoryItem): ...
    def title(self) -> str: ...
    def url(self) -> PySide2.QtCore.QUrl: ...


class QWebEnginePage(PySide2.QtCore.QObject):

    @typing.overload
    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    @typing.overload
    def __init__(self, profile:PySide2.QtWebEngineWidgets.QWebEngineProfile, parent:PySide2.QtCore.QObject=...): ...
    def acceptNavigationRequest(self, url:PySide2.QtCore.QUrl, type:PySide2.QtWebEngineWidgets.QWebEnginePage.NavigationType, isMainFrame:bool) -> bool: ...
    def action(self, action:PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction) -> PySide2.QtWidgets.QAction: ...
    def backgroundColor(self) -> PySide2.QtGui.QColor: ...
    def certificateError(self, certificateError:PySide2.QtWebEngineWidgets.QWebEngineCertificateError) -> bool: ...
    def chooseFiles(self, mode:PySide2.QtWebEngineWidgets.QWebEnginePage.FileSelectionMode, oldFiles:typing.List, acceptedMimeTypes:typing.List) -> typing.List: ...
    def contentsSize(self) -> PySide2.QtCore.QSizeF: ...
    def contextMenuData(self) -> PySide2.QtWebEngineWidgets.QWebEngineContextMenuData: ...
    def createStandardContextMenu(self) -> PySide2.QtWidgets.QMenu: ...
    def createWindow(self, type:PySide2.QtWebEngineWidgets.QWebEnginePage.WebWindowType) -> PySide2.QtWebEngineWidgets.QWebEnginePage: ...
    def devToolsPage(self) -> PySide2.QtWebEngineWidgets.QWebEnginePage: ...
    def download(self, url:PySide2.QtCore.QUrl, filename:str=...): ...
    def event(self, arg__1:PySide2.QtCore.QEvent) -> bool: ...
    def findText(self, subString:str, options:PySide2.QtWebEngineWidgets.QWebEnginePage.FindFlags=...): ...
    def hasSelection(self) -> bool: ...
    def history(self) -> PySide2.QtWebEngineWidgets.QWebEngineHistory: ...
    def icon(self) -> PySide2.QtGui.QIcon: ...
    def iconUrl(self) -> PySide2.QtCore.QUrl: ...
    def inspectedPage(self) -> PySide2.QtWebEngineWidgets.QWebEnginePage: ...
    def isAudioMuted(self) -> bool: ...
    def javaScriptAlert(self, securityOrigin:PySide2.QtCore.QUrl, msg:str): ...
    def javaScriptConfirm(self, securityOrigin:PySide2.QtCore.QUrl, msg:str) -> bool: ...
    def javaScriptConsoleMessage(self, level:PySide2.QtWebEngineWidgets.QWebEnginePage.JavaScriptConsoleMessageLevel, message:str, lineNumber:int, sourceID:str): ...
    def javaScriptPrompt(self, securityOrigin:PySide2.QtCore.QUrl, msg:str, defaultValue:str, result:str) -> bool: ...
    @typing.overload
    def load(self, request:PySide2.QtWebEngineCore.QWebEngineHttpRequest): ...
    @typing.overload
    def load(self, url:PySide2.QtCore.QUrl): ...
    def printToPdf(self, filePath:str, layout:PySide2.QtGui.QPageLayout=...): ...
    def profile(self) -> PySide2.QtWebEngineWidgets.QWebEngineProfile: ...
    def recentlyAudible(self) -> bool: ...
    def replaceMisspelledWord(self, replacement:str): ...
    def requestedUrl(self) -> PySide2.QtCore.QUrl: ...
    @typing.overload
    def runJavaScript(self, scriptSource:str): ...
    @typing.overload
    def runJavaScript(self, scriptSource:str, worldId:int): ...
    def save(self, filePath:str, format:PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.SavePageFormat=...): ...
    def scripts(self) -> PySide2.QtWebEngineWidgets.QWebEngineScriptCollection: ...
    def scrollPosition(self) -> PySide2.QtCore.QPointF: ...
    def selectedText(self) -> str: ...
    def setAudioMuted(self, muted:bool): ...
    def setBackgroundColor(self, color:PySide2.QtGui.QColor): ...
    def setContent(self, data:PySide2.QtCore.QByteArray, mimeType:str=..., baseUrl:PySide2.QtCore.QUrl=...): ...
    def setDevToolsPage(self, page:PySide2.QtWebEngineWidgets.QWebEnginePage): ...
    def setFeaturePermission(self, securityOrigin:PySide2.QtCore.QUrl, feature:PySide2.QtWebEngineWidgets.QWebEnginePage.Feature, policy:PySide2.QtWebEngineWidgets.QWebEnginePage.PermissionPolicy): ...
    def setHtml(self, html:str, baseUrl:PySide2.QtCore.QUrl=...): ...
    def setInspectedPage(self, page:PySide2.QtWebEngineWidgets.QWebEnginePage): ...
    def setUrl(self, url:PySide2.QtCore.QUrl): ...
    def setView(self, view:PySide2.QtWidgets.QWidget): ...
    @typing.overload
    def setWebChannel(self, arg__1:PySide2.QtWebChannel.QWebChannel): ...
    @typing.overload
    def setWebChannel(self, arg__1:PySide2.QtWebChannel.QWebChannel, worldId:int): ...
    def setZoomFactor(self, factor:float): ...
    def settings(self) -> PySide2.QtWebEngineWidgets.QWebEngineSettings: ...
    def title(self) -> str: ...
    def triggerAction(self, action:PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction, checked:bool=...): ...
    def url(self) -> PySide2.QtCore.QUrl: ...
    def view(self) -> PySide2.QtWidgets.QWidget: ...
    def webChannel(self) -> PySide2.QtWebChannel.QWebChannel: ...
    def zoomFactor(self) -> float: ...


class QWebEngineProfile(PySide2.QtCore.QObject):

    @typing.overload
    def __init__(self, name:str, parent:PySide2.QtCore.QObject=...): ...
    @typing.overload
    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def cachePath(self) -> str: ...
    def clearAllVisitedLinks(self): ...
    def clearHttpCache(self): ...
    def clearVisitedLinks(self, urls:typing.List): ...
    def cookieStore(self) -> PySide2.QtWebEngineCore.QWebEngineCookieStore: ...
    @staticmethod
    def defaultProfile() -> PySide2.QtWebEngineWidgets.QWebEngineProfile: ...
    def httpAcceptLanguage(self) -> str: ...
    def httpCacheMaximumSize(self) -> int: ...
    def httpCacheType(self) -> PySide2.QtWebEngineWidgets.QWebEngineProfile.HttpCacheType: ...
    def httpUserAgent(self) -> str: ...
    def installUrlSchemeHandler(self, scheme:PySide2.QtCore.QByteArray, arg__2:PySide2.QtWebEngineCore.QWebEngineUrlSchemeHandler): ...
    def isOffTheRecord(self) -> bool: ...
    def isSpellCheckEnabled(self) -> bool: ...
    def persistentCookiesPolicy(self) -> PySide2.QtWebEngineWidgets.QWebEngineProfile.PersistentCookiesPolicy: ...
    def persistentStoragePath(self) -> str: ...
    def removeAllUrlSchemeHandlers(self): ...
    def removeUrlScheme(self, scheme:PySide2.QtCore.QByteArray): ...
    def removeUrlSchemeHandler(self, arg__1:PySide2.QtWebEngineCore.QWebEngineUrlSchemeHandler): ...
    def scripts(self) -> PySide2.QtWebEngineWidgets.QWebEngineScriptCollection: ...
    def setCachePath(self, path:str): ...
    def setHttpAcceptLanguage(self, httpAcceptLanguage:str): ...
    def setHttpCacheMaximumSize(self, maxSize:int): ...
    def setHttpCacheType(self, arg__1:PySide2.QtWebEngineWidgets.QWebEngineProfile.HttpCacheType): ...
    def setHttpUserAgent(self, userAgent:str): ...
    def setPersistentCookiesPolicy(self, arg__1:PySide2.QtWebEngineWidgets.QWebEngineProfile.PersistentCookiesPolicy): ...
    def setPersistentStoragePath(self, path:str): ...
    def setRequestInterceptor(self, interceptor:PySide2.QtWebEngineCore.QWebEngineUrlRequestInterceptor): ...
    def setSpellCheckEnabled(self, enabled:bool): ...
    def setSpellCheckLanguages(self, languages:typing.List): ...
    def settings(self) -> PySide2.QtWebEngineWidgets.QWebEngineSettings: ...
    def spellCheckLanguages(self) -> typing.List: ...
    def storageName(self) -> str: ...
    def urlSchemeHandler(self, arg__1:PySide2.QtCore.QByteArray) -> PySide2.QtWebEngineCore.QWebEngineUrlSchemeHandler: ...
    def visitedLinksContainsUrl(self, url:PySide2.QtCore.QUrl) -> bool: ...


class QWebEngineScript(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtWebEngineWidgets.QWebEngineScript): ...
    def __copy__(self): ...
    def injectionPoint(self) -> PySide2.QtWebEngineWidgets.QWebEngineScript.InjectionPoint: ...
    def isNull(self) -> bool: ...
    def name(self) -> str: ...
    def runsOnSubFrames(self) -> bool: ...
    def setInjectionPoint(self, arg__1:PySide2.QtWebEngineWidgets.QWebEngineScript.InjectionPoint): ...
    def setName(self, arg__1:str): ...
    def setRunsOnSubFrames(self, on:bool): ...
    def setSourceCode(self, arg__1:str): ...
    def setWorldId(self, arg__1:int): ...
    def sourceCode(self) -> str: ...
    def swap(self, other:PySide2.QtWebEngineWidgets.QWebEngineScript): ...
    def worldId(self) -> int: ...


class QWebEngineScriptCollection(Shiboken.Object):

    def clear(self): ...
    def contains(self, value:PySide2.QtWebEngineWidgets.QWebEngineScript) -> bool: ...
    def count(self) -> int: ...
    def findScript(self, name:str) -> PySide2.QtWebEngineWidgets.QWebEngineScript: ...
    def findScripts(self, name:str) -> typing.List: ...
    @typing.overload
    def insert(self, arg__1:PySide2.QtWebEngineWidgets.QWebEngineScript): ...
    @typing.overload
    def insert(self, list:typing.List): ...
    def isEmpty(self) -> bool: ...
    def remove(self, arg__1:PySide2.QtWebEngineWidgets.QWebEngineScript) -> bool: ...
    def size(self) -> int: ...
    def toList(self) -> typing.List: ...


class QWebEngineSettings(Shiboken.Object):

    @staticmethod
    def defaultSettings() -> PySide2.QtWebEngineWidgets.QWebEngineSettings: ...
    def defaultTextEncoding(self) -> str: ...
    def fontFamily(self, which:PySide2.QtWebEngineWidgets.QWebEngineSettings.FontFamily) -> str: ...
    def fontSize(self, type:PySide2.QtWebEngineWidgets.QWebEngineSettings.FontSize) -> int: ...
    @staticmethod
    def globalSettings() -> PySide2.QtWebEngineWidgets.QWebEngineSettings: ...
    def resetAttribute(self, attr:PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute): ...
    def resetFontFamily(self, which:PySide2.QtWebEngineWidgets.QWebEngineSettings.FontFamily): ...
    def resetFontSize(self, type:PySide2.QtWebEngineWidgets.QWebEngineSettings.FontSize): ...
    def resetUnknownUrlSchemePolicy(self): ...
    def setAttribute(self, attr:PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute, on:bool): ...
    def setDefaultTextEncoding(self, encoding:str): ...
    def setFontFamily(self, which:PySide2.QtWebEngineWidgets.QWebEngineSettings.FontFamily, family:str): ...
    def setFontSize(self, type:PySide2.QtWebEngineWidgets.QWebEngineSettings.FontSize, size:int): ...
    def setUnknownUrlSchemePolicy(self, policy:PySide2.QtWebEngineWidgets.QWebEngineSettings.UnknownUrlSchemePolicy): ...
    def testAttribute(self, attr:PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute) -> bool: ...
    def unknownUrlSchemePolicy(self) -> PySide2.QtWebEngineWidgets.QWebEngineSettings.UnknownUrlSchemePolicy: ...


class QWebEngineView(PySide2.QtWidgets.QWidget):

    def __init__(self, parent:PySide2.QtWidgets.QWidget=...): ...
    def back(self): ...
    def contextMenuEvent(self, arg__1:PySide2.QtGui.QContextMenuEvent): ...
    def createWindow(self, type:PySide2.QtWebEngineWidgets.QWebEnginePage.WebWindowType) -> PySide2.QtWebEngineWidgets.QWebEngineView: ...
    def dragEnterEvent(self, e:PySide2.QtGui.QDragEnterEvent): ...
    def dragLeaveEvent(self, e:PySide2.QtGui.QDragLeaveEvent): ...
    def dragMoveEvent(self, e:PySide2.QtGui.QDragMoveEvent): ...
    def dropEvent(self, e:PySide2.QtGui.QDropEvent): ...
    def event(self, arg__1:PySide2.QtCore.QEvent) -> bool: ...
    def findText(self, subString:str, options:PySide2.QtWebEngineWidgets.QWebEnginePage.FindFlags=...): ...
    def forward(self): ...
    def hasSelection(self) -> bool: ...
    def hideEvent(self, arg__1:PySide2.QtGui.QHideEvent): ...
    def history(self) -> PySide2.QtWebEngineWidgets.QWebEngineHistory: ...
    def icon(self) -> PySide2.QtGui.QIcon: ...
    def iconUrl(self) -> PySide2.QtCore.QUrl: ...
    @typing.overload
    def load(self, request:PySide2.QtWebEngineCore.QWebEngineHttpRequest): ...
    @typing.overload
    def load(self, url:PySide2.QtCore.QUrl): ...
    def page(self) -> PySide2.QtWebEngineWidgets.QWebEnginePage: ...
    def pageAction(self, action:PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction) -> PySide2.QtWidgets.QAction: ...
    def reload(self): ...
    def selectedText(self) -> str: ...
    def setContent(self, data:PySide2.QtCore.QByteArray, mimeType:str=..., baseUrl:PySide2.QtCore.QUrl=...): ...
    def setHtml(self, html:str, baseUrl:PySide2.QtCore.QUrl=...): ...
    def setPage(self, page:PySide2.QtWebEngineWidgets.QWebEnginePage): ...
    def setUrl(self, url:PySide2.QtCore.QUrl): ...
    def setZoomFactor(self, factor:float): ...
    def settings(self) -> PySide2.QtWebEngineWidgets.QWebEngineSettings: ...
    def showEvent(self, arg__1:PySide2.QtGui.QShowEvent): ...
    def sizeHint(self) -> PySide2.QtCore.QSize: ...
    def stop(self): ...
    def title(self) -> str: ...
    def triggerPageAction(self, action:PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction, checked:bool=...): ...
    def url(self) -> PySide2.QtCore.QUrl: ...
    def zoomFactor(self) -> float: ...

# eof