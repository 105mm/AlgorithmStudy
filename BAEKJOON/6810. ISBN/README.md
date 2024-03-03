6810번
제출
맞힌 사람
숏코딩
재채점 결과
채점 현황
내 제출
질문 게시판
ISBN 다국어
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	3769	2558	2378	67.982%
문제
The International Standard Book Number (ISBN) is a 13-digit code for identifying books. These numbers have a special property for detecting whether the number was written correctly.

The 1-3-sum of a 13-digit number is calculated by multiplying the digits alternately by 1’s and 3’s (see example) and then adding the results. For example, to compute the 1-3-sum of the number 9780921418948 we add

9 ∗ 1 + 7 ∗ 3 + 8 ∗ 1 + 0 ∗ 3 + 9 ∗ 1 + 2 ∗ 3 + 1 ∗ 1 + 4 ∗ 3 + 1 ∗ 1 + 8 ∗ 3 + 9 ∗ 1 + 4 ∗ 3 + 8 ∗ 1

to get 120.

The special property of an ISBN number is that its 1-3-sum is always a multiple of 10.

Write a program to compute the 1-3-sum of a 13-digit number. To reduce the amount of typing, you may assume that the first ten digits will always be 9780921418, like the example above. Your program should input the last three digits and then print its 1-3-sum. Use a format similar to the samples below.

예제 입력 1 
9
4
8
예제 출력 1 
The 1-3-sum is 120