
#include <iostream>
#include <fstream>
#include <bitset>
#include <string>
#include <unordered_set>
using namespace std;

constexpr size_t N = 12;

unsigned short gamma(vector<unsigned short> const & decimals)
{
	size_t bit_counts[N]{};
	for (auto const val : decimals)
	{
		for (size_t i = 0; i < N; ++i)
		{
			if ((val >> i) & 1) bit_counts[i]++;
		}
	}
	unsigned short power = 1;
	unsigned short gamma = 0;
	size_t const sz = decimals.size();
	size_t half = (sz % 2 == 0 ? sz / 2 : sz / 2 + 1);
	for (size_t i = 0; i < N; ++i)
	{
		if (bit_counts[i] >= half) gamma += power;
		power *= 2;
	}
	return gamma;
}

unsigned short epsilon(unsigned short gamma)
{
	return ((1 << N) - 1) ^ gamma;
}

unsigned short epsilon(vector<unsigned short> const& decimals)
{
	return epsilon(gamma(decimals));
}

unsigned short extract_molecule_rating(vector<unsigned short> const& decimals, unsigned short(*bit_criteria)(vector<unsigned short> const&))
{
	vector<unsigned short> molecule_decs = decimals;
	for (size_t i = 0; i < N; ++i)
	{
		size_t const comp = (*bit_criteria)(molecule_decs);

		vector<unsigned short> tmp;
		size_t idx = N - 1 - i;
		unsigned short val = (comp >> idx & 1);
		for (auto& molecule_dec : molecule_decs)
		{
			if (((molecule_dec >> idx) & 1) == val) tmp.push_back(molecule_dec);
		}
		molecule_decs = tmp;
		if (molecule_decs.size() == 1) break;
	}
	return molecule_decs[0];
}


int main()
{
	ifstream input("input.txt");
	string bitstring = ""; 
	vector<unsigned short> decimals;
	while (input >> bitstring)
	{
		decimals.push_back(stoi(bitstring, 0, 2));
	}
	input.close();

	//part1 (cast to uint since 2^24 is bigger than an unsigned short).
	unsigned short const g = gamma(decimals);
	unsigned short const e = epsilon(g);
	cout << " Part 1 : " << static_cast<unsigned>(g) * static_cast<unsigned>(e) << endl;

	//o2
	unsigned short(*o2_bit_criteria)(vector<unsigned short> const&) = &gamma;
	unsigned short const o2_rating = extract_molecule_rating(decimals, o2_bit_criteria);

	//co2
	unsigned short(*co2_bit_criteria)(vector<unsigned short> const&) = &epsilon;
	unsigned short const co2_rating = extract_molecule_rating(decimals, co2_bit_criteria);

	//part2 (cast to uint since 2^24 is bigger than an unsigned short).
	cout << " Part 2 : " << static_cast<unsigned>(o2_rating) * static_cast<unsigned>(co2_rating) << endl;
	return 0;
}
