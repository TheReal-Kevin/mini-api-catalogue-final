import unittest
from operations import addition, maximum, format_nom


class TestOperations(unittest.TestCase):
    """Tests unitaires pour les fonctions du module operations."""

    def test_addition(self):
        """Test de la fonction addition."""
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(0, 0), 0)
        self.assertEqual(addition(10.5, 2.3), 12.8)

    def test_maximum(self):
        """Test de la fonction maximum."""
        self.assertEqual(maximum(1, 2, 3), 3)
        self.assertEqual(maximum(5), 5)
        self.assertEqual(maximum(-1, -5, -2), -1)
        self.assertEqual(maximum(3.5, 2.1, 4.0), 4.0)

        # Test avec erreur
        with self.assertRaises(ValueError):
            maximum()

    def test_format_nom(self):
        """Test de la fonction format_nom."""
        self.assertEqual(format_nom("jean", "dupont"), "Jean DUPONT")
        self.assertEqual(format_nom("MARIE", "martin"), "Marie MARTIN")
        self.assertEqual(format_nom("pierre", "durand"), "Pierre DURAND")
        self.assertEqual(format_nom("élodie", "lévesque"), "Élodie LÉVESQUE")


if __name__ == '__main__':
    unittest.main()
