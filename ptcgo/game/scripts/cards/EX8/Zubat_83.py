from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4dcc1fe2-60bd-5277-8de2-c27883aece0d",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name",
    display_name="Zubat",
    searchable_by=["Zubat", "Basic", "Zubat"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="EX8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=41,
    abilities=[
        Ability(
            title="Self-control",
            game_text="Zubat can't be Paralyzed.",
            effect=unimplemented,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)