import pytest
from brownie import config
from brownie import Contract


@pytest.fixture
def deployer(accounts):
    yield accounts[0]


@pytest.fixture
def user(accounts):
    yield accounts[1]


@pytest.fixture
def crv():
    crv_address = Contract("0xD533a949740bb3306d119CC777fa900bA034cd52")
    yield crv_address

@pytest.fixture
def frax():
    frax_address = Contract("0x853d955aCEf822Db058eb8505911ED77F175b99e")
    yield frax_address

@pytest.fixture
def frax_amount(user, accounts, frax):
    amount = 5000 * 1e18
    frax_whale = accounts.at("0x13Cc34Aa8037f722405285AD2C82FE570bfa2bdc", force=True)
    frax.transfer(user, amount, {'from':frax_whale})
    yield frax_amount

@pytest.fixture
def deneme_contract(Deneme, user, deployer):
    deneme_contract_address = deployer.deploy(Deneme)
    yield deneme_contract_address

@pytest.fixture
def weth():
    weth_address = Contract("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
    yield weth_address

@pytest.fixture
def booster():
    booster_address = Contract("0xF403C135812408BFbE8713b5A23a04b3D48AAE31")
    yield booster_address

@pytest.fixture
def ve_crv():
    ve_crv_address = Contract("0x5f3b5DfEb7B28CDbD7FAba78963EE202a494e2A2")
    yield ve_crv_address

@pytest.fixture
def ve_bal():
    ve_bal_address = Contract("0xC128a9954e6c874eA3d62ce62B468bA073093F25")
    yield ve_bal_address 

@pytest.fixture
def bal_gauge_controller():
    bal_gauge_controller_address = Contract("0xC128468b7Ce63eA702C1f104D55A2566b13D3ABD")
    yield bal_gauge_controller_address 

@pytest.fixture
def bal_steth_gauge():
    bal_steth_gauge_address = Contract("0xcD4722B7c24C29e0413BDCd9e51404B4539D14aE")
    yield bal_steth_gauge_address

@pytest.fixture
def aura_voter_proxy():
    aura_voter_proxy_address = Contract("0xaF52695E1bB01A16D33D7194C28C42b10e0Dbec2")
    yield aura_voter_proxy_address 

@pytest.fixture
def aura_token():
    aura_token_address = Contract("0xC0c293ce456fF0ED870ADd98a0828Dd4d2903DBF")
    yield aura_token_address

@pytest.fixture
def aura_reward_pool_steth():
    aura_reward_pool_steth_address = Contract("0xe4683Fe8F53da14cA5DAc4251EaDFb3aa614d528")
    yield aura_reward_pool_steth_address

@pytest.fixture
def voter_proxy():
    voter_proxy_address = Contract("0x989AEb4d175e16225E39E87d0D97A3360524AD80")
    yield voter_proxy_address

@pytest.fixture
def gauge_controller():
    gauge_controller_address = Contract("0x2F50D538606Fa9EDD2B11E2446BEb18C9D5846bB")
    yield gauge_controller_address

@pytest.fixture
def usdn_pool_gauge():
    usdn_pool_gauge_address = Contract("0xF98450B5602fa59CC66e1379DFfB6FDDc724CfC4")
    yield usdn_pool_gauge_address

@pytest.fixture
def usdd_pool_gauge():
    usdd_pool_gauge_address = Contract("0xd5d3efC90fFB38987005FdeA303B68306aA5C624")
    yield usdd_pool_gauge_address

@pytest.fixture
def tusd_pool_gauge():
    tusd_pool_gauge_address = Contract("0x359FD5d6417aE3D8D6497d9B2e7A890798262BA4")
    yield tusd_pool_gauge_address 

@pytest.fixture
def busd_pool_gauge():
    busd_pool_gauge_address = Contract("0x69fb7c45726cfe2badee8317005d3f94be838840")
    yield busd_pool_gauge_address 

@pytest.fixture
def frax_pool_gauge():
    frax_pool_gauge_address = Contract("0x72e158d38dbd50a483501c24f792bdaaa3e7d55c")
    yield frax_pool_gauge_address

@pytest.fixture
def mim_pool_gauge():
    mim_pool_gauge_address = Contract("0xd8b712d29381748dB89c36BCa0138d7c75866ddF")
    yield mim_pool_gauge_address

@pytest.fixture
def steth_pool_gauge():
    steth_pool_gauge_address = Contract("0x182b723a58739a9c974cfdb385ceadb237453c28")
    yield steth_pool_gauge_address

@pytest.fixture
def mim_pool():
    mim_pool_address = Contract("0x5a6A4D54456819380173272A5E8E9B9904BdF41B")
    yield mim_pool_address

@pytest.fixture
def usdn():
    usdn_address = Contract("0x674C6Ad92Fd080e4004b2312b45f796a192D27a0")
    yield usdn_address 

@pytest.fixture
def usdn_pool():
    usdn_pool_address = Contract("0x0f9cb53Ebe405d49A0bbdBD291A65Ff571bC83e1")
    yield usdn_pool_address  

@pytest.fixture
def usdn_lp_token():
    usdn_lp_token_address = Contract("0x4f3E8F405CF5aFC05D68142F3783bDfE13811522")
    yield usdn_lp_token_address

@pytest.fixture
def usdn_reward_pool():
    usdn_reward_pool_address = Contract("0x4a2631d090e8b40bBDe245e687BF09e5e534A239")
    yield usdn_reward_pool_address 

@pytest.fixture
def mim_reward_pool():
    mim_reward_pool_address = Contract("0xFd5AbF66b003881b88567EB9Ed9c651F14Dc4771")
    yield mim_reward_pool_address

@pytest.fixture
def steth_reward_pool():
    steth_reward_pool_address = Contract("0x0A760466E1B4621579a82a39CB56Dda2F4E70f03")
    yield steth_reward_pool_address

@pytest.fixture
def _3crv():
    _3crv_address = Contract("0x6c3F90f043a72FA612cbac8115EE7e52BDe6E490")
    yield _3crv_address

@pytest.fixture
def _3crv_whale(accounts):
    _3crv_whale = accounts.at("0xe74b28c2eAe8679e3cCc3a94d5d0dE83CCB84705", force=True)
    yield _3crv_whale

@pytest.fixture
def usdn_whale(accounts):
    usdn_whale = accounts.at("0x868d94B174bed780717Cf62E7eD31653638d5948", force=True)
    yield usdn_whale

@pytest.fixture
def amount():
    amount = 100_000 * 1e18
    yield amount

@pytest.fixture
def mint_3crv(user, accounts, amount, _3crv):
    _3crv_whale = accounts.at("0xe74b28c2eAe8679e3cCc3a94d5d0dE83CCB84705", force=True)
    _3crv.transfer(user, amount, {'from':_3crv_whale})
    yield mint_3crv

