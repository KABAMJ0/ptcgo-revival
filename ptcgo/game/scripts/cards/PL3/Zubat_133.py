from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bcb05794-0244-55e2-95b5-480fcccaea7c",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name",
    display_name="Zubat",
    searchable_by=["Zubat", "Basic", "Zubat"],
    subtypes=["Basic"],
    collector_number=133,
    set_code="PL3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=41,
    abilities=[
        Attack(
            title="Quick Turn",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)