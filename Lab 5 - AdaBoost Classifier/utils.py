
""" HELPER FUNCTION: GET ACCURACY ========================================="""
def get_accuracy(pred, Y):
    return sum(pred == Y) / float(len(Y))

""" HELPER FUNCTION: PRINT ACCURACY ========================================="""
def print_accuracy(acc_train, acc_test):
    print(f'Accuracy: Training: {acc_train * 100}% - Test: {acc_test * 100}%')
   
""" HELPER FUNCTION: GET ERROR RATE ========================================="""
def get_error_rate(pred, Y):
    return sum(pred != Y) / float(len(Y))           # percentage of misclassifications

""" HELPER FUNCTION: PLOT FUNCTION ========================================="""
def plot_accuracy(acc_train, acc_test):
    import pandas as pd
    import matplotlib.pyplot as plt
    df_error = pd.DataFrame([acc_train, acc_test]).T
    df_error.columns = ['Training', 'Test']
    plot1 = df_error.plot(linewidth=3, figsize=(8, 6),
                          color=['lightblue', 'darkblue'], grid=True)
    plot1.set_xlabel('Number of iterations', fontsize=12)
    plot1.set_xticklabels(range(0, 450, 50))
    plot1.set_ylabel('Accuracy', fontsize=12)
    plot1.set_title('Accuracy vs number of iterations', fontsize=16)
    plt.axhline(y=acc_test[0], linewidth=1, color='red', ls='dashed')
    plt.show()
    
    



