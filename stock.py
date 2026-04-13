import streamlit as st  # import Streamlit library

st.title("Stock Calculation")  # set app title
st.info('Here You Can Easily Calculate Prices of Buying And Selling Stock Freely')  # display info message
com_price = 5  # commission price

def stock_price():  # function to get stock price input
    stk_price = st.number_input('Enter The Stock Current Price',value=1)  # input for stock price with default value 1
    return stk_price  # return stock price value

stk_price = stock_price()  # call function and store stock price
if stk_price <= 0:  # check if stock price is invalid
    st.error('Invalid stock price')  # display error message

def abudget():  # function to get budget input
    budget = (st.number_input('Enter Your Budget',value=1) - com_price)  # input budget and subtract commission
    return budget  # return adjusted budget

new_budget = abudget()  # call function and store new budget
if new_budget <= 0:  # check if budget is invalid
    st.error('Invalid budget')  # display error message

st.info(f'Your Budget After Commission: {new_budget}')  # show budget after commission
st.header('Profit of:')  # display section header

first = st.button('-5-20')  # button for profit range -5 to 20
scnd = st.button('21-60')  # button for profit range 21 to 60
thrd = st.button('60+')  # button for profit range 60+

if first:  # if first button is clicked
    stk_amount = int(new_budget / stk_price)  # calculate number of stocks
    min_sell_price = float(new_budget / stk_amount)  # calculate minimum selling price
    max_sell_price = float((new_budget + 25) / stk_amount)  # calculate maximum selling price
    st.success(f'Recommendation: Buy {stk_amount} Stocks, And Sell At Price Of At Least: {min_sell_price:.2f}, Or Maximum Price Of: {max_sell_price:.2f}')  # display recommendation

if scnd:  # if second button is clicked
    stk_amount = int(new_budget / stk_price)  # calculate number of stocks
    min_sell_price = float((new_budget + 26) / stk_amount)  # calculate minimum selling price
    max_sell_price = float((new_budget + 65) / stk_amount)  # calculate maximum selling price
    st.success(f'Recommendation: Buy {stk_amount} Stocks, And Sell At Price Of At Least : {min_sell_price:.2f}, Or Maximum Price Of: {max_sell_price:.2f}')  # display recommendation

if thrd:  # if third button is clicked
    stk_amount = int(new_budget / stk_price)  # calculate number of stocks
    max_sell_price = float((new_budget + 66) / stk_amount)  # calculate maximum selling price
    st.success(f'Recommendation: Buy {stk_amount} Stocks, And Sell It At At Least: {max_sell_price:.2f}')  # display recommendation

st.header('Actual Price (price at sell):')  # display section header for actual sell price
final_price = st.number_input('Enter Price Of Stock At Sell:',value=1)  # input for final selling price

if True:  # always execute this block
    stk_amount = int(new_budget / stk_price)  # calculate number of stocks again
    prof = final_price * stk_amount  # calculate total return from selling
    if prof > (new_budget+5):  # check if profit is greater than budget + commission
        st.success(f'Your Profit is:{prof-new_budget}')  # display profit
    if prof < (new_budget+5):  # check if result is less than budget + commission
        st.error(f'Your Loss is:{prof-new_budget}')  # display loss