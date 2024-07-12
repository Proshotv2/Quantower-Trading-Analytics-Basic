import sqlite3
import pandas as pd
from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def LoadTrades(conn):
    trades = "SELECT * FROM USER_TRADES"
    df = pd.read_sql_query(trades, conn)
    return df

def perform_analysis(df):
    # Calculate total trades
    total_trades = len(df)

    # Calculate gross and net PnL
    total_gross_pnl = df['gross_pnl_value'].sum()
    total_net_pnl = df['net_pnl_value'].sum()

    # Calculate win/loss ratio
    wins = df[df['gross_pnl_value'] > 0]
    losses = df[df['gross_pnl_value'] <= 0]
    win_loss_ratio = len(wins) / len(losses) if len(losses) > 0 else float('inf')

    # Calculate average trade duration (assuming 'time' is in milliseconds)
    df['trade_duration'] = df['time'].diff().fillna(0)
    avg_trade_duration = df['trade_duration'].mean()

    # Create equity curve
    df['equity_curve'] = df['gross_pnl_value'].cumsum()

    # Return calculated metrics
    return {
        'total_trades': total_trades,
        'total_gross_pnl': total_gross_pnl,
        'total_net_pnl': total_net_pnl,
        'win_loss_ratio': win_loss_ratio,
        'avg_trade_duration': avg_trade_duration,
        'equity_curve': df['equity_curve']
    }

def plot_equity_curve(equity_curve):
    plt.figure(figsize=(10, 6))
    plt.plot(equity_curve)
    plt.title('Equity Curve')
    plt.xlabel('Trade Number')
    plt.ylabel('Cumulative PnL')
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return plot_url

@app.route('/')
def index():
    conn = sqlite3.connect('C:\\Program Files\\Quantower\\UserTradesCache\\Apex (Rithmic-Rithmic-Custom-VmrAtMbSRkq2CiB48TGHg)\\user-trades.db')
    df = LoadTrades(conn)
    conn.close()

    # Perform analysis
    analysis = perform_analysis(df)

    # Generate plots
    equity_curve_plot = plot_equity_curve(analysis['equity_curve'])

    # Pass the data to the template
    return render_template('index.html', analysis=analysis, equity_curve_plot=equity_curve_plot)

if __name__ == '__main__':
    app.run(debug=True)
