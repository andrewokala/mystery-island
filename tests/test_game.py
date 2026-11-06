import unittest

from game import new_game, move_player, collect_item

class TestNewGame(unittest.TestCase):

    def test_new_game_starts_at_beach(self):
        player = new_game("Andrew")

        self.assertEqual(player["location"], "Beach")

    def test_new_game_starts_with_five_energy(self):
        player = new_game("Andrew")

        self.assertEqual(player["energy"], 5)

    def test_new_game_starts_with_empty_inventory(self):
        player = new_game("Andew")

        self.assertEqual(player["inventory"], [])

class TestPlayerMovement(unittest.TestCase):
    
    def test_player_can_move_to_valid_location(self):
        player = new_game("Andrew")

        success, message = move_player(player, "Jungle")

        self.assertTrue(success)
        self.assertEqual(player["location"], "Jungle")
        self.assertEqual(player["energy"],  4)

    def test_player_cannot_move_to_invalid_location(self):
        player = new_game("Andrew")

        success, message = move_player(player, "Lighthouse")

        self.assertFalse(success)
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)

    def test_player_cannot_cross_bridge_without_rope(self):
        player = new_game("Andrew")

        player["location"] = "Old Bridge"

        success, message = move_player(player, "Lighthouse")

        self.assertFalse(success)
        self.assertEqual(player["location"], "Old Bridge")
        self.assertEqual(player["energy"], 5)

class TestInventory(unittest.TestCase):

    def test_player_can_collect_lantern(self):
        player = new_game("Andrew")
        player["location"] = "Jungle"

        success, message = collect_item(player, "Lantern")

        self.assertTrue(success)
        self.assertIn("Lantern", player["inventory"])

    def test_player_can_collect_rope(self):
        player = new_game("Andrew")
        player["location"] = "Cave"

        success, message = collect_item(player, "Rope")

        self.assertTrue(success)
        self.assertIn("Rope", player["inventory"])

    def test_player_cannot_collect_same_item_twice(self):
        player = new_game("Andrew")
        player["location"] = "Jungle"

        first_success, first_message = collect_item(player, "Lantern")
        second_success, second_message = collect_item(player, "Lantern")

        self.assertTrue(first_success)
        self.assertFalse(second_success)
        self.assertEqual(player["inventory"], ["Lantern"])

    def test_player_cannot_collect_item_from_wrong_location(self):
        player = new_game("Andrew")
        
        success, message = collect_item(player, "Lantern")

        self.assertFalse(success)
        self.assertEqual(player["inventory"], [])



if __name__ == "__main__":
    unittest.main()