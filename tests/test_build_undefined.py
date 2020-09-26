from python_utility.build_undefined import Build


def test_build_undefined() -> None:
    assert Build.GIT_TAG != ''
    assert Build.GIT_HASH != ''
    assert Build.BUILD_DATE != ''
