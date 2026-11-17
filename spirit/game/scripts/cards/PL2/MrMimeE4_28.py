from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bc05653e-3bcb-5ebb-a7b7-f91822a819c5",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMimeE4.Name",
    display_name="Mr. Mime E4",
    searchable_by=["Mr. Mime E4", "Basic", "SP", "MrMimeE4"],
    subtypes=["Basic", "SP"],
    collector_number=28,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=122,
    abilities=[
        Attack(
            title="Magic Heal",
            game_text="Flip 3 coins. Remove a number of damage counters equal to the number of heads from your Pok\u00e9mon in any way you like.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Barrier Attack",
            game_text="During your opponent's next turn, any damage done to Mr. Mime E4 by attacks is reduced by 10 (after applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)