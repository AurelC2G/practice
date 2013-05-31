#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <unordered_map>
#include <cmath>
#include <set>
#include <algorithm>

using namespace std;

void input();
unsigned int solve(unsigned int testId);

int main()
{
  unsigned int T;
  cin >> T;

  for (auto t = 0; t < T; t++) {
    input();
    cout << solve(t) << endl;
  }

  return 0;
}

int N;
vector<unsigned int> v;

void input()
{
  cin >> N;
  v.resize(N);

  for (auto i = 0; i < N; i++) {
    cin >> v[i];
  }
}

unsigned int solve(unsigned int testId)
{
  if (N == 0) {
    return 0;
  }

  const vector<unsigned int> factors = {5, 2, 1};
  auto minV = *min_element(v.begin(), v.end());

  unsigned int bestRes = 1000000000;
  for (int delta = 0; delta < 5; delta++) {
    int target = minV - delta;
    
    unsigned int res = 0;
    for (auto i = 0; i < N; i++) {
      int diff = v[i] - target;
      
      for (auto f : factors) {
	auto n = diff / f;
	res += n;
	diff -= n*f;
      }
    }
    
    bestRes = min(bestRes, res);
  }


  return bestRes;
}
