from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.passives_common import ability_lock_passive


def _has_memory_capsule(carrier):
    for child in carrier.children:
        d = def_for(child.archetype_id)
        if d and d.display_name == "Memory Capsule":
            return True
    return False


def _fire_locked(pokemon, carrier):
    if not _has_memory_capsule(carrier):
        return False
    return PokemonTypes.FIRE.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="cabf8d14-3e00-555c-99dc-425f7c333f95",
    key="SWSH9TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeon.Name",
    display_name="Vaporeon",
    searchable_by=["Vaporeon", "Stage 1", "Vaporeon"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="SWSH9TG",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Torrential Awakening",
            game_text="If this Pok\u00e9mon has a Memory Capsule attached, Fire Pok\u00e9mon in play (both yours and your opponent's) have no Abilities.",
            passive=ability_lock_passive(_fire_locked),
        ),
        Attack(
            title="Aurora Beam",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)