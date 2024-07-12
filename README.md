# Quantower-Trading-Analytics-Basic

The purpose of this python script was to access the builtin db to a specific Quantower Connection and pull all the trades that have been taken on this particular connection. 

![image](https://github.com/user-attachments/assets/662d5446-7a5f-487b-b710-7e8f2c88dcae)

It can be further refined to filter down to individual accounts or symbol id if need be:

trade_id | symbol_id | account_id | time | price | quantity | side | position_impact_type | gross_pnl_value | gross_pnl_asset | net_pnl_value | net_pnl_asset | fee_value | fee_asset | order_id | order_type_id | position_id | comment
--------------------------------------------------
1034385 | MNQZ2@CME | APEX-27***-01 | 638058177357434500 | 11982.0 | 4.0 | 0 | 1 | 0.0 | USD | None | None | None | None | 29053944 | Limit | MNQZ2@CME@APEX-27***-01 | None
1035130 | MNQZ2@CME | APEX-27***-01 | 638058187652748100 | 11978.0 | 4.0 | 1 | 1 | -32.0 | USD | None | None | None | None | 29054042 | Market | MNQZ2@CME@APEX-27100-01 | None
1043026 | MNQZ2@CME | APEX-27***-01 | 638058240908950470 | 11961.0 | 1.0 | 0 | 1 | 0.0 | USD | None | None | None | None | 29078113 | Limit | MNQZ2@CME@APEX-27***-01 | None
1043029 | MNQZ2@CME | APEX-27***-01 | 638058240910030230 | 11961.0 | 3.0 | 0 | 1 | 0.0 | USD | None | None | None | None | 29078113 | Limit | MNQZ2@CME@APEX-27***-01 | None
1043406 | MNQZ2@CME | APEX-27***-01 | 638058241282494750 | 11955.0 | 3.0 | 1 | 1 | -36.0 | USD | None | None | None | None | 29080267 | Market | MNQZ2@CME@APEX-27100-01 | None


