def test_sentinel_import_package() -> None:
    import sentinel
    assert sentinel.__name__ == "sentinel"

# Purposeful bad case proves that it works as intended

# def test_sentinel_import_package_two() -> None:
    # import sentinel_bad
    # assert sentinel.__name__ == "sentinel"

    