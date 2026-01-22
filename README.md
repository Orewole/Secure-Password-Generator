# 🔐 PyGen-Secure
> A robust, randomized password generation tool for CLI environments.

**Version:** 1.0.0  
**Author:** [Your Name]  
**License:** MIT

## 📖 Project Overview
**PyGen-Secure** is a utility designed to improve digital security by automating the creation of strong, high-entropy passwords. It eliminates the human bias involved in password creation by leveraging pseudo-random number generation.

---

## ⚙️ Software Development Life Cycle (SDLC) Report

### Phase 1: Requirements Engineering
The system was built to address the need for quick, complex credential generation.
**Functional Requirements:**
1.  **Customizable Length:** The user must specify the length of the password (minimum 6 characters).
2.  **Complexity Toggle:** The user must have the option to include or exclude special characters (symbols).
3.  **Entropy:** The system must ensure characters are selected randomly without predictable patterns.
4.  **Clipboard Ready:** The output must be displayed clearly for copying.

### Phase 2: System Architecture & Design
The architecture is procedural, utilizing Python's standard libraries.

**Component Design:**
*   **`build_character_pool(include_symbols)`**: A helper function responsible for concatenating ASCII letters, digits, and punctuation based on user input.
*   **`generate_secure_token`**: The core logic engine that samples the pool to create the final string.
*   **`runtime_interface`**: The user interaction loop that handles input validation (ensuring length is an integer).

**Data Flow:**
Input (Length/Yes-No) → `build_character_pool` → `generate_secure_token` → Output (String).

### Phase 3: Implementation Details
The solution implements the design using Python 3.
*   **Libraries:** utilized `string` for character constants and `random` for non-deterministic selection.
*   **Error Handling:** Implemented a `while` loop in the `runtime_interface` to catch `ValueError` if non-integer lengths are entered.
*   **Logic:** A specific check ensures the password length is not negative or zero.

### Phase 4: Quality Assurance (Testing)
**Test Log:**
*   *Test 1 (Length Boundary):* Entered length `4`.
    *   *Outcome:* System generated a 4-character password successfully.
*   *Test 2 (Symbol Exclusion):* Selected `n` for symbols.
    *   *Outcome:* Resulting password contained only alphanumeric characters (A-Z, 0-9).
*   *Test 3 (Invalid Input):* Entered "Strong" when asked for length.
    *   *Outcome:* System caught the exception and printed "Please enter a valid number."

### Phase 5: Deployment
The tool is packaged as a portable script (`pygen_secure.py`). It requires Python 3.6+ and has no external dependencies.

---

## 💻 Installation & Usage

1.  Download `pygen_secure.py`.
2.  Run the script in your terminal:
    ```bash
    python pygen_secure.py
    ```
3.  Follow the prompts to generate your secure token.
