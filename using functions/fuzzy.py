# ==========================================
# 🧠 Fuzzy Set Operations (All Major Operations)
# ==========================================
# Define fuzzy sets as Python dictionaries
A = {'x1': 0.2, 'x2': 0.5, 'x3': 0.7, 'x4': 1.0}
B = {'x1': 0.6, 'x2': 0.3, 'x3': 0.9, 'x4': 0.4}
print("Fuzzy Set A:", A)
print("Fuzzy Set B:", B)
# ---------------------------
# 1️ ⃣ Fuzzy Union (A ∪ B)
# ---------------------------
union = {x: max(A[x], B[x]) for x in A}
print("\nUnion (A ∪ B):", union)
# ---------------------------
# 2️ ⃣ Fuzzy Intersection (A ∩ B)
# ---------------------------
intersection = {x: min(A[x], B[x]) for x in A}
print("\nIntersection (A ∩ B):", intersection)
# ---------------------------
# 3️ ⃣ Fuzzy Complement (A′, B′)
# ---------------------------
complement_A = {x: round(1 - A[x], 2) for x in A}
complement_B = {x: round(1 - B[x], 2) for x in B}
print("\nComplement of A (A′):", complement_A)
print("Complement of B (B′):", complement_B)
# ---------------------------
# 4️ ⃣ Fuzzy Difference (A - B)
# ---------------------------
difference = {x: round(min(A[x], 1 - B[x]), 2) for x in A}
print("\nDifference (A - B):", difference)
# ---------------------------
# 5️ ⃣ Algebraic Sum (A + B)
# ---------------------------
algebraic_sum = {x: round(A[x] + B[x] - (A[x] * B[x]), 2) for x in A}
print("\nAlgebraic Sum (A + B):", algebraic_sum)
# ---------------------------
# 6️ ⃣ Algebraic Product (A ⋅ B)
# ---------------------------
algebraic_product = {x: round(A[x] * B[x], 2) for x in A}
print("\nAlgebraic Product (A ⋅ B):", algebraic_product)
# ---------------------------
# 7️ ⃣ Bounded Sum
# ---------------------------
bounded_sum = {x: round(min(1, A[x] + B[x]), 2) for x in A}
print("\nBounded Sum:", bounded_sum)
# ---------------------------
# 8️ ⃣ Bounded Difference
# ---------------------------
bounded_diff = {x: round(max(0, A[x] + B[x] - 1), 2) for x in A}
print("\nBounded Difference:", bounded_diff)
# ==========================================
# 📊 Visualization of all operations
# ==========================================
import matplotlib.pyplot as plt
elements = list(A.keys())
# Convert dictionary values to lists
A_values = list(A.values())
B_values = list(B.values())
U_values = list(union.values())
I_values = list(intersection.values())
C_A_values = list(complement_A.values())
C_B_values = list(complement_B.values())
D_values = list(difference.values())
AS_values = list(algebraic_sum.values())
AP_values = list(algebraic_product.values())
BS_values = list(bounded_sum.values())
BD_values = list(bounded_diff.values())
# Plot multiple operations
plt.figure(figsize=(10,6))
plt.plot(elements, A_values, 'bo-', label='Set A')
plt.plot(elements, B_values, 'ro-', label='Set B')
plt.plot(elements, U_values, 'g--', label='Union (A ∪ B)')
plt.plot(elements, I_values, 'm--', label='Intersection (A ∩ B)')
plt.plot(elements, D_values, 'c--', label='Difference (A - B)')
plt.plot(elements, AS_values, 'y--', label='Algebraic Sum')
plt.plot(elements, AP_values, 'k--', label='Algebraic Product')
plt.plot(elements, BS_values, 'b:', label='Bounded Sum')
plt.plot(elements, BD_values, 'r:', label='Bounded Difference')
plt.title("Fuzzy Set Operations Visualization", fontsize=13)
plt.xlabel("Elements")
plt.ylabel("Membership Value")
plt.legend()
plt.grid(True)
plt.show()