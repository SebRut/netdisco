"""Discover devices that implement the Qbo platform."""
from . import MDNSDiscoverable


class Discoverable(MDNSDiscoverable):
    """Add support for discovering Qbo platform devices."""

    def __init__(self, nd):
        """Initialize the Qbo discovery."""
        super(Discoverable, self).__init__(nd, '_qbo._tcp.local.')
