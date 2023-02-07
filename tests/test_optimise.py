import brownie
import decimal
import pytest


# def test_optimise(
#     user,
#     ve_crv,
#     voter_proxy,
#     usdn_pool,
#     usdn_pool_gauge,
#     mim_pool_gauge,
#     usdn_lp_token,
#     usdn_reward_pool,
#     gauge_controller,
#     mim_pool,
#     chain,
#     crv,
#     usdd_pool_gauge,
#     tusd_pool_gauge,
#     busd_pool_gauge,
#     frax_pool_gauge,
#     mim_reward_pool,
#     steth_pool_gauge,
#     steth_reward_pool,
# ):
#     mintable_crv_a_day = crv.mintable_in_timeframe(chain.time(), chain.time() + 86400)
#     print("Crv daily emissions", mintable_crv_a_day)
 
#     adjusted_supply_cvx_mim = mim_pool_gauge.working_balances(voter_proxy)
#     adjusted_total_supply_mim = mim_pool_gauge.working_supply()
#     adjusted_ratio_mim = adjusted_supply_cvx_mim / adjusted_total_supply_mim

#     adjusted_supply_steth = steth_pool_gauge.working_balances(voter_proxy)
#     adjusted_total_supply_steth = steth_pool_gauge.working_supply()
#     adjusted_ratio_steth = adjusted_supply_steth / adjusted_total_supply_steth
#     print('Adjusted ratio for cvx mim before our deposit', adjusted_ratio_mim)
#     print('Adjusted ratio for cvx steth before our deposit', adjusted_ratio_steth)


#     mim_gauge_relative_weight = gauge_controller.gauge_relative_weight(mim_pool_gauge) / 1e16
#     mim_gauge_relative_weight_percent = mim_gauge_relative_weight / 100

#     steth_gauge_relative_weight = gauge_controller.gauge_relative_weight(steth_pool_gauge) / 1e16
#     steth_gauge_relative_weight_percent = steth_gauge_relative_weight / 100

#     usdd_gauge_relative_weight = gauge_controller.gauge_relative_weight(usdd_pool_gauge) / 1e16
#     tusd_pool_gauge_relative_weight = gauge_controller.gauge_relative_weight(tusd_pool_gauge) / 1e16
#     busd_pool_gauge_relative_weight = gauge_controller.gauge_relative_weight(busd_pool_gauge) / 1e16
#     frax_pool_gauge_relative_weight = gauge_controller.gauge_relative_weight(frax_pool_gauge) / 1e16

#     daily_crv_cvx_getting = adjusted_ratio_mim * mintable_crv_a_day * mim_gauge_relative_weight_percent
#     print("Daily crv cvx-mim rewards contract gets before our deposit", convert_to_string(daily_crv_cvx_getting))

#     print('Mim gauge relative weight', mim_gauge_relative_weight)
#     print('USDD gauge relative weight', usdd_gauge_relative_weight) 
#     print('TUSD gauge relative weight', tusd_pool_gauge_relative_weight) 
#     print('BUSD gauge relative weight', busd_pool_gauge_relative_weight) 
#     print('FRAX gauge relative weight', frax_pool_gauge_relative_weight)
#     print('Steth gauge relative weight', steth_gauge_relative_weight)
#     print("Chain time", chain.time())


#     # adjusted supply effect given x deposit = 0.4x + (cvx_ve / total_ve) * (3 / 5) * (lp_supply of gauge + x)
#     # 0.4x + (c+x)0.3 = 0.7x + 0.3c, where c is lp_supply of the gauge
#     # (total_lp_supply * cvx_ve) / (3/5 * total_ve)
#     cvx_ve = ve_crv.balanceOf(voter_proxy)
#     total_ve = ve_crv.totalSupply()    

