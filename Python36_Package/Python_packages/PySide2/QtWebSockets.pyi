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
PySide2.QtWebSockets, except for defaults which are replaced by "...".
"""

# Module PySide2.QtWebSockets
import PySide2
from PySide2.support.signature import typing
from PySide2.support.signature.mapping import (
    Virtual, Missing, Invalid, Default, Instance)

class Object(object): pass

import shiboken2 as Shiboken
Shiboken.Object = Object

import PySide2.QtCore
import PySide2.QtNetwork
import PySide2.QtWebSockets


class QMaskGenerator(PySide2.QtCore.QObject):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def nextMask(self) -> int: ...
    def seed(self) -> bool: ...


class QWebSocket(PySide2.QtCore.QObject):

    def __init__(self, origin:str=..., version:PySide2.QtWebSockets.QWebSocketProtocol.Version=..., parent:PySide2.QtCore.QObject=...): ...
    def abort(self): ...
    def bytesToWrite(self) -> int: ...
    def close(self, closeCode:PySide2.QtWebSockets.QWebSocketProtocol.CloseCode=..., reason:str=...): ...
    def closeCode(self) -> PySide2.QtWebSockets.QWebSocketProtocol.CloseCode: ...
    def closeReason(self) -> str: ...
    def error(self) -> PySide2.QtNetwork.QAbstractSocket.SocketError: ...
    def errorString(self) -> str: ...
    def flush(self) -> bool: ...
    def isValid(self) -> bool: ...
    def localAddress(self) -> PySide2.QtNetwork.QHostAddress: ...
    def localPort(self) -> int: ...
    def maskGenerator(self) -> PySide2.QtWebSockets.QMaskGenerator: ...
    @typing.overload
    def open(self, request:PySide2.QtNetwork.QNetworkRequest): ...
    @typing.overload
    def open(self, url:PySide2.QtCore.QUrl): ...
    def origin(self) -> str: ...
    def pauseMode(self) -> PySide2.QtNetwork.QAbstractSocket.PauseModes: ...
    def peerAddress(self) -> PySide2.QtNetwork.QHostAddress: ...
    def peerName(self) -> str: ...
    def peerPort(self) -> int: ...
    def ping(self, payload:PySide2.QtCore.QByteArray=...): ...
    def proxy(self) -> PySide2.QtNetwork.QNetworkProxy: ...
    def readBufferSize(self) -> int: ...
    def request(self) -> PySide2.QtNetwork.QNetworkRequest: ...
    def requestUrl(self) -> PySide2.QtCore.QUrl: ...
    def resourceName(self) -> str: ...
    def resume(self): ...
    def sendBinaryMessage(self, data:PySide2.QtCore.QByteArray) -> int: ...
    def sendTextMessage(self, message:str) -> int: ...
    def setMaskGenerator(self, maskGenerator:PySide2.QtWebSockets.QMaskGenerator): ...
    def setPauseMode(self, pauseMode:PySide2.QtNetwork.QAbstractSocket.PauseModes): ...
    def setProxy(self, networkProxy:PySide2.QtNetwork.QNetworkProxy): ...
    def setReadBufferSize(self, size:int): ...
    def state(self) -> PySide2.QtNetwork.QAbstractSocket.SocketState: ...
    def version(self) -> PySide2.QtWebSockets.QWebSocketProtocol.Version: ...


class QWebSocketCorsAuthenticator(Shiboken.Object):

    @typing.overload
    def __init__(self, origin:str): ...
    @typing.overload
    def __init__(self, other:PySide2.QtWebSockets.QWebSocketCorsAuthenticator): ...
    def allowed(self) -> bool: ...
    def origin(self) -> str: ...
    def setAllowed(self, allowed:bool): ...
    def swap(self, other:PySide2.QtWebSockets.QWebSocketCorsAuthenticator): ...


class QWebSocketProtocol: ...


class QWebSocketServer(PySide2.QtCore.QObject):

    def __init__(self, serverName:str, secureMode:PySide2.QtWebSockets.QWebSocketServer.SslMode, parent:PySide2.QtCore.QObject=...): ...
    def close(self): ...
    def error(self) -> PySide2.QtWebSockets.QWebSocketProtocol.CloseCode: ...
    def errorString(self) -> str: ...
    def handleConnection(self, socket:PySide2.QtNetwork.QTcpSocket): ...
    def hasPendingConnections(self) -> bool: ...
    def isListening(self) -> bool: ...
    def listen(self, address:PySide2.QtNetwork.QHostAddress=..., port:int=...) -> bool: ...
    def maxPendingConnections(self) -> int: ...
    def nativeDescriptor(self) -> int: ...
    def nextPendingConnection(self) -> PySide2.QtWebSockets.QWebSocket: ...
    def pauseAccepting(self): ...
    def proxy(self) -> PySide2.QtNetwork.QNetworkProxy: ...
    def resumeAccepting(self): ...
    def secureMode(self) -> PySide2.QtWebSockets.QWebSocketServer.SslMode: ...
    def serverAddress(self) -> PySide2.QtNetwork.QHostAddress: ...
    def serverName(self) -> str: ...
    def serverPort(self) -> int: ...
    def serverUrl(self) -> PySide2.QtCore.QUrl: ...
    def setMaxPendingConnections(self, numConnections:int): ...
    def setNativeDescriptor(self, descriptor:int) -> bool: ...
    def setProxy(self, networkProxy:PySide2.QtNetwork.QNetworkProxy): ...
    def setServerName(self, serverName:str): ...
    def setSocketDescriptor(self, socketDescriptor:int) -> bool: ...
    def socketDescriptor(self) -> int: ...
    def supportedVersions(self) -> typing.List: ...

# eof
