"""
Tests for depricated methods.
"""
from nose.tools import assert_true, assert_false
from six import PY2


if PY2:
    def test_has_key():
        """
        The now-depricated has_keys method
        """
        from attrdict.dictionary import AttrDict

        mapping = AttrDict(
            {'foo': 'bar', frozenset((1, 2, 3)): 'abc', 1: 2}
        )
        empty = AttrDict()

        assert_true('foo' in mapping)
        assert_false('foo' in empty)

        assert_true(frozenset((1, 2, 3)) in mapping)
        assert_false(frozenset((1, 2, 3)) in empty)

        assert_true(1 in mapping)
        assert_false(1 in empty)

        assert_false('banana' in mapping)
        assert_false('banana' in empty)
