from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if, count_in_play


def _opponent_has_tag_team(ctx):
    return count_in_play(
        "opponent", lambda p: "TAG TEAM" in subtypes_for(p.archetype_id))(ctx) > 0

card = PokemonCardDef(
    guid="0fa9c356-157f-5863-9ef8-0b2b36db10fd",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heracross.Name",
    display_name="Heracross",
    searchable_by=["Heracross", "Basic", "Heracross"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=214,
    abilities=[
        Attack(
            title="Lunge Out",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Riled Horn",
            game_text="If your opponent has any TAG TEAM Pok\u00e9mon in play, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=bonus_if(_opponent_has_tag_team, 70),
        ),
    ],
)