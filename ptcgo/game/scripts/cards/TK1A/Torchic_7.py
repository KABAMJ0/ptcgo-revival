from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b832f417-0f18-53fd-90e9-430d555d35de",
    key="TK1A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name",
    display_name="Torchic",
    searchable_by=["Torchic", "Basic", "Torchic"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="TK1A",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=255,
    abilities=[
        Attack(
            title="Firebreathing",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)