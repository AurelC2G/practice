#include <iostream>
#include <map>

using namespace std;

struct State {
  State() : full(true), canSomeoneWin(true), winner('.') {}

  void next(char c)
  {
    if (c == '.') {
      full = false;
      canSomeoneWin = false;
      return;
    }

    if (c == 'T') {
      return;
    }

    if (!canSomeoneWin) {
      return;
    }
    
    if (winner == '.') {
      winner = c;
    } else if (winner != c) {
      canSomeoneWin = false;
    }
  }

  bool full;
  bool canSomeoneWin;
  char winner;
};

int main(int argc, char* argv[])
{
  unsigned T;
  cin >> T;

  char B[4][4];

  for (auto t = 1; t <= T; t++) {

    cout << "Case #" << t << ": ";

    for (auto i = 0; i < 4; i++) {
      for (auto j = 0; j < 4; j++) {
	cin >> B[i][j];
      }
    }
    
    map<char, bool> win;
    win['O'] = false;
    win['X'] = false;
    bool isFull = true;

    // Lines
    for (auto i = 0; i < 4; i++) {
      State s;
      for (auto j = 0; j < 4; j++) {
	s.next(B[i][j]);
      }
      if (!s.full) isFull = false;
      if (s.canSomeoneWin) win[s.winner] = true;
    }

    // Col
    for (auto i = 0; i < 4; i++) {
      State s;
      for (auto j = 0; j < 4; j++) {
	s.next(B[j][i]);
      }
      if (!s.full) isFull = false;
      if (s.canSomeoneWin) win[s.winner] = true;
    }

    // Diag1
    {
      State s;
      for (auto i = 0; i < 4; i++) {
	s.next(B[i][i]);
      }
      if (!s.full) isFull = false;
      if (s.canSomeoneWin) win[s.winner] = true;
    }

    // Diag2
    {
      State s;
      for (auto i = 0; i < 4; i++) {
	s.next(B[i][3-i]);
      }
      if (!s.full) isFull = false;
      if (s.canSomeoneWin) win[s.winner] = true;
    }
    
    if (win['O'] && win['X']) {
      cout << "Draw" << endl;
    } else if (win['O']) {
      cout << "O won" << endl;
    } else if (win['X']) {
      cout << "X won" << endl;
    } else if (isFull) {
      cout << "Draw" << endl;
    } else {
      cout << "Game has not completed" << endl;
    }
  }

  return 0;
}