#     ## mim
#     total_lp_supply_mim_pool = mim_pool_gauge.totalSupply()
#     cvx_lp_supply_mim_pool = mim_pool_gauge.balanceOf(voter_proxy)
#     new_adjusted_cvx, new_adjusted_total = after_deposit_yield(1000 * 1e18, cvx_lp_supply_mim_pool, total_lp_supply_mim_pool, total_ve, cvx_ve, mim_pool_gauge, voter_proxy)
#     new_adjusted_ratio = new_adjusted_cvx / new_adjusted_total
#     new_crv_emissions_daily = mintable_crv_a_day * new_adjusted_ratio * mim_gauge_relative_weight_percent
#     print("Daily crv cvx-mim rewards gets after our deposit", convert_to_string(new_crv_emissions_daily))

#     total_supply_before_rewards_contract = mim_reward_pool.totalSupply()
#     total_supply_after_rewards_contract = total_supply_before_rewards_contract + 1000 * 1e18

#     our_ratio = (1000 * 1e18) / total_supply_after_rewards_contract
#     our_portion_of_daily_crv_rewards = our_ratio * new_crv_emissions_daily
#     print("If we would deposit -amount- LP tokens we would get daily this much CRV", convert_to_string(our_portion_of_daily_crv_rewards))

#     ## steth
#     total_lp_supply_steth_pool = steth_pool_gauge.totalSupply()
#     cvx_lp_supply_steth_pool = steth_pool_gauge.balanceOf(voter_proxy)
#     new_adjusted_steth, new_adjusted_total_steth = after_deposit_yield(100 * 1e18, cvx_lp_supply_steth_pool, total_lp_supply_steth_pool, total_ve, cvx_ve, steth_pool_gauge, voter_proxy)
#     new_adjusted_ratio_steth = new_adjusted_steth / new_adjusted_total_steth
#     new_crv_emissions_daily_steth = mintable_crv_a_day * new_adjusted_ratio_steth * steth_gauge_relative_weight_percent
#     print("Daily crv steth rewards gets after our deposit", convert_to_string(new_crv_emissions_daily_steth))

#     total_supply_before_rewards_contract_steth = steth_reward_pool.totalSupply()
#     total_supply_after_rewards_contract_steth = total_supply_before_rewards_contract_steth + 100 * 1e18

#     our_ratio_steth = (100 * 1e18) / total_supply_after_rewards_contract_steth
#     our_portion_of_daily_crv_rewards_steth = our_ratio_steth * new_crv_emissions_daily_steth
#     print("If we would deposit -amount- LP tokens Steth we would get daily this much CRV", convert_to_string(our_portion_of_daily_crv_rewards_steth))


#     k = cvx_ve / total_ve
#     print('K', k)
#     mim_lp_supply = mim_pool_gauge.totalSupply() / 1e18
#     mim_lp_supply = mim_lp_supply * k
#     print('Adjusted lp supply of mim', mim_lp_supply)


