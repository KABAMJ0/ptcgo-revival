from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cc511eff-c5f7-5c3e-8dbf-041c0834bba3",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlakazamE4.Name",
    display_name="Alakazam E4",
    searchable_by=["Alakazam E4", "Basic", "SP", "AlakazamE4"],
    subtypes=["Basic", "SP"],
    collector_number=38,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=65,
    abilities=[
        Attack(
            title="Recover",
            game_text="Discard a Psychic Energy attached to Alakazam E4 and remove 4 damage counters from Alakazam E4.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Mysterious Beam",
            game_text="Flip a coin. If heads, discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)