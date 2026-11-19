from ptcgo.game.card_effects.support_common import remove_self_from_play
from ptcgo.game.card_effects.passives_common import ability_lock_passive
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, is_pokemon_v, subtypes_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _basic_pokemon_v(pokemon, carrier):
    return "Basic" in subtypes_for(pokemon.archetype_id) \
        and is_pokemon_v(pokemon.archetype_id)
card = PokemonCardDef(
    guid="ef58dc18-0ff5-54dd-818f-15a8c07e62c8",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=158,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=442,
    abilities=[
        Ability(
            title="Fettered in Misfortune",
            game_text="Basic Pok\u00e9mon V in play (both yours and your opponent's) have no Abilities.",
            passive=ability_lock_passive(_basic_pokemon_v),
        ),
        Attack(
            title="Fade Out",
            game_text="Put this Pok\u00e9mon and all attached cards into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=remove_self_from_play(destination="hand", with_attachments="same"),
        ),
    ],
)