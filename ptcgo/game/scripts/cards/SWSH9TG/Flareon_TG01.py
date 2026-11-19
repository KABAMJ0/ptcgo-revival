from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.passives_common import ability_lock_passive


def _has_memory_capsule(pokemon):
    return any(
        getattr(def_for(child.archetype_id), "display_name", None) == "Memory Capsule"
        for child in pokemon.children
    )


def _grass_lock(pokemon, carrier):
    if not _has_memory_capsule(carrier):
        return False
    return PokemonTypes.GRASS.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="ca031865-c59c-5bde-ac4d-2abbe3f65b85",
    key="SWSH9TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name",
    display_name="Flareon",
    searchable_by=["Flareon", "Stage 1", "Flareon"],
    subtypes=["Stage 1"],
    collector_number=1,
    set_code="SWSH9TG",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Incandescent Awakening",
            game_text="If this Pok\u00e9mon has a Memory Capsule attached, Grass Pok\u00e9mon in play (both yours and your opponent's) have no Abilities.",
            passive=ability_lock_passive(_grass_lock),
        ),
        Attack(
            title="Fire Mane",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)