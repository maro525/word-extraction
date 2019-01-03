

#include <iostream>
#include <mecab.h>

int main(int argc, char **argv){
  char input[1024] = "太郎は次郎が持っている本を花子に渡した。";

  MeCab::Tagger *tagger = MeCab::createTagger("");
  const char *result = tagger->parse(input);

  std::cout << "INPUT: " << input << std::endl;
  std::cout << "RESULT: " << result << std::endl;

  return 0;
}
