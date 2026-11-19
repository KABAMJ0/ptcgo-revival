from ptcgo.game.attributes import AttrID


def _team_basic():
    """(target, carrier) pred: your Basic Pokemon whose printed name carries
    "Team Rocket's" -- the wording names a GROUP, not this Pokemon."""
    named = pokemon_named("team rocket")

    def pred(target, carrier):
        return (target.owning_player_id == carrier.owning_player_id
                and target.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
                and named(target))

    return pred


from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonStage
from ptcgo.game.card_effects.passives_common import (
    attack_effect_shield_passive, pokemon_named,
)
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7faedbc4-7b4d-5527-b261-fb62cdbe2391",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsArticuno.Name",
    display_name="Team Rocket's Articuno",
    searchable_by=["Team Rocket's Articuno", "Basic", "TeamRocketsArticuno"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=144,
    abilities=[
        Ability(
            title="Repelling Veil",
            game_text="Prevent all effects of attacks used by your opponent's Pok\u00e9mon done to your Basic Team Rocket's Pok\u00e9mon. (Existing effects are not removed. Damage is not an effect.)",
            passive=attack_effect_shield_passive(protects=_team_basic()),

        ),
        Attack(
            title="Dark Frost",
            game_text="If this Pok\u00e9mon has any Team Rocket's Energy attached, this attack does 60 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)