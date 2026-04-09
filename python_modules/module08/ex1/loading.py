#!/usr/bin/env python3

def checker() -> bool:
    dependencies: int = 0
    print("Checking dependencies:")
    try:
        import pandas as p
        print(f"[OK] {p.__name__} ({p.__version__}) - "
              f"Data manipulation ready")
        dependencies += 1
    except ImportError:
        print("[NOK] Missing dependencie: pandas")

    try:
        import numpy as n
        print(f"[OK] {n.__name__} ({n.__version__}) - "
              f"Numerical computation ready")
        dependencies += 1
    except ImportError:
        print("[NOK] Missing dependencie: numpy")

    try:
        import matplotlib as m
        print(f"[OK] {m.__name__} ({m.__version__}) - Visualization ready")
        dependencies += 1
    except ImportError:
        print("[NOK] Missing dependencie: matplotlib")

    if dependencies != 3:
        return False
    return True


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    if checker():
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        print("\nAnalyzing Matrix data...")
        matrix = sorted(np.random.rand(1000))
        df = pd.DataFrame(matrix, columns=["values"])
        print(f"Processing {len(df)} data points...")
        print("Generating visualization...")
        plt.plot(df["values"])
        plt.savefig("matrix_analysis.png")
        plt.close()
        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")
    else:
        print("\nInstall the required dependencies first.")


if __name__ == "__main__":
    main()
