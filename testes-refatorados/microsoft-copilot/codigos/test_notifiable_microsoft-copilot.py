import pytest
from flunt.notifications.notifiable import Notifiable
from flunt.notifications.notification import Notification

@pytest.fixture
def notifiable():
    return Notifiable()

@pytest.fixture
def notifications():
    return [Notification('key1', 'message1'), Notification('key2', 'message2')]

def test_notifiable_initialization(notifiable):
    assert notifiable.is_valid
    assert not notifiable.notifications

def test_notifiable_add_notification(notifiable):
    notification = Notification('key', 'message')
    notifiable.add_notification(notification)
    assert not notifiable.is_valid
    assert len(notifiable.notifications) == 1
    assert notifiable.notifications[0] == notification

def test_notifiable_add_notifications(notifiable, notifications):
    notifiable.add_notifications(notifications)
    assert not notifiable.is_valid
    assert len(notifiable.notifications) == 2
    assert notifiable.notifications == notifications

def test_notifiable_get_notifications(notifiable, notifications):
    notifiable.add_notifications(notifications)
    assert notifiable.get_notifications() == notifications

def test_notifiable_clear(notifiable, notifications):
    notifiable.add_notifications(notifications)
    notifiable.clear()
    assert notifiable.is_valid
    assert not notifiable.notifications

def test_notifiable_str(notifiable, notifications):
    notifiable.add_notifications(notifications)
    assert str(notifiable) == str(notifications)
