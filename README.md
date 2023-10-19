# Simple Pytest

## src

```
app
├── lib.py         # storage와 entity의 interface 정의
├── entity.py      # storage에 저장할 robot entity 정의
├── storage.py     # entity을 저장할 memory storage 정의
├── exceptions.py  # exception 정의
└── utils.py       # utility 함수 정의
```

## tests

```
tests
├── ch01  # unittest을 사용한 테스트
├── ch02  # pytest로 migration
├── ch03  # refactor: 테스트를 모듈별로 분리하고 conftest.py을 이용해 fixture 관리
└── ch04  # refactor: pytest.mark.parametrize을 사용해 다양한 케이스 테스트
```

## run

```shell
make test_ch01
```

```shell
make test_ch02
```

```shell
make test_ch03
```

```shell
make test_ch04
```

```shell
make test_all
```
