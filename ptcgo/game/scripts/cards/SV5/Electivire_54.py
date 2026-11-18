from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.card_effects.attacks_common import bonus_if, count_in_play
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID

_is_water = lambda pokemon: PokemonTypes.WATER.value in (
    pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])
_water_in_play = lambda ctx: count_in_play("opponent", _is_water)(ctx) > 0


card = PokemonCardDef(
    guid="e484696e-b0fb-583f-86cf-46ca09e182f3",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electivire.Name",
    display_name="Electivire",
    searchable_by=["Electivire", "Stage 1", "Electivire"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    family_id=125,
    abilities=[
        Attack(
            title="Short-Circuit Knuckle",
            game_text="If your opponent has any Water Pok\u00e9mon in play, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=bonus_if(_water_in_play, 120),
        ),
        Attack(
            title="Electroslug",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
    ],
)