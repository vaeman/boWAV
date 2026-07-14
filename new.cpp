#include <cstdlib>
#include <ctime>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

vector<int> input() {
    int n;
    cin >> n;
    cin.ignore();

    string nums;
    getline(cin, nums);

    vector<int> numsArr(n - 1);
    int lastwhitespace = 0;
    int c = 0;

    for (int i = 0; i <= (int)nums.size(); i++) {
        if (i == (int)nums.size() || isspace(nums[i])) {
            if (i > lastwhitespace) {
                numsArr[c] = atoi(nums.substr(lastwhitespace, i - lastwhitespace).c_str());
                c += 1;
            }
            lastwhitespace = i + 1;
        }
    }

    return numsArr;
}
vector<int> bubbleSort(vector<int> nums) {
    bool swapped = false;

    int arrSize = nums.size();

    for (int i = 0; i < arrSize - 1; i++) {
        for (int j = 0; j < arrSize - 1; j++) {
            if (nums[j] > nums[j + 1]) {

                int hsh = nums[j];

                nums[j] = nums[j + 1];
                nums[j + 1] = hsh;

                swapped = true;
            } else
                continue;
        }
        if (!swapped) {
            break;
        }
    }
    return nums;
}

// quick sort

vector<int> quickSort(vector<int> nums) {
    bool sorted = false;
    int pivot = nums[nums.size() - 1];

    while (!sorted) {
        int temp;
        int j = -1;

        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i] < pivot) {
                j += 1;
                temp = nums[j];
                nums[j] = nums[i];
                nums[i] = temp;
            }
        }
        temp = nums[j + 1];
        nums[j + 1] = nums[nums.size() - 1];
        nums[nums.size() - 1] = temp;
    }
    return nums;
}

void printArr(vector<int> arr) {
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i];
    }
}

int findMissing(vector<int> nums) {
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] != i + 1) {
            return i + 1;
        }
    }
    return 0;
}

int main() {

    vector<int> nums;
    nums = input();

    // nums = bubbleSort(nums);
    nums = quickSort(nums);
    printArr(nums);
    // cout << findMissing(nums);
    return 0;
}