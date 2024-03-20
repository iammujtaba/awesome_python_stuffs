import time
from requests import Session
import requests
from requests_futures.sessions import FuturesSession
from concurrent.futures import as_completed
from pprint import pprint
from requests_threads import AsyncSession

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('%r (%r, %r) %2.2f sec' % \
                    (method.__name__, args, kw, te - ts))
        return result

    return timed

@timeit
def future_session(max_request=8):
    session = FuturesSession()
    futures=[session.get(f'http://httpbin.org/get?{i}') for i in range(max_request)]
    return [future.result() for future in as_completed(futures)]

@timeit
def requests_session(max_request=8):
    session = Session()
    return [session.get(f'http://httpbin.org/get?{i}') for i in range(max_request)]


@timeit
def generic_reqeust(max_request):
    return [requests.get(f'http://httpbin.org/get?{i}') for i in range(max_request)]

@timeit
async def aysnc_request(max_request):
    session = AsyncSession(n=max_request)
    rs = []
    for _ in range(100):
        rs.append(await session.get(f'http://httpbin.org/get?{_}'))
    session.run()
    return rs
r2 = generic_reqeust(1)
r0 = requests_session(1)
r1 = future_session(1)

# 1 API Hit
# 'generic_reqeust' ((1,), {}) 0.83 sec
# 'requests_session' ((1,), {}) 0.71 sec
# 'future_session' ((1,), {}) 0.55 sec

# 8 API Hit
# 'generic_reqeust' ((8,), {}) 4.95 sec
# 'requests_session' ((8,), {}) 2.95 sec
# 'future_session' ((8,), {}) 0.70 sec


from requests_threads import AsyncSession

session = AsyncSession(n=8)

async def _main():
    rs = []
    for _ in range(8):
        rs.append(await session.get(f'http://httpbin.org/get?{_}'))
    print(rs)

if __name__ == '__main__':
    session.run(_main)
 