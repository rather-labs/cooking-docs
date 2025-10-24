This definition should be used all number representation except input fields.
Cooking uses comas as a thousand divider and a single point as the decimal divider, i.e. 999,999.99
When hovering over a formatted value, the frontend should display a tooltip with the complete value unless strictly specified otherwise.
## Definition
- Numbers bigger than 999,999 -> 'n' M (no decimal places)
	- $10 M -> $10,000,000.12
	- 2 M % -> 2,123,456.012345 %
	- 234 M SOL -> 234,003,193.001236 SOL
- Numbers bigger than 99,999 -> 'n' K (up to 2 decimal places for the first hundred places)
	- $5.87 K -> $5,866.12 (bigger than 5 rounds up)
	- 19.44 K % -> 19,442.023135 %
	- 48.12 K SOL -> 48,123.112345 SOL
- Numbers smaller than 999 -> 'n'.dd (up to 2 decimal places. Values bigger than 5 rounds up)
	- $193.01 -> $193.012345
	- 10.34 % -> 10.340145 %
	- 50.12 SOL -> 50.120423 SOL
- Solana values smaller than 10 and the first 3 decimal places != 0 -> 'n'.dddddd (up to 6 decimal places. Values bigger than 5 rounds up)
	- 9.012345
- Solana values smaller than 10 and the first 3 decimal places = 0 -> 'n'.dₙddd (subscript value represents the amount of 0 before the first three non-zero values. Values bigger than 5 rounds up)
