pragma solidity 0.8.17;

interface IApprove {
    function approve(address spender, uint256 amount) external returns (bool);
}

interface ICurveFi {
    function add_liquidity(
        // USDbtc pool
        uint256[] calldata amounts,
        uint256 min_mint_amount
    ) external returns (uint256);

    function coins() external view returns (address[] memory s);

    // function add_liquidity(
    //     // stETH pool
    //     uint256[2] calldata amounts,
    //     uint256 min_mint_amount,
    //     bool use_underlying
    // ) external returns (uint256);
}
contract Tryme {
    ICurveFi public constant pool = ICurveFi(0xDcEF968d416a41Cdac0ED8702fAC8128A64241A2);
    address public constant token = 0x853d955aCEf822Db058eb8505911ED77F175b99e; // frax
    address[] public x;
    function addLiq() external {
        x = ICurveFi(pool).coins();
    }
}

