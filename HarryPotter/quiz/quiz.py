from xml.dom import HierarchyRequestErr


class Solution:
  
  def commandLineInput(self):
    print('Enter your name:')
    x = input()

    if 'MaoMao' == x:
      print('Ni hao, ' + x)
    elif 'Maggie' == x:
      print('Hello, ' + x)
    elif 'Voldmort' == x:
     print ('Hello, Lord Baldy. ' + x)
    else:
      print('Hello, stranger ' + x)

  def main(self) -> bool:
    self.commandLineInput();
if __name__ == '__main__':
  solution = Solution()
  solution.main()
