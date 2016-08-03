from birdy import *
import unittest


class TestBirdy(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.birdStuff = Birdy()

    def test_user_creation(self):
        user = User("Chase Ramsey", "Rammer")
        self.assertEqual("Chase Ramsey", user.full_name)
        self.assertEqual("Rammer", user.screen_name)
        self.assertIsNotNone(user.user_id)
        self.assertIsInstance(user, User)

    def test_new_public_chirp_creation(self):
        source = User("Chase Ramsey", "Rammer")
        chirp = Chirp(
            message = "Russell is the coolest.",
            user = source.user_id,
            private = False
            )
        self.assertEqual(chirp.message, "Russell is the coolest.")
        self.assertEqual(chirp.user_id, source.user_id)
        self.assertEqual(chirp.private, False)
        self.assertIsInstance(chirp, Chirp)
        self.assertIsNotNone(chirp.chirp_id)

    def test_reply_public_chirp_creation(self):
        source = User("Keith Allen Bradley", "HardKnox")
        reply_target = Chirp(
            message = "Russell is the coolest.",
            chirpUUID = chirp.chirp_id,
            private = False,
            conversation = chirp.convo_id
            )
        chirp = Chirp(
            message = "You know that's right",
            user = source.user_id,
            private = False,
            conversation = reply_target.convo_id
            )
        self.assertEqual(chirp.message, "You know that's right!")
        self.assertEqual(reply_target.chirpUUID, chirp.chirp_id)
        self.assertEqual(reply_target.private, False)
        self.assertEqual(chirp.private, False)
        self.assertEqual(reply_target.conversation, chirp.convo_id)
        self.assertIsInstance(chirp, Chirp)

    def test_new_private_chirp_creation(self):
        source = User("Chase Ramsey", "Rammer")
        target = User("Keith Allen Bradley", "HardKnox")
        chirp = Chirp(
            message = "Russell is the coolest.",
            user = source.user_id,
            private = True,
            receiver = target.user_id
            )
        self.assertEqual(chirp.message, "Russell is the coolest.")
        self.assertEqual(chirp.user_id, source.user_id)
        self.assertEqual(chirp.private, True)
        self.assertIsInstance(chirp, Chirp)
        self.assertIsNotNone(chirp.chirp_id)


if __name__ == '__main__':
    unittest.main()
