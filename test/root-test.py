RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RESET='\033[0m'

def good(msg):
    return f"{GREEN}{msg}{RESET}"

def bad(msg):
    return f"{RED}{msg}{RESET}"

def info(msg):
    return f"{BLUE}{msg}{RESET}"

def testEqual(msg, x, y, results):
    (nfails, ntests) = results
    if(x == y):
        print(f"  {msg} ... {good('PASS')}")
        return (nfails, ntests + 1)
    else:
        print(f"  {msg} ... {bad('FAIL')}")
        return (nfails + 1, ntests + 1)

def testTrue(msg, x, results):
    (nfails, ntests) = results
    if x:
        print(f"  {msg} ... {good('PASS')}")
        return (nfails, ntests + 1)
    else:
        print(f"  {msg} ... {bad('FAIL')}")
        return (nfails + 1, ntests + 1)

def testEqualMaybe(msg, x, y, results):
    (nfails, ntests) = results
    if x is not None and x == y:
        print(f"  {msg} ... {good('PASS')}")
        return (nfails, ntests + 1)
    else:
        print(f"  {msg} ... {bad('FAIL')}")
        return (nfails + 1, ntests + 1)

def testIsNothing(msg, x, results):
    (nfails, ntests) = results
    if x is None:
        print(f"  {msg} ... {good('PASS')}")
        return (nfails, ntests + 1)
    else:
        print(f"  {msg} ... {bad('FAIL')}")
        return (nfails + 1, ntests + 1)

def printMsg(msg, x):
    print(info(msg))
    return x

def printResult(x):
    if(x[0] == 0):
        print(good(f"All {x[1]!s} tests pass"))
    else:
        print(bad(f"{x[0]!s}/{x[1]!s} tests failed"))
    return x
