#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
  unsigned T;
  cin >> T;

  for (auto t = 1; t <= T; t++) {
    unsigned N, M;
    cin >> N >> M;
    
    vector<vector<unsigned> > B(N);
    for (auto i = 0; i < N; i++) {
      B[i].resize(M);
      for (auto j = 0; j < M; j++) {
	cin >> B[i][j];
      }
    }
    
    vector<unsigned> maxForLine(N);
    for (auto i = 0; i < N; i++) {
      maxForLine[i] = 0;
      for (auto j = 0; j < M; j++) {
	if (B[i][j] > maxForLine[i]) {
	  maxForLine[i] = B[i][j];
	}
      }
    }
    
    vector<unsigned> maxForCol(M);
    for (auto j = 0; j < M; j++) {
      maxForCol[j] = 0;
      for (auto i = 0; i < N; i++) {
	if (B[i][j] > maxForCol[j]) {
	  maxForCol[j] = B[i][j];
	}
      }
    }
    
    bool result = true;
    for (auto i = 0; i < N; i++) {
      if (!result) break;
      
      for (auto j = 0; j < M; j++) {
	if (B[i][j] < maxForLine[i] && B[i][j] < maxForCol[j]) {
	  result = false;
	  break;
	}
      }
    }
    

    cout << "Case #" << t << ": " << ((result) ? "YES" : "NO") << endl;
  }

  return 0;
}
