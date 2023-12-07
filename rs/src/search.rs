use num;
use std::ops;

pub fn search<P, S, T>(step: &S, pred: &P, lo: T, hi: T) -> (T, T)
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

pub fn binary<T>(lo: &T, hi: &T) -> Option<T>
where
    T: Copy
        + Ord
        + num::One
        + num::FromPrimitive
        + ops::Add<Output = T>
        + ops::Sub<Output = T>
        + ops::Div<Output = T>,
{
    let two = num::FromPrimitive::from_u8(2).unwrap();
    (*hi - num::one() > *lo).then(|| (*lo + *hi).div(two))
}
