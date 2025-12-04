import pytest
# Assuming the Message class is in a file named 'message.py'
from message import Message

messages_1 = Message("A.Tutor@grandwich.ac.uk", "Hello", "B.Tutor@grandwich.ac.uk", "How is the course going?", 2)
messages_2 = Message("B.Tutor@grandwich.ac.uk", "Re: Hello", "A.Tutor@grandwich.ac.uk",
                      "> How is the course going?\n\nBrilliant, thanks. The students are all fantastic and are going to get top marks in their coursework.",
                      5)
messages_3 = Message("B.Tutor@grandwich.ac.uk", "Re: Hello", "A.Tutor@grandwich.ac.uk",
                      "> How is the course going?\n\nBrilliant, thanks. The students are all fantastic and are going to get top marks in their coursework.",
                      6)
def test_message_info():
    """Test the info method of the Message class.
    {self.stars():8} {self.sender:25} {self.label:5} {self.subject}
    """
    assert messages_1.info() == "**       A.Tutor@grandwich.ac.uk         Hello"
    #assert messages_2.info() == "**

def test_message_stars():
    """Test the stars method of the Message class."""
    assert messages_1.stars() == "**"
    assert messages_2.stars() == "*****"
    assert messages_3.stars() == "*****"
