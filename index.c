#include <stdio.h>
#include <ctype.h>  // For the toupper function

void displayMenu() {
    printf("============================================\n");
    printf("                  COFFEE MENU               \n");
    printf("============================================\n");
    printf("[I] Ice Coffee\n");
    printf("============================================\n");
}

void displayIceCoffeeMenu() {
    printf("++++++++++++++ ICE COFFEE ++++++++++++++\n");
    printf("1. Espresso       60  Bath\n");
    printf("2. Macchiato      50  Bath\n");
    printf("3. Latte          55  Bath\n");
    printf("============================================\n");
}

int main() {
    char menuChoice;
    int menuSelection = 0;
    int quantity = 0;
    int price = 0;
    int total = 0;

    displayMenu();

    // Prompt user to select a menu category
    printf("Please Select a Menu [I for Ice Coffee] >> ");
    scanf(" %c", &menuChoice);

    // Convert input to uppercase to handle both 'i' and 'I'
    menuChoice = toupper(menuChoice);

    // Check if the user pressed 'I' for Ice Coffee
    if (menuChoice == 'I') {
        displayIceCoffeeMenu();

        // Prompt user to select an item from the Ice Coffee menu
        printf("Please Select ICE Coffee Menu >> ");
        scanf("%d", &menuSelection);

        // Check if the selection is valid
        if (menuSelection < 1 || menuSelection > 3) {
            printf("Please Select Menu Again !!\n");
            return 1;  // Exit the program with an error code
        }

        // Determine price based on menu selection
        switch (menuSelection) {
            case 1:
                price = 60;
                printf("You selected Espresso.\n");
                break;
            case 2:
                price = 50;
                printf("You selected Macchiato.\n");
                break;
            case 3:
                price = 55;
                printf("You selected Latte.\n");
                break;
        }

        // Prompt user for quantity
        printf("Quantity >> ");
        scanf("%d", &quantity);

        // Calculate total
        total = price * quantity;

        // Display the total
        printf("Total >> %d Bath\n", total);

    } else {
        // If the user did not press 'I', show an error message
        printf("กรุณาเลือกเมนู I เพื่อดูเมนู ICE Coffee\n");
    }

    return 0;
}
