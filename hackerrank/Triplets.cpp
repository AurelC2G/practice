#include <cmath>
#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>
using namespace std;


// Binary indexed tree.
// Lets us compute how many elements <= i were added to the tree
// in logarithmic time.
class BIT
{
public:
  BIT(size_t max)
    : mTree(max) {
  }

  void add(unsigned int i) {
    auto n = mTree.size();
    for (; i < n; i |= i + 1) {
      mTree[i]++;
    }
  }
  
  unsigned int count(unsigned int left, unsigned int right) {
    return count(right) - count(left-1);
  }

private:
  unsigned int count(int ind) {
    unsigned int sum = 0;
    while (ind >= 0) {
      sum += mTree[ind];
      ind &= ind + 1;
      ind--;
    }
    return sum;
  }

  vector<unsigned int> mTree;
};



// Without changing the order, replace the numbers in d by consecutive ones.
// This way, we make sure the biggest is N<=10^5, and can use them as indices.
void renumber(vector<unsigned int> &d) // O(N * log(N))
{
  auto N = d.size();
  map<unsigned int, unsigned int> transform;

  for (auto i = 0; i < N; i++) { // O(N)
    transform[d[i]] = 0; // O(log(N))
  }

  unsigned int num = 0;
  for (auto &it : transform) { // O(N)
    it.second = num;
    num++;
  }

  for (unsigned int i = 0; i < N; i++) { // O(N)
    d[i] = transform[d[i]]; // O(log(N))
  }
}

// if the same number n is present at positions i and j (i<j):
// any triplet beginning by n should use i
// any triplet ending by n should use j
//
// for triplets with n in the middle:
// - if the first is < i, use i
// - else (if the first is > i), use j
unsigned long long int solve(vector<unsigned int> &d)
{
  auto N = d.size();
  if (N < 3) {
    return 0L;
  }

  renumber(d); // O(N * log(N))

  // hasOneLater[i] is true if there is j > i such as d[i] == d[j]
  vector<bool> hasOneLater(N);

  // hasOneLater[i] is true if there is j < i such as d[i] == d[j]
  vector<bool> hasOneEarlier(N);

  // first[d[i]] = i (given a value in d, get its earliest position)
  vector<int> first(N);

  // last[d[i]] = i (given a value in d, get its last position)
  vector<int> last(N);

  for (auto i = 0; i < N; i++) { // O(N)
    first[i] = -1;
  }
  for (auto i = 0; i < N; i++) { // O(N)
    last[d[i]] = i;

    if (first[d[i]] == -1) { // O(log(N))
      first[d[i]] = i;
    } else {
      hasOneEarlier[i] = true;
      hasOneLater[first[d[i]]] = true;
    }
  }


  // smaller[i] = number of j < i such as:
  // * d[j] < d[i]
  // * !hasOneEarlier[j]
  // * !hasOneEarlier[i] or j > first[d[i]]
  vector<unsigned int> smaller(N);
  {
    BIT b(N);
    for (auto i = 0; i < N; i++) { // O(N)
      if (!hasOneEarlier[i]) {
	b.add(d[i]); // O(log(N))
      }
      smaller[i] = b.count(0, d[i]-1);// O(log(N))
      if (hasOneEarlier[i])  {
	smaller[i] -= smaller[first[d[i]]];
      }
    }
  }

  // larger[i] = number of j > i such as:
  // * d[j] > d[i]
  // * !hasOneLater[j]
  vector<unsigned int> larger(N);
  {
    BIT b(N);
    for (int i = N-1; i >= 0; i--) { // O(N)
      if (!hasOneLater[i]) {
	b.add(d[i]); // O(log(N))
      }
      larger[i] = b.count(d[i]+1, N-1); // O(log(N))
    }
  }

  // Number of triplets = SUM_i(larger[i] * smaller[i])
  unsigned long long int res = 0;
  for (auto i = 0; i < N; i++) { // O(N)
    res += smaller[i] * larger[i];
  }
  
  return res;
}

int main() {
    unsigned int N;
    cin >> N;

    vector<unsigned int> d(N);
    for (auto i = 0; i < N; i++) {
        cin >> d[i];
    }

    std::cout << solve(d) << std::endl;

    return 0;
}
