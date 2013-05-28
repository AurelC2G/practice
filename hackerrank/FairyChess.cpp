#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <unordered_map>

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

int N, M, S;

typedef pair<int, int> Pos;
Pos pos;
vector<vector<bool> > pawns;
vector<vector<unsigned int> > currentGrid, nextGrid;

void clearGrid(vector<vector<unsigned int> > &grid)
{
  for (auto i = 0; i < N; i++) {
    for (auto j = 0; j < N; j++) {
      grid[i][j] = 0;
    }
  }
}

void clear()
{
  pawns.clear();
  clearGrid(currentGrid);
  clearGrid(nextGrid);
}

void input()
{
  cin >> N >> M >> S;
  pawns.resize(N);
  currentGrid.resize(N);
  nextGrid.resize(N);
  
  for (auto i = 0; i < N; i++) {
    string line;
    cin >> line;
    pawns[i].resize(N);
    currentGrid[i].resize(N);
    nextGrid[i].resize(N);
    
    for (auto j = 0; j < N; j++) {
      if (line[j] == 'L') {
	pos = make_pair(i, j);
      } else if (line[j] == 'P') {
	pawns[i][j] = true;
      }
    }
  }
}

void solve(unsigned int testId)
{
  currentGrid[pos.first][pos.second] = 1;
  for (auto step = 0; step < M; step++) {
    
    for (auto i = 0; i < N; i++) {
      for (auto j = 0; j < N; j++) {
	if (currentGrid[i][j] == 0) {
	  continue;
	}
	
	for (int di = -S; di <= S; di++) {
	  if (di + i < 0 || di + i >= N) {
	    continue;
	  }
	  int remainingMax = S - abs(di);
	  for (int dj = -remainingMax; dj <= remainingMax; dj++) {
	    if (dj + j < 0 || dj + j >= N) {
	      continue;
	    }
	    if (pawns[di+i][dj+j]) {
	      continue;
	    }
	    
	    nextGrid[i+di][j+dj] += currentGrid[i][j];
	    nextGrid[i+di][j+dj] %= MOD;
	  }
	}
      }
    }

    currentGrid.swap(nextGrid);
    clearGrid(nextGrid);
  }
  
  unsigned int res = 0;
  for (auto i = 0; i < N; i++) {
    for (auto j = 0; j < N; j++) {
      res += currentGrid[i][j];
      res %= MOD;
    }
  }
  cout << res << endl;
}
