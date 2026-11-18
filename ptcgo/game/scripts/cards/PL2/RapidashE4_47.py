from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f16c4527-e467-5465-8ef7-30365b797253",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RapidashE4.Name",
    display_name="Rapidash E4",
    searchable_by=["Rapidash E4", "Basic", "SP", "RapidashE4"],
    subtypes=["Basic", "SP"],
    collector_number=47,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    family_id=78,
    abilities=[
        Attack(
            title="Pickup Power",
            game_text="Flip 3 coins. For each heads, search your discard pile for a basic Energy card, show it to your opponent, and put it into your hand.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Fire Mane",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
    ],
)