#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

int main(void) {
    char line[1024];
    if (!fgets(line, sizeof(line), stdin)) {
        return 0;
    }

    char *comma = strchr(line, ',');
    if (!comma) {
        printf("false\n");
        return 0;
    }

    int count[26] = {0};

    for (char *p = line; p < comma; p++) {
        if (isalpha((unsigned char)*p)) {
            count[tolower((unsigned char)*p) - 'a']++;
        }
    }

    for (char *p = comma + 1; *p != '\0'; p++) {
        if (isalpha((unsigned char)*p)) {
            count[tolower((unsigned char)*p) - 'a']--;
        }
    }

    bool is_anagram = true;
    for (int i = 0; i < 26; i++) {
        if (count[i] != 0) {
            is_anagram = false;
            break;
        }
    }

    printf("%s\n", is_anagram ? "true" : "false");
    return 0;
}
