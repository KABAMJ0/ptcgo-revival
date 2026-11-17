from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9a08258a-fc7a-5200-9a95-9fd4688c6c99",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Basculin.Name",
    display_name="Basculin",
    searchable_by=["Basculin", "Basic", "Basculin"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="RSV10PT5",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=550,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Bared Fangs",
            game_text="If your opponent's Active Pok\u00e9mon has no damage counters on it before this attack does damage, this attack does nothing.",
            cost={PokemonTypes.WATER: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)