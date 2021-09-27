from time import sleep
from ChromeAuto import ChromeAuto

chrome = ChromeAuto()

def nextEpisode(current):
    next_episode = current + 1
    while (next_episode in fillers):
        next_episode += 1

    return next_episode

audio = 'legendado'
anime = 'detective-conan'
current = 631
count = 10
fillers = [634, 635, 636, 637, 638, 639, 640, 641, 658, 663, 664, 665, 666, 669, 670, 677, 678, 679, 680, 686, 687, 688, 689, 692, 693, 694, 695, 696, 697, 698, 707, 708, 709, 716, 717, 718, 719, 720, 721, 726, 729, 730, 733, 735, 736, 737, 742, 743, 750, 753, 757, 758, 761, 762, 767, 768, 769, 774, 775, 776, 777, 778, 784, 789, 790, 791, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 813, 816, 817, 818, 819, 820, 821, 824, 825, 826, 829, 833, 834, 835, 838, 839, 840, 841, 842, 845, 846, 851, 852, 855, 856, 857, 858, 859, 860, 865, 868, 869, 870, 871, 875, 876, 877, 880, 883, 884, 891, 892, 893, 898, 899, 900, 903, 904, 905, 906, 907, 908, 911, 912, 913, 914, 915, 918, 921, 922, 923, 924, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 943, 944, 945, 946, 947, 948, 949, 950, 951, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 975, 976, 977, 978, 979, 980, 981, 982, 985, 986, 987, 988, 989, 990, 991, 992, 996, 997, 998, 999, 1002, 1006, 1007, 1008, 1009, 1010, 1013, 1014, 1015, 1016, 1017];

for i in range(0, count):
    if len(str(current)) == 1:
        current = '0' + str(current)

    chrome.access(f'https://betteranime.net/anime/{audio}/{anime}/episodio-{current}/download')
    chrome.click_by_text('Qualidade HD')
    chrome.click_by_xpath('/html/body/div/header/div/div/button')
    chrome.back_page(0)
    chrome.click_by_xpath('/html/body/div/header/div/div/a')
    sleep(80)

    current = nextEpisode(current)