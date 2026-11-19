from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if
from ptcgo.game.card_effects.pokemon import has_pokemon_subtype


def _stage2_darkness_on_bench(ctx) -> bool:
    """A Stage 2 Darkness Pokemon of yours sits on your Bench."""
    for pokemon in ctx.my_bench():
        if PokemonTypes.DARKNESS.value not in (
                pokemon.get_attribute(AttrID.POKEMON_TYPES) or []):
            continue
        if has_pokemon_subtype(pokemon, "Stage 2"):
            return True
    return False


card = PokemonCardDef(
    guid="375c5611-ec4e-5603-be08-9556de5d0145",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name",
    display_name="Sableye",
    searchable_by=["Sableye", "Basic", "Sableye"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="ME2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=302,
    abilities=[
        Attack(
            title="Cocky Claw",
            game_text="If you have any Stage 2 Darkness Pok\u00e9mon on your Bench, this attack does 70 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(_stage2_darkness_on_bench, 70),
        ),
    ],
)