from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.effects import is_evolution_pokemon
from ptcgo.game.card_effects.attacks_common import bonus_if
from ptcgo.game.card_effects.passives_common import takes_less_passive


def _not_fire(attacker) -> bool:
    """The attackers Fluffy answers: every non-Fire Pokemon."""
    types = attacker.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.FIRE.value not in types


card = PokemonCardDef(
    guid="d39573d3-372f-5739-a302-9eaa257cd1ba",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bewear.Name",
    display_name="Bewear",
    searchable_by=["Bewear", "Stage 1", "Bewear"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="SM4",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name",
    family_id=759,
    abilities=[
        Ability(
            title="Fluffy",
            game_text="This Pok\u00e9mon takes 30 less damage from the attacks of your opponent's non-Fire Pok\u00e9mon (after applying Weakness and Resistance).",
            passive=takes_less_passive(30, attacker_pred=_not_fire),
        ),
        Attack(
            title="Cross-Cut",
            game_text="If your opponent's Active Pok\u00e9mon is an Evolution Pok\u00e9mon, this attack does 60 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(lambda ctx: is_evolution_pokemon(ctx.defender), 60),
        ),
    ],
)