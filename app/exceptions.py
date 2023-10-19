class DuplicateEntity(Exception):
    """storage에 같은 id의 데이터를 중복 저장 할 수 없다."""


class NotFoundEntity(Exception):
    """storage에서 entity을 찾을 수 없다."""
