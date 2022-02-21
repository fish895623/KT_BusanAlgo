def solution(cacheSize, cities):
    cache_cityes = []
    time_count = 0
    if cacheSize ==0:
        return len(cities) * 5
    while cities:
        ct = cities.pop(0).lower()
        
        if len(cache_cityes) ==0:
            cache_cityes.append(ct)
            time_count += 5
        else:
            if ct in cache_cityes:
                time_count +=1
                find_idx = cache_cityes.index(ct)
                cache_cityes.pop(find_idx)
                cache_cityes.append(ct)
            else:
                if len(cache_cityes) < cacheSize:
                    cache_cityes.append(ct)
                else:
                    cache_cityes.pop(0)
                    cache_cityes.append(ct)
                time_count += 5
    return time_count