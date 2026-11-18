from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="179c4def-75f9-557d-a970-6d5730eed36d",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Furfrou.Name",
    display_name="Furfrou",
    searchable_by=["Furfrou", "Basic", "Furfrou"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=676,
    abilities=[
        Attack(
            title="Tight Jaw",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Sharp Fang",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)