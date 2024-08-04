import unittest


def stair(steps):
  finstr = ""
  if steps == 0:
    return "___"
  if steps == 1:
    return "  _\n_|"
  for x in range(steps, -1, -1):
    if x == steps:
      finstr += " " * (x * 2) + "_" + "\n"
    elif x == 0:
      finstr += "_|"
    else:
      finstr += " " * (x * 2) + "_|" + "\n"
  return finstr


class TestS3AWK(unittest.TestCase):
        
    def test_sample(Test):
        Test.assertEqual(stair(0), "___", "Zero must return 3 underscores")
        Test.assertEqual(stair(1), '  _\n_|')
        Test.assertEqual(stair(2), '    _\n  _|\n_|')
        Test.assertEqual(stair(3), '      _\n    _|\n  _|\n_|')
        Test.assertEqual(stair(5), '          _\n        _|\n      _|\n    _|\n  _|\n_|')
        Test.assertEqual(stair(10), '                    _\n                  _|\n                _|\n              _|\n            _|\n          _|\n        _|\n      _|\n    _|\n  _|\n_|')
        Test.assertEqual(stair(50), '                                                                                                    _\n                                                                                                  _|\n                                                                                                _|\n                                                                                              _|\n                                                                                            _|\n                                                                                          _|\n                                                                                        _|\n                                                                                      _|\n                                                                                    _|\n                                                                                  _|\n                                                                                _|\n                                                                              _|\n                                                                            _|\n                                                                          _|\n                                                                        _|\n                                                                      _|\n                                                                    _|\n                                                                  _|\n                                                                _|\n                                                              _|\n                                                            _|\n                                                          _|\n                                                        _|\n                                                      _|\n                                                    _|\n                                                  _|\n                                                _|\n                                              _|\n                                            _|\n                                          _|\n                                        _|\n                                      _|\n                                    _|\n                                  _|\n                                _|\n                              _|\n                            _|\n                          _|\n                        _|\n                      _|\n                    _|\n                  _|\n                _|\n              _|\n            _|\n          _|\n        _|\n      _|\n    _|\n  _|\n_|')


if __name__ == '__main__':
   unittest.main()
