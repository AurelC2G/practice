#include <cmath>
#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>
using namespace std;


// Without changing the order, replace the numbers in d by consecutive ones.
// This way, we make sure the biggest is 10^5, and can use them as indices.
void renumber(vector<unsigned int> &d)
{
  auto N = d.size();
  map<unsigned int, unsigned int> transform;

  for (auto i = 0; i < N; i++) {
    transform[d[i]] = 0;
  }

  unsigned int num = 0;
  for (auto &it : transform) {
    it.second = num;
    num++;
  }

  for (unsigned int i = 0; i < N; i++) {
    d[i] = transform[d[i]];
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

  renumber(d);

  // hasOneLater[i] is true if there is j > i such as d[i] == d[j]
  vector<bool> hasOneLater(N);

  // hasOneLater[i] is true if there is j < i such as d[i] == d[j]
  vector<bool> hasOneEarlier(N);

  // positions[d[i]] = i (given a value in d, get its earliest position)
  vector<int> positions(N);
  for (auto i = 0; i < N; i++) {
    positions[i] = -1;
  }
  for (auto i = 0; i < N; i++) {
    if (positions[d[i]] == -1) {
      positions[d[i]] = i;
    } else {
      hasOneEarlier[i] = true;
      hasOneLater[positions[d[i]]] = true;
    }
  }

  // maxs[i] : max of the i-th block of 100 numbers
  vector<unsigned int> maxs(N/100+1);
  for (unsigned int i = 0; i < N; i++) {
    maxs[i/100] = max(maxs[i/100], d[i]);
  }

  // doublets[i] = number of j such as:
  // * i < j
  // * d[i] < d[j]
  // * !hasOneLater[j] (in this case j will be the third element of the
  //   triplet, so it should only use the latest one)
  vector<unsigned int> doublets(N);
  doublets[N-1] = 0;
  unsigned int i = N-1;
  do {
    i--;

    doublets[i] = 0;

    unsigned int block = i/100;
    if (maxs[block] > d[i]) {
      unsigned int blockEnd = 100 * (block + 1);
      if (blockEnd > N) blockEnd = N;
      for (unsigned int j = i+1; j < blockEnd; j++) {
	if (d[i] < d[j] && !hasOneLater[j]) {
	  doublets[i]++;
	}
      }
    }
    for (block++; block < N/100+1; block++) {
      if (maxs[block] <= d[i]) {
	continue;
      }

      unsigned int blockEnd = 100 * (block + 1);
      if (blockEnd > N) blockEnd = N;
      for (unsigned int j = 100*block; j < blockEnd; j++) {
	if (d[i] < d[j] && !hasOneLater[j]) {
	  doublets[i]++;
	}
      }
    }
  } while (i > 0);


  unsigned long long int total = 0;
  i = N-3;
  do {
    i--;

    if (hasOneEarlier[i]) {
      // we should not start the triplet with i
      continue;
    }

    // let's count the triplets starting with i.
    // We iterate over the second element of the triplet

    unsigned int block = i/100;
    if (maxs[block] > d[i]) {
      unsigned int blockEnd = 100 * (block + 1);
      if (blockEnd > N) blockEnd = N;
      for (unsigned int j = i+1; j < blockEnd; j++) {
	if (d[i] >= d[j]) {
	  continue;
	}

	// if j is not the first, we can only use it if i is > than the first
	if (hasOneEarlier[j] && positions[d[j]] > i) {
	  continue;
	}

	total += doublets[j];
      }
    }
    for (block++; block < N/100+1; block++) {
      if (maxs[block] <= d[i]) {
	continue;
      }

      unsigned int blockEnd = 100 * (block + 1);
      if (blockEnd > N) blockEnd = N;
      for (unsigned int j = 100*block; j < blockEnd; j++) {
	if (d[i] >= d[j]) {
	  continue;
	}

	// if j is not the first, we can only use it if i is > than the first
	if (hasOneEarlier[j] && positions[d[j]] > i) {
	  continue;
	}

	total += doublets[j];
      }
    }
  } while (i > 0);

  return total;
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
