from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.passives_common import (
    attacker_is_basic, is_in_active_spot,
)
from ptcgo.game.session.passives import Passive


_is_basic = attacker_is_basic()


class _DisgustingPollenPassive(Passive):
    """"As long as this Pokemon is your Active Pokemon, your opponent's Basic
    Pokemon can't attack." A stage test rather than a name test, so every
    Basic the opponent controls is covered, promoted ones included."""

    def blocks_attack(self, pokemon, carrier):
        return (is_in_active_spot(carrier)
                and pokemon.owning_player_id != carrier.owning_player_id
                and _is_basic(pokemon))



card = PokemonCardDef(
    guid="d653ecab-8125-525c-95b2-a407c015bc63",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name",
    display_name="Vileplume",
    searchable_by=["Vileplume", "Stage 2", "Vileplume"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="SM3",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Disgusting Pollen",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, your opponent's Basic Pok\u00e9mon can't attack.",
            passive=_DisgustingPollenPassive(),
        ),
        Attack(
            title="Downer Shock",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Asleep. If tails, your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True, tails_conditions=(SpecialConditions.CONFUSED,)),
        ),
    ],
)