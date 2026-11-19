from ptcgo.game.card_effects.attacks_common import bonus_if
from ptcgo.game.card_effects.passives_common import has_team_plasma
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


def _defender_is_team_plasma(ctx) -> bool:
    defender = ctx.defender
    return defender is not None and has_team_plasma(ctx.board, defender)


card = PokemonCardDef(
    guid="9c2679ea-c58b-549e-891f-e766f2108cc7",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sawk.Name",
    display_name="Sawk",
    searchable_by=["Sawk", "Basic", "Sawk"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="BW10",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=539,
    abilities=[
        Attack(
            title="Kick of Righteousness",
            game_text="If the Defending Pok\u00e9mon is a Team Plasma Pok\u00e9mon, this attack does 40 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=bonus_if(_defender_is_team_plasma, 40),
        ),
        Attack(
            title="Low Sweep",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)