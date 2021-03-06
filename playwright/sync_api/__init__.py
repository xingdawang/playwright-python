# Copyright (c) Microsoft Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Python package `playwright` is a Python library to automate Chromium,
Firefox and WebKit with a single API. Playwright is built to enable cross-browser
web automation that is ever-green, capable, reliable and fast.
"""

import playwright._impl._api_structures
import playwright._impl._api_types
import playwright.sync_api._generated
from playwright.sync_api._context_manager import PlaywrightContextManager
from playwright.sync_api._generated import (
    Accessibility,
    BindingCall,
    Browser,
    BrowserContext,
    BrowserType,
    CDPSession,
    ChromiumBrowserContext,
    ConsoleMessage,
    Dialog,
    Download,
    ElementHandle,
    FileChooser,
    Frame,
    JSHandle,
    Keyboard,
    Mouse,
    Page,
    Playwright,
    Request,
    Response,
    Route,
    Selectors,
    Touchscreen,
    Video,
    WebSocket,
    Worker,
)

Cookie = playwright._impl._api_structures.Cookie
ResourceTiming = playwright._impl._api_structures.ResourceTiming
StorageState = playwright._impl._api_structures.StorageState

DeviceDescriptor = playwright._impl._api_types.DeviceDescriptor
Error = playwright._impl._api_types.Error
FilePayload = playwright._impl._api_types.FilePayload
FloatRect = playwright._impl._api_types.FloatRect
Geolocation = playwright._impl._api_types.Geolocation
PdfMargins = playwright._impl._api_types.PdfMargins
ProxySettings = playwright._impl._api_types.ProxySettings
SourceLocation = playwright._impl._api_types.SourceLocation
TimeoutError = playwright._impl._api_types.TimeoutError


def sync_playwright() -> PlaywrightContextManager:
    return PlaywrightContextManager()


__all__ = [
    "sync_playwright",
    "Accessibility",
    "BindingCall",
    "Browser",
    "BrowserContext",
    "BrowserType",
    "CDPSession",
    "ChromiumBrowserContext",
    "ConsoleMessage",
    "Cookie",
    "DeviceDescriptor",
    "Dialog",
    "Download",
    "ElementHandle",
    "Error",
    "FileChooser",
    "FilePayload",
    "FloatRect",
    "Frame",
    "Geolocation",
    "JSHandle",
    "Keyboard",
    "Mouse",
    "Page",
    "PdfMargins",
    "Playwright",
    "ProxySettings",
    "Request",
    "ResourceTiming",
    "Response",
    "Route",
    "Selectors",
    "SourceLocation",
    "StorageState",
    "sync_playwright",
    "TimeoutError",
    "Touchscreen",
    "Video",
    "WebSocket",
    "Worker",
]
