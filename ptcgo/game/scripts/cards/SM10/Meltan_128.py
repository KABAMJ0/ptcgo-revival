from ptcgo.game.card_effects.attacks_common import active_is, bonus_if
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID

def _meltan_is_type(pokemon):
    return PokemonTypes.METAL.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])

card = PokemonCardDef(
    guid="358eedf0-3098-564b-97df-18cea3744e66",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    display_name="Meltan",
    searchable_by=["Meltan", "Basic", "Meltan"],
    subtypes=["Basic"],
    collector_number=128,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=808,
    abilities=[
        Attack(
            title="Steel Melt",
            game_text="If your opponent's Active Pok\u00e9mon is a Metal Pok\u00e9mon, this attack does 40 more damage.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            damage_operator="+",
            effect=bonus_if(active_is(_meltan_is_type), 40),
        ),
    ],
)