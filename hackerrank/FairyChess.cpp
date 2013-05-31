#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <unordered_map>
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

int N, M, S;

typedef pair<int, int> Pos;
Pos pos;
vector<vector<unsigned int> > pawns, currentGrid, nextGrid, diag1, diag2;

void clearGrid(vector<vector<unsigned int> > &grid)
{
  auto n = grid.size();
  for (auto i = 0; i < n; i++) {
    for (auto j = 0; j < n; j++) {
      grid[i][j] = 0;
    }
  }
}

void resizeGrid(vector<vector<unsigned int> > &grid, size_t n)
{
  grid.resize(n);
  for (auto i = 0; i < n; i++) {
    grid[i].resize(n);
  }

  clearGrid(grid);
}

void clear()
{
}

void input()
{
  cin >> N >> M >> S;
  resizeGrid(pawns, N);
  resizeGrid(currentGrid, N);
  resizeGrid(nextGrid, N);
  resizeGrid(diag1, N + 2*S + 2);
  resizeGrid(diag2, N + 2*S + 2);
  
  for (auto i = 0; i < N; i++) {
    string line;
    cin >> line;
    
    for (auto j = 0; j < N; j++) {
      if (line[j] == 'L') {
	pos = make_pair(i, j);
      } else if (line[j] == 'P') {
	pawns[i][j] = 1;
      }
    }
  }
}

unsigned int sumDiamond(int i, int j)
{
  unsigned int res = 0;
  
  for (int di = -S; di <= S; di++) {
    if (di + i < 0 || di + i >= N) {
      continue;
    }
    int remainingMax = S - abs(di);
    for (int dj = -remainingMax; dj <= remainingMax; dj++) {
      if (dj + j < 0 || dj + j >= N) {
	continue;
      }
      res += currentGrid[di+i][dj+j];
      res %= MOD;
    }
  }

  return res;
}

inline unsigned int current(int i, int j)
{
  return (i >= 0 && i < N && j >= 0 && j < N) ? currentGrid[i][j] : 0;
}

void prepareDiags() // O(N^2)
{
  clearGrid(diag1);
  clearGrid(diag2);
  
  // diag1 (NW -> SE)
  // diag1[i+S+1][j+S+1] = sum of currentGrid[i][j] ... currentGrid[i+S][j+S]

  // Compute the first line manually (i=-S)
  for (int j = -S-1; j < N+S; j++) { // O(N)
    if (j+S >= 0 && j+S < N) {
      diag1[-S +S+1][j +S+1] = currentGrid[0][j+S];
    }
  }
  
  // The next lines just add to the previous ones
  for (int i = -S+1; i < N; i++) { // O(N)
    for (int j = -S; j < N+S; j++) { // O(N)
      diag1[i +S+1][j +S+1] = diag1[i-1 +S+1][j-1 +S+1]	+ MOD - current(i-1, j-1);
      diag1[i +S+1][j +S+1] %= MOD;
      diag1[i +S+1][j +S+1] += current(i+S, j+S);
      diag1[i +S+1][j +S+1] %= MOD;
    }
  }
  
  // diag2 (SW -> NE)
  // diag2[i+S+1][j+S+1] = sum of currentGrid[i][j] ... currentGrid[i-(S-1)][j+(S-1)]
  for (int i = 0; i < N+S; i++) { // O(N)
    for (int j = -S; j < N+S; j++) { // O(N)
      diag2[i +S+1][j +S+1] = diag2[i-1 +S+1][j+1 +S+1]	+ MOD - current(i-S, j+S);
      diag2[i +S+1][j +S+1] %= MOD;
      diag2[i +S+1][j +S+1] += current(i, j);
      diag2[i +S+1][j +S+1] %= MOD;
    }
  }
}

unsigned int extendRight(unsigned int sum, int i, int j)
{
  // Remove everything on the left
  sum += MOD - diag1[i +S+1][j-S-1 +S+1];
  sum %= MOD;
  sum += MOD - diag2[i-1 +S+1][j-S +S+1];
  sum %= MOD;
  
  // Add everything on the right
  sum += diag2[i+S +S+1][j +S+1];
  sum %= MOD;
  sum += diag1[i-S +S+1][j +S+1];
  sum %= MOD;

  return sum;
}

unsigned int extendBottom(unsigned int sum, int i, int j)
{
  // Remove everything on the top
  sum += MOD - diag1[i-S-1 +S+1][j +S+1];
  sum %= MOD;
  sum += MOD - diag2[i-1 +S+1][j-S +S+1];
  sum %= MOD;
  
  // Add everything on the bottom
  sum += diag1[i +S+1][j-S +S+1];
  sum %= MOD;
  sum += diag2[i+S-1 +S+1][j+1 +S+1];
  sum %= MOD;

  return sum;
}

void solve(unsigned int testId) // O(M * N^2)
{
  currentGrid[pos.first][pos.second] = 1;
  for (auto step = 0; step < M; step++) { // O(M)
    
    prepareDiags(); // O(N^2)

    auto sum = sumDiamond(0, 0); // O(S^2)

    for (auto i = 0; i < N; i++) { // (O(N)
      if (i > 0) {
	sum = extendBottom(sum, i, 0); // O(1)
      }

      auto sumLine = sum;
      for (auto j = 0; j < N; j++) { // (O(N)
	if (j > 0) {
	  sumLine = extendRight(sumLine, i, j); // O(1)
	}
	nextGrid[i][j] = (pawns[i][j]) ? 0 : sumLine;
      }
    }

    currentGrid.swap(nextGrid);
    clearGrid(nextGrid);
  }

  unsigned int res = 0;
  for (auto i = 0; i < N; i++) { // O(N)
    for (auto j = 0; j < N; j++) {
      res += currentGrid[i][j];
      res %= MOD;
    }
  }
  cout << res << endl;
}
