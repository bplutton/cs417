"""
Lab 9: Tombstone Tests — YOU WRITE THESE.

Each test function has a description of what to test.
Your job is to write the implementation. Use the tests in
test_hash_table.py as examples for how to write assertions.

Run your tests:
    pytest -v -k "TestTombstones"
"""

from hash_table_open import HashTableOpen


class TestTombstones:
    """Tests that tombstones keep the hash table working correctly."""

    def test_probe_chain_survives_deletion(self):
        """
        Insert three keys that collide (use a small table, like size=3).
        Delete the MIDDLE one.
        Verify that you can still find the LAST one.

        This is the core tombstone test — if delete uses None instead
        of a tombstone, this test will fail because the probe chain breaks.
        """
        ht = HashTableOpen(size=3)
        ht.put("x", 10)
        ht.put("Greece", 20)
        ht.put("y", 30)
        ht.delete("Greece")
        assert "Greece" not in ht

    def test_tombstone_slot_reused_on_insert(self):
        """
        Insert a key, then delete it (creating a tombstone).
        Insert a NEW key that would land on that same slot.
        Verify the new key is stored and the count is correct.

        This tests that put() treats tombstones as open slots
        for new insertions.
        """
        ht = HashTableOpen(size=3)
        ht.put(1, 10)
        ht.delete(1)
        ht.put(2, 20)
        assert 1 not in ht

    def test_count_correct_through_delete_and_reinsert(self):
        """
        Start with a table, insert 3 keys (count should be 3).
        Delete one (count should be 2).
        Reinsert a key with the same name (count should be 3).
        Delete two keys (count should be 1).

        Verify len() is correct after every step.
        """
        ht = HashTableOpen(size=3)
        ht.put(1, 10)
        ht.put(2, 20)
        ht.put(3, 30)
        assert len(ht) == 3
        ht.delete(2)
        assert len(ht) == 2
        ht.put(2, 200)
        assert len(ht) == 3
        ht.delete(1)
        ht.delete(3)
        assert len(ht) == 1