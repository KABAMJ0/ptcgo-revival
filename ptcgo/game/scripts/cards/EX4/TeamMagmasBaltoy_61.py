from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import place_counters

card = PokemonCardDef(
    guid="a48e3f4a-4220-576a-b5ab-4a7de4062424",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasBaltoy.Name",
    display_name="Team Magma's Baltoy",
    searchable_by=["Team Magma's Baltoy", "Basic", "TeamMagmasBaltoy"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=343,
    abilities=[
        Attack(
            title="Night Attack",
            game_text="Put 1 damage counter on 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=place_counters(1, target="choose_any_opponent"),
        ),
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)