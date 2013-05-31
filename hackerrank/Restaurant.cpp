#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <unordered_map>
#include <cmath>
#include <set>

namespace std {
  template <typename T, typename U>
  struct hash<pair<T,U> > {
    size_t operator()(const pair<T, U> &x) const {
      return hash<T>()(x.first) ^ hash<U>()(x.second);
    }
  };
}

using namespace std;

void clear();
void input();
void solve(unsigned int testId);

int main()
{
  unsigned int T;
  cin >> T;

  for (auto t = 0; t < T; t++) {
    clear();
    input();
    solve(t);
  }

  return 0;
}


#define MOD 1000000007

int l, b;

void clear()
{
}

void input()
{
  cin >> l >> b;
}

void solve(unsigned int testId)
{
  // r, q integers such as:
  // l = c*r
  // b = c*q

  // We know that c = 1 works (r = l; q = b). Can we find better?

  unsigned int best = l*b;
  for (unsigned int r = l; r >= 1; r--) {
    double c = (double)l/(double)r;
    double q = b/c;
    if (floor(q) == q) {
      best = r*q;
    }
  }

  cout << best << endl;
}
