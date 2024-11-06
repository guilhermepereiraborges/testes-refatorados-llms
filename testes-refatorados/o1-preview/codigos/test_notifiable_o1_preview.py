import pytest
from flunt.notifications.notifiable import Notifiable
from flunt.notifications.notification import Notification

@pytest.fixture
def notifiable():
    return Notifiable()

class TestNotifiable:
    def test_initialization(self, notifiable):
        """Testa a inicialização de um Notifiable."""
        assert notifiable.is_valid
        assert not notifiable.notifications

    def test_add_notification(self, notifiable):
        """Testa a adição de uma única notificação."""
        notification = Notification('key', 'message')
        notifiable.add_notification(notification)
        assert not notifiable.is_valid
        assert len(notifiable.notifications) == 1
        assert notifiable.notifications[0] == notification

    def test_add_notifications(self, notifiable):
        """Testa a adição de múltiplas notificações."""
        notifications = [
            Notification('key1', 'message1'),
            Notification('key2', 'message2')
        ]
        notifiable.add_notifications(notifications)
        assert not notifiable.is_valid
        assert len(notifiable.notifications) == 2
        assert notifiable.notifications == notifications

    def test_get_notifications(self, notifiable):
        """Testa a recuperação das notificações."""
        notifications = [
            Notification('key1', 'message1'),
            Notification('key2', 'message2')
        ]
        notifiable.add_notifications(notifications)
        assert notifiable.get_notifications() == notifications

    def test_clear(self, notifiable):
        """Testa a limpeza das notificações."""
        notifications = [
            Notification('key1', 'message1'),
            Notification('key2', 'message2')
        ]
        notifiable.add_notifications(notifications)
        notifiable.clear()
        assert notifiable.is_valid
        assert not notifiable.notifications

    def test_str_representation(self, notifiable):
        """Testa a representação em string do Notifiable."""
        notifications = [
            Notification('key1', 'message1'),
            Notification('key2', 'message2')
        ]
        notifiable.add_notifications(notifications)
        assert str(notifiable) == str(notifications)
