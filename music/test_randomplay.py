import pytest
from unittest import mock 
from randomplay import random_clip

def test_random_clip():
    ''' Test random_clip() with a mock cursor.
    ''' 
    cur = mock.MagicMock()
    # Call the function being tested, and check return value
    name, data = random_clip(cur)
    # Was execute() called?
    cur.execute.assert_called()
    # Was  fetchone() called?
    cur.fetchone.assert_called()
