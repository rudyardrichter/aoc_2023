pub fn binary_search<P, S, T>(step: &S, pred: &P, lo: T, hi: T) -> (T, T)
where
    S: Fn(&T, &T) -> Option<T>,
    P: Fn(&T) -> bool,
{
    let mut lo = lo;
    let mut hi = hi;
    while let Some(mid) = step(&lo, &hi) {
        if pred(&mid) {
            hi = mid;
        } else {
            lo = mid;
        }
    }
    (lo, hi)
}
