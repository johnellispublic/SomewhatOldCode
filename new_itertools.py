import operator


def count(start=0, step=1):
    while True:
        yield start
        start += step


def cycle(it):
    while True:
        for item in it:
            yield item


def repeat(item, n=-1):
    while n != 0:
        yield item
        n -= 1


def accumulate(it, func=operator.add):
    total = None
    for i in it:
        if total is None:
            total = i
        else:
            yield total
            total = func(total, i)


def _chain__from_iterable(iterators):
    for it in iterators:
        for i in it:
            yield i


def chain(*iterators):
    for it in iterators:
        for i in it:
            yield i


chain.from_iterable = _chain__from_iterable


def compress(data, selectors):
    for d, s in zip(data, selectors):
        if s:
            yield d


def dropwhile(pred, seq):
    started = False
    for item in seq:
        if pred(item):
            started = True
        if started:
            yield item


def filterfalse(pred, seq):
    for item in seq:
        if not pred(item):
            yield item


def groupby(iterable, key=lambda x: x):
    group = []
    for item in iterable:
        if not group or group[0] == key(item):
            group.append(item)
        else:
            yield (group[0], group)
            group = [item]

    yield (group[0], group)


def islice(it, start=0, stop=float("inf"), step=1):
    i = 0
    for item in it:
        if start < i < stop and (i - start) % step == 0:
            yield item


def pairwise(it):
    prev = None
    for item in it:
        if prev is None:
            prev = item
        else:
            yield (prev, item)
            prev = item


def starmap(func, seq):
    for item in seq:
        yield func(*item)


def takewhile(pred, seq):
    for item in seq:
        if not pred(item):
            break
        else:
            yield item

def tee(iter, n=2):
    pass
