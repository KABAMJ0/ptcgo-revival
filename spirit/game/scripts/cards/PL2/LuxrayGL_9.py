from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="269c40c6-12c4-59b1-9690-58cb7b0e151f",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LuxrayGL.Name",
    display_name="Luxray GL",
    searchable_by=["Luxray GL", "Basic", "SP", "LuxrayGL"],
    subtypes=["Basic", "SP"],
    collector_number=9,
    set_code="PL2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=405,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Trash Bolt",
            game_text="Discard an Energy card from your hand. (If you can't discard a card from your hand, this attack does nothing.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=unimplemented,
        ),
    ],
)