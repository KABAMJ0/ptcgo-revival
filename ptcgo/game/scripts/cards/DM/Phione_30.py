from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

from ptcgo.game.card_effects.passives_common import condition_immunity_passive
from ptcgo.game.attributes import AttrID, SpecialConditions
from ptcgo.game.session import passives as _passives


def _water_pokemon(pokemon, carrier):
    if pokemon.owning_player_id != carrier.owning_player_id:
        return False
    return PokemonTypes.WATER.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


_murmurs = condition_immunity_passive([SpecialConditions.CONFUSED], protects=_water_pokemon)

card = PokemonCardDef(
    guid="10baa9bb-8f5c-59f6-97d3-ca0c27dc8dd2",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phione.Name",
    display_name="Phione",
    searchable_by=["Phione", "Basic", "Phione"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="DM",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=489,
    abilities=[
        Ability(
            title="Murmurs of the Sea",
            game_text="Your Water Pok\u00e9mon can't be Confused. If those Pok\u00e9mon are already Confused, remove that Special Condition.",
            passive=_murmurs,
        ),
        Attack(
            title="Water Pulse",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)