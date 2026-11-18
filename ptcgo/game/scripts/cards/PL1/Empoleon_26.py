from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="df95961c-61d9-5414-9fd8-937e2879b18c",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Empoleon.Name",
    display_name="Empoleon",
    searchable_by=["Empoleon", "Stage 2", "Empoleon"],
    subtypes=["Stage 2"],
    collector_number=26,
    set_code="PL1",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    family_id=393,
    abilities=[
        Attack(
            title="Knock Off",
            game_text="Choose 1 card from your opponent's hand without looking and discard it.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Jet Smash",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 70 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Empoleon can't use Jet Smash during your next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)