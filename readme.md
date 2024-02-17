# UnitTest Workshop

```
.
├── Dockerfile
├── Makefile
├── app
│   ├── main.py
│   ├── repositories
│   │   └── random.py
│   └── services
│       ├── calculator.py
│       ├── test_calculator.py
│       └── test_calculator_with_libs.py
├── docker-compose.yaml
├── readme.md
└── requirements.txt
```

- require python >= 3.9

## python install package
```
make install
```

## unittest
```
make test
make coverage
```

## ref libraries
- https://docs.python.org/3/library/unittest.mock.html