def test_balancer(
    ve_bal,
    bal_gauge_controller,
    bal_steth_gauge,
    aura_reward_pool_steth,
    aura_voter_proxy,
    chain,
    web3,
    aura_token,
):
    weekly_bal_emissions = 145000 * 1e18
    print("Bal daily emissions", weekly_bal_emissions)
 
    adjusted_supply = bal_steth_gauge.working_balances(aura_voter_proxy)
    adjusted_total_supply = bal_steth_gauge.working_supply()
    adjusted_ratio = adjusted_supply / adjusted_total_supply
    print('Adjusted ratio for aura voter proxy before our deposit', adjusted_ratio)

    bal_steth_gauge_relative_weight = bal_gauge_controller.gauge_relative_weight(bal_steth_gauge) / 1e16
    bal_steth_gauge_relative_weight_percent = bal_steth_gauge_relative_weight / 100
    print('Steth gauge relative weight percent', bal_steth_gauge_relative_weight_percent)

    yearly_bal_rewards = adjusted_ratio * weekly_bal_emissions * 52 * bal_steth_gauge_relative_weight_percent
    print("Yearly bal rewards aura contract gets before our deposit", convert_to_string(yearly_bal_rewards))

    # (total_lp_supply * aura_ve) / (3/5 * total_ve)
    aura_ve = ve_bal.balanceOf(aura_voter_proxy)
    total_ve = ve_bal.totalSupply()    

    total_lp_supply_gauge = bal_steth_gauge.totalSupply()
    lp_supply_gauge = bal_steth_gauge.balanceOf(aura_voter_proxy)

    SUPPLY_AMOUNT = 10 * 1e18

    new_adjusted_supply, new_adjusted_total_supply = after_deposit_yield(SUPPLY_AMOUNT, lp_supply_gauge, total_lp_supply_gauge, total_ve, aura_ve, bal_steth_gauge, aura_voter_proxy)
    new_adjusted_ratio = new_adjusted_supply / new_adjusted_total_supply
    new_yearly_bal_emissions = weekly_bal_emissions * new_adjusted_ratio * 52 * bal_steth_gauge_relative_weight_percent
    print("Yearly bal rewards aura contract gets after our deposit", convert_to_string(new_yearly_bal_emissions))

    total_supply_before_rewards_contract = aura_reward_pool_steth.totalSupply()
    total_supply_after_rewards_contract = total_supply_before_rewards_contract + (SUPPLY_AMOUNT)

    our_ratio = (SUPPLY_AMOUNT) / total_supply_after_rewards_contract
    our_portion_of_yearly_bal_emissions = our_ratio * new_yearly_bal_emissions
    print("If we would deposit -amount- LP tokens we would get daily this much BAL", convert_to_string(our_portion_of_yearly_bal_emissions))
    
    actual_bal_amount_receivable = our_portion_of_yearly_bal_emissions * 1/4
    print("Actual amount of BAL we can receive after fees deducted", convert_to_string(actual_bal_amount_receivable))

    REDUCTION_PER_CLIFF = 100000000000000000000000
    TOTAL_CLIFFS = 500
    EMISSIONS_MAX_SUPPLY = 50000000000000000000000000
    aura_token_supply = aura_token.totalSupply()
    aura_token_initial_minted = aura_token.INIT_MINT_AMOUNT()

    aura_token_emissions_minted = aura_token_supply - aura_token_initial_minted
    cliff = aura_token_emissions_minted / REDUCTION_PER_CLIFF

    if cliff < TOTAL_CLIFFS:
        reduction = ((TOTAL_CLIFFS - cliff) * 5/2) + 700
        aura_to_mint = (actual_bal_amount_receivable * reduction) / TOTAL_CLIFFS
        amount_till_max = EMISSIONS_MAX_SUPPLY - aura_token_emissions_minted

        if aura_to_mint > amount_till_max:
            aura_to_mint = amount_till_max
    
    print("Aura token rewards we can receive after a year", convert_to_string(aura_to_mint))


    

def convert_to_string(number):
    number = decimal.Decimal(number) # Creating Decimal Instance from Number(12.1231e-09)
    digit = abs(number.as_tuple().exponent) # Getting the precision count // If 0.123123 -> output will be 6
    number_str = f"{float(number):.{digit}f}" # returning with specific precision
    number_str = number_str.replace('.', '')
    return number_str

def after_deposit_yield(amount_supplied, supply_before, total_supply_before, total_ve, cvx_ve, mim_pool_gauge, voter_proxy):
    supply_after = amount_supplied + supply_before
    total_supply_after = amount_supplied + total_supply_before

    lim = (total_supply_after * cvx_ve) / (3/5 * total_ve)
    lim += 2/5 * supply_after
    print("lim", convert_to_string(lim))

    if lim > supply_after:
        lim = supply_after
    
    print("Real supplied", convert_to_string(lim))
    
    old_working_balance = mim_pool_gauge.working_balances(voter_proxy)
    old_total_working_balance = mim_pool_gauge.working_supply()

    print("Old working bal", convert_to_string(old_working_balance))
    print("Old total working bal", convert_to_string(old_total_working_balance))

    new_working_balance = lim
    new_total_working_balance = old_total_working_balance + new_working_balance - old_working_balance

    print("New working bal", convert_to_string(new_working_balance))
    print("New total working bal", convert_to_string(new_total_working_balance))

    return new_working_balance, new_total_working_balance