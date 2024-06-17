
// Rat in a maze
class RatInMaze {
    public static ArrayList<String> ans;
    public static ArrayList<String> findPath(int[][] m, int n) {
    ans = new ArrayList<>();
    if(m[0][0] == 0) return ans;
    boolean visited[][] = new boolean[n][n];
    visited[0][0] = true;
    ratMaze(m, visited, 0, 0, "");
    return ans;
    }
    
    public static void ratMaze(int maze[][], boolean visited[][], int r, int c, String psf) {
        if(r == maze.length - 1 && c == maze[0].length - 1) {
            ans.add(psf);
            return;
        }
        
        // top cell
        if(isSafe(maze, visited, r-1, c)) {
            visited[r-1][c] = true;
            ratMaze(maze, visited, r-1, c, psf + "U");
            visited[r-1][c] = false;
        }
        
        // right cell
        if(isSafe(maze, visited, r, c + 1)) {
            visited[r][c+1] = true;
            ratMaze(maze, visited, r, c + 1, psf + "R");
           visited[r][c+1] = false;
        }
        
        // down cell
        if(isSafe(maze, visited, r+1, c)) {
            visited[r+1][c] = true;
            ratMaze(maze, visited, r+1, c, psf + "D");
            visited[r+1][c] = false;
        }
        
        // Left cell
        if(isSafe(maze, visited, r, c - 1)) {
            visited[r][c-1] = true;
            ratMaze(maze, visited, r, c-1, psf + "L");
            visited[r][c-1] = false;
        }
       
    }
    
    public static boolean isSafe(int maze[][], boolean visited[][], int r, int c) {
        if(c < 0 || c >= maze.length || r < 0 || r>= maze.length || maze[r][c] == 0 || visited[r][c]) return false;
        return true;
    }
}


// Palindromic partition
class PalindromicPartition {
    List<List<String>> ans;

    public List<List<String>> partition(String s) {
       ans = new ArrayList<>();
       helper(s, new ArrayList<>());
       return ans;
    }


    public void helper(String s, ArrayList<String> myCurrentPartions) {
        if(s.length() == 0) {
            ans.add(new ArrayList<>(myCurrentPartions));
            return;
        }  
       for(int i = 1; i <= s.length(); i++) {
           String prefix = s.substring(0, i); 
           if(isPalindrome(prefix)){
               String remaining = s.substring(i);
               myCurrentPartions.add(prefix);
               helper(remaining, myCurrentPartions);
               myCurrentPartions.removeLast();
           }
       }
    }

    public boolean isPalindrome(String s) {
       int l = 0, r = s.length() - 1;
       while(l < r){
           if(s.charAt(l) != s.charAt(r)) return false;
           l++;
           r--;
       }
       return true;
    }


}


// Sudoku solver
class SudokuSolver{
    public void solveSudoku(char[][] board) {
        helper(board, 0, 0);
    }

    public boolean helper(char board[][], int row, int col) {
        if(col == board[0].length) {
            row++;
            col = 0;   
        }
        if(row == board.length) return true;

        if(board[row][col] == '.') {
            for(char num = '1'; num <= '9'; num++) {
                if(isValid(board, row, col, num)) {
                    board[row][col] = num;
                    if(helper(board, row, col + 1)) return true;
                    board[row][col] = '.';
                }
            }
            return false;
        } 
        return helper(board, row, col+1);
    }

    public boolean isValid(char board[][], int row, int col, char num) {
        // verify row
        for(int c = 0; c < 9; c++) 
            if(board[row][c] == num) return false;

        // verify column
        for(int r = 0; r < 9; r++) 
            if(board[r][col] == num) return false;

        // check the grid
        int startRow = (row/3) * 3;
        int startCol = (col/3) * 3;
        for(int i = 0; i < 3; i++) {
            for(int j = 0; j < 3; j++) {
                if(board[startRow + i][startCol + j] == num) return false;
            }
        }
        return true;     
    }
}